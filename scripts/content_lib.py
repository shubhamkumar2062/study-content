"""Shared code for validate.py and build.py.

Standard library only, so anyone with Python 3.9+ can run the checks.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"
SCHEMA = ROOT / "schema"
PUBLIC = ROOT / "public"
CONTENT_FORMAT = 1          # bump only for a change older apps can't read; publish it under /v2/
MIN_APP_VERSION = 1         # apps older than this are told to update
OUTPUT = PUBLIC / f"v{CONTENT_FORMAT}"

IMAGE_LINK = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


# ---------------------------------------------------------------------------
# Error collection
# ---------------------------------------------------------------------------

@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, where: Path | str, message: str) -> None:
        self.errors.append(f"{rel(where)}: {message}")

    def warn(self, where: Path | str, message: str) -> None:
        self.warnings.append(f"{rel(where)}: {message}")


def rel(path: Path | str) -> str:
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------------------
# A small JSON Schema checker (the subset our schemas use)
# ---------------------------------------------------------------------------

_TYPES = {
    "object": dict, "array": list, "string": str, "boolean": bool, "null": type(None),
}


def _is_type(value, name: str) -> bool:
    if name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, _TYPES[name])


def check_schema(value, schema: dict, root: dict, path: str, out: list[str]) -> None:
    if "$ref" in schema:
        ref = schema["$ref"]
        assert ref.startswith("#/definitions/"), ref
        schema = root["definitions"][ref.split("/")[-1]]
    if "enum" in schema and value not in schema["enum"]:
        out.append(f"{path}: {json.dumps(value)} is not one of {schema['enum']}")
        return
    expected = schema.get("type")
    if expected and not _is_type(value, expected):
        out.append(f"{path}: expected {expected}, found {type(value).__name__}")
        return
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            out.append(f"{path}: must be at least {schema['minLength']} characters")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            out.append(f"{path}: {value!r} does not match {schema['pattern']}")
    if _is_type(value, "number"):
        if "minimum" in schema and value < schema["minimum"]:
            out.append(f"{path}: {value} is below the minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            out.append(f"{path}: {value} is above the maximum {schema['maximum']}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            out.append(f"{path}: needs at least {schema['minItems']} items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            out.append(f"{path}: allows at most {schema['maxItems']} items")
        if "items" in schema:
            for i, item in enumerate(value):
                check_schema(item, schema["items"], root, f"{path}[{i}]", out)
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                out.append(f"{path}: missing required field '{key}'")
        props = schema.get("properties", {})
        for key, item in value.items():
            if key in props:
                check_schema(item, props[key], root, f"{path}.{key}", out)
            elif schema.get("additionalProperties") is False:
                out.append(f"{path}: unknown field '{key}'")


_schema_cache: dict[str, dict] = {}


def load_json(path: Path, report: Report, schema_name: str | None = None):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        report.error(path, "file not found")
        return None
    except json.JSONDecodeError as exc:
        report.error(path, f"not valid JSON (line {exc.lineno}, column {exc.colno}): {exc.msg}")
        return None
    if schema_name:
        if schema_name not in _schema_cache:
            _schema_cache[schema_name] = json.loads((SCHEMA / schema_name).read_text(encoding="utf-8"))
        schema = _schema_cache[schema_name]
        problems: list[str] = []
        check_schema(data, schema, schema, "$", problems)
        for problem in problems:
            report.error(path, problem)
        if problems:
            return None
    return data


# ---------------------------------------------------------------------------
# Ids
# ---------------------------------------------------------------------------

def code_slug(code: str) -> str:
    """Folder and URL form of a subject code: BP301T -> bp301t, N-NF(I)125 -> n-nf-i-125."""
    slug = re.sub(r"[^a-z0-9]+", "-", code.lower()).strip("-")
    return slug


def subject_id(stream: str, programme: str, scheme: str, term: str, code: str) -> str:
    return ".".join([stream, programme, scheme, term, code_slug(code)])


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def read_markdown(path: Path, report: Report) -> tuple[dict, str] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        report.error(path, "file not found")
        return None
    meta: dict[str, str] = {}
    match = FRONT_MATTER.match(text)
    if match:
        for line in match.group(1).splitlines():
            if not line.strip():
                continue
            if ":" not in line:
                report.error(path, f"front-matter line without 'key: value': {line!r}")
                continue
            key, val = line.split(":", 1)
            meta[key.strip()] = val.strip()
        text = text[match.end():]
    if not text.strip():
        report.error(path, "has no text after the front-matter")
    return meta, text


# ---------------------------------------------------------------------------
# Catalog
# ---------------------------------------------------------------------------

@dataclass
class CatalogSubject:
    id: str
    stream: str
    programme: str
    scheme: str
    term: str
    code: str
    title: str
    kind: str
    linked_theory: str | None
    scheme_status: str


@dataclass
class Catalog:
    exam_bodies: list[dict]
    streams: list[dict]
    subjects: dict[str, CatalogSubject]                     # by subject id
    by_term: dict[tuple[str, str, str, str], dict[str, CatalogSubject]]  # code -> subject


def load_catalog(report: Report) -> Catalog | None:
    bodies_doc = load_json(SOURCE / "exam-bodies.json", report, "exam-bodies.schema.json")
    body_ids: set[str] = set()
    if bodies_doc:
        for body in bodies_doc["examBodies"]:
            if body["id"] in body_ids:
                report.error(SOURCE / "exam-bodies.json", f"duplicate exam body id '{body['id']}'")
            body_ids.add(body["id"])

    streams: list[dict] = []
    subjects: dict[str, CatalogSubject] = {}
    by_term: dict[tuple[str, str, str, str], dict[str, CatalogSubject]] = {}
    catalog_dir = SOURCE / "catalog"
    files = sorted(catalog_dir.glob("*.json"))
    if not files:
        report.error(catalog_dir, "no catalog files")
    for path in files:
        stream = load_json(path, report, "catalog-stream.schema.json")
        if not stream:
            continue
        if stream["id"] != path.stem:
            report.error(path, f"stream id '{stream['id']}' must match the file name '{path.stem}'")
        streams.append(stream)
        seen_prog: set[str] = set()
        for prog in stream["programmes"]:
            if prog["id"] in seen_prog:
                report.error(path, f"duplicate programme id '{prog['id']}'")
            seen_prog.add(prog["id"])
            if body_ids and prog["examBodyId"] not in body_ids:
                report.error(path, f"programme '{prog['id']}' names unknown exam body '{prog['examBodyId']}'")
            seen_scheme: set[str] = set()
            for scheme in prog["schemes"]:
                if scheme["id"] in seen_scheme:
                    report.error(path, f"{prog['id']}: duplicate scheme id '{scheme['id']}'")
                seen_scheme.add(scheme["id"])
                if scheme["status"] == "not-sourced" and scheme["terms"]:
                    report.error(path, f"{prog['id']}.{scheme['id']}: a not-sourced scheme must not list terms")
                if scheme["status"] != "not-sourced" and not scheme.get("syllabusSource"):
                    report.error(path, f"{prog['id']}.{scheme['id']}: say which syllabus the subject list comes from (syllabusSource)")
                seen_term: set[str] = set()
                for term in scheme["terms"]:
                    if term["id"] in seen_term:
                        report.error(path, f"{prog['id']}.{scheme['id']}: duplicate term id '{term['id']}'")
                    seen_term.add(term["id"])
                    key = (stream["id"], prog["id"], scheme["id"], term["id"])
                    codes: dict[str, CatalogSubject] = {}
                    for subj in term["subjects"]:
                        sid = subject_id(*key, subj["code"])
                        if subj["code"] in codes or sid in subjects:
                            report.error(path, f"{'.'.join(key)}: duplicate subject code '{subj['code']}'")
                            continue
                        entry = CatalogSubject(
                            id=sid, stream=key[0], programme=key[1], scheme=key[2], term=key[3],
                            code=subj["code"], title=subj["title"], kind=subj["kind"],
                            linked_theory=subj.get("linkedTheory"), scheme_status=scheme["status"],
                        )
                        codes[subj["code"]] = entry
                        subjects[sid] = entry
                    for entry in codes.values():
                        if entry.linked_theory and entry.linked_theory not in codes:
                            report.error(path, f"{entry.id}: linkedTheory '{entry.linked_theory}' is not a subject of the same term")
                        if entry.linked_theory and entry.kind != "practical":
                            report.error(path, f"{entry.id}: only a practical can have linkedTheory")
                    by_term[key] = codes
    return Catalog(exam_bodies=(bodies_doc or {}).get("examBodies", []), streams=streams,
                   subjects=subjects, by_term=by_term)


# ---------------------------------------------------------------------------
# Subjects
# ---------------------------------------------------------------------------

@dataclass
class SubjectContent:
    entry: CatalogSubject
    folder: Path
    meta: dict
    pack: dict
    media: list[Path]


def find_subject_folders() -> list[Path]:
    root = SOURCE / "subjects"
    return sorted(p.parent for p in root.glob("*/*/*/*/*/subject.json")) if root.exists() else []


def check_stray_folders(report: Report) -> None:
    """Every folder under source/subjects must be on the stream/programme/scheme/term/code path."""
    root = SOURCE / "subjects"
    if not root.exists():
        return
    for path in root.rglob("*"):
        if path.name.startswith("."):
            continue
        parts = path.relative_to(root).parts
        if path.is_file() and len(parts) < 6:
            report.error(path, "file outside a subject folder (expected subjects/<stream>/<programme>/<scheme>/<term>/<code>/…)")
        if path.is_dir() and len(parts) == 5 and not (path / "subject.json").exists():
            report.error(path, "subject folder without subject.json")


def load_subject(folder: Path, catalog: Catalog, report: Report) -> SubjectContent | None:
    stream, programme, scheme, term, code_folder = folder.relative_to(SOURCE / "subjects").parts
    key = (stream, programme, scheme, term)
    term_subjects = catalog.by_term.get(key)
    if term_subjects is None:
        report.error(folder, f"no catalog term {'.'.join(key)} (orphan folder: add it to source/catalog/{stream}.json or move it)")
        return None
    entry = next((s for s in term_subjects.values() if code_slug(s.code) == code_folder), None)
    if entry is None:
        report.error(folder, f"no subject with code folder '{code_folder}' in catalog term {'.'.join(key)} (orphan folder)")
        return None
    if entry.kind not in ("theory", "elective", "mandatory", "qualifying"):
        report.error(folder, f"{entry.code} is a {entry.kind}; its guides belong in its linked theory subject's pack")

    errors_before = len(report.errors)
    meta = load_json(folder / "subject.json", report, "subject.schema.json")
    if meta is None:
        return None
    if meta["code"] != entry.code:
        report.error(folder / "subject.json", f"code '{meta['code']}' does not match the catalog code '{entry.code}'")
    if meta["title"] != entry.title:
        report.warn(folder / "subject.json", f"title differs from the catalog ('{meta['title']}' vs '{entry.title}')")

    unit_numbers = [u["number"] for u in meta["units"]]
    if len(set(unit_numbers)) != len(unit_numbers):
        report.error(folder / "subject.json", "duplicate unit numbers")

    def notes_of(rel_path: str) -> str | None:
        parsed = read_markdown(folder / rel_path, report)
        if parsed is None:
            return None
        md_meta, text = parsed
        check_images(folder / rel_path, text, folder, report)
        return text

    units = []
    for unit in sorted(meta["units"], key=lambda u: u["number"]):
        units.append({"number": unit["number"], "title": unit["title"], "markdown": notes_of(unit["notes"])})
    extras = []
    for extra in meta.get("extras", []):
        extras.append({"id": extra["id"], "title": extra["title"], "markdown": notes_of(extra["notes"])})

    practical_codes = meta.get("practicalCodes", [])
    for pcode in practical_codes:
        pentry = term_subjects.get(pcode)
        if pentry is None or pentry.kind != "practical":
            report.error(folder / "subject.json", f"practicalCodes: '{pcode}' is not a practical in the same term")
        elif pentry.linked_theory != entry.code:
            report.error(folder / "subject.json", f"practicalCodes: catalog entry {pcode} must have linkedTheory '{entry.code}'")
    practicals = []
    seen_practicals: set[str] = set()
    for prac in meta.get("practicals", []):
        if prac["id"] in seen_practicals:
            report.error(folder / "subject.json", f"duplicate practical id '{prac['id']}'")
        seen_practicals.add(prac["id"])
        practicals.append({"id": prac["id"], "title": prac["title"], "markdown": notes_of(prac["file"])})
    if practicals and not practical_codes:
        report.error(folder / "subject.json", "practical guides listed but practicalCodes is empty")

    ids: set[str] = set()

    def unique(where: Path, item_id: str) -> None:
        if item_id in ids:
            report.error(where, f"duplicate id '{item_id}'")
        ids.add(item_id)

    questions: list[dict] = []
    banks_ok = True
    qpath = folder / "questions.json"
    if qpath.exists():
        doc = load_json(qpath, report, "questions.schema.json")
        banks_ok = banks_ok and doc is not None
        if doc:
            questions = doc["questions"]
            for q in questions:
                unique(qpath, q["id"])
                if q["unit"] not in unit_numbers:
                    report.error(qpath, f"{q['id']}: unit {q['unit']} is not a unit of this subject")
                check_images(qpath, q["question"] + "\n" + q["answer"], folder, report)

    mcqs: list[dict] = []
    mpath = folder / "mcqs.json"
    if mpath.exists():
        doc = load_json(mpath, report, "mcqs.schema.json")
        banks_ok = banks_ok and doc is not None
        if doc:
            mcqs = doc["mcqs"]
            for m in mcqs:
                unique(mpath, m["id"])
                if m["unit"] not in unit_numbers:
                    report.error(mpath, f"{m['id']}: unit {m['unit']} is not a unit of this subject")
                if m["correct"] >= len(m["options"]):
                    report.error(mpath, f"{m['id']}: correct answer index {m['correct']} but only {len(m['options'])} options (counted from 0)")
                normalised = [o.strip().lower() for o in m["options"]]
                if len(set(normalised)) != len(normalised):
                    report.error(mpath, f"{m['id']}: two options are the same")

    tests: list[dict] = []
    tpath = folder / "mocktests.json"
    if tpath.exists():
        doc = load_json(tpath, report, "mocktests.schema.json")
        if doc:
            tests = doc["tests"]
            available = {
                "mcq": len(mcqs),
                "very-short": sum(1 for q in questions if q["type"] == "very-short"),
                "short": sum(1 for q in questions if q["type"] == "short"),
                "long": sum(1 for q in questions if q["type"] == "long"),
            }
            for t in tests:
                unique(tpath, t["id"])
                total = 0
                for s in t["sections"]:
                    if s["attempt"] > s["count"]:
                        report.error(tpath, f"{t['id']}.{s['id']}: attempt {s['attempt']} is more than the {s['count']} questions shown")
                    if banks_ok and available[s["source"]] < s["count"]:
                        report.error(tpath, f"{t['id']}.{s['id']}: needs {s['count']} '{s['source']}' questions but the bank has {available[s['source']]}")
                    total += s["attempt"] * s["marksEach"]
                if total != t["totalMarks"]:
                    report.error(tpath, f"{t['id']}: sections add up to {total} marks, but totalMarks is {t['totalMarks']}")

    media_dir = folder / "media"
    media = sorted(p for p in media_dir.iterdir() if p.is_file() and not p.name.startswith(".")) if media_dir.exists() else []
    referenced = referenced_media(folder)
    for path in media:
        if path.name not in referenced:
            report.warn(path, "image not used by any note or question")

    known = {"subject.json", "questions.json", "mcqs.json", "mocktests.json", "notes", "practicals", "media"}
    for child in folder.iterdir():
        if child.name not in known and not child.name.startswith("."):
            report.error(child, "unexpected file or folder in a subject folder")

    if len(report.errors) != errors_before:
        return None

    pack = {
        "contentFormat": CONTENT_FORMAT,
        "subjectId": entry.id,
        "code": entry.code,
        "title": meta["title"],
        "stream": entry.stream,
        "programme": entry.programme,
        "scheme": entry.scheme,
        "term": entry.term,
        "reviewed": meta["reviewed"],
        "syllabusSource": meta.get("syllabusSource"),
        "practicalCodes": practical_codes,
        "units": units,
        "extras": extras,
        "questions": sorted(questions, key=lambda q: (q["unit"], q["id"])),
        "mcqs": sorted(mcqs, key=lambda m: (m["unit"], m["id"])),
        "mockTests": tests,
        "practicals": practicals,
        "media": [p.name for p in media],
    }
    return SubjectContent(entry=entry, folder=folder, meta=meta, pack=pack, media=media)


_media_refs: dict[Path, set[str]] = {}


def check_images(where: Path, text: str, folder: Path, report: Report) -> None:
    refs = _media_refs.setdefault(folder, set())
    for target in IMAGE_LINK.findall(text):
        if re.match(r"^[a-z]+://", target):
            report.error(where, f"image '{target}' must be a file in this subject's media folder, not a web link")
            continue
        if not target.startswith("media/") or "/" in target[len("media/"):]:
            report.error(where, f"image '{target}' must be written as media/<file name>")
            continue
        name = target[len("media/"):]
        refs.add(name)
        if not (folder / "media" / name).is_file():
            report.error(where, f"image '{target}' not found in {rel(folder / 'media')}")


def referenced_media(folder: Path) -> set[str]:
    return _media_refs.get(folder, set())


# ---------------------------------------------------------------------------
# Exams
# ---------------------------------------------------------------------------

def load_exams(catalog: Catalog, report: Report) -> dict[str, dict]:
    body_ids = {b["id"] for b in catalog.exam_bodies}
    result: dict[str, dict] = {}
    for path in sorted((SOURCE / "exams").glob("*.json")):
        doc = load_json(path, report, "exams.schema.json")
        if not doc:
            continue
        if doc["bodyId"] != path.stem:
            report.error(path, f"bodyId '{doc['bodyId']}' must match the file name '{path.stem}'")
        if doc["bodyId"] not in body_ids:
            report.error(path, f"unknown exam body '{doc['bodyId']}'")
        session_ids: set[str] = set()
        for session in doc["sessions"]:
            if session["id"] in session_ids:
                report.error(path, f"duplicate session id '{session['id']}'")
            session_ids.add(session["id"])
            for i, paper in enumerate(session["papers"]):
                where = f"{session['id']}.papers[{i}]"
                key = (None, paper["programmeId"], paper["schemeId"], paper["termId"])
                matches = [k for k in catalog.by_term if k[1:] == key[1:]]
                if not matches:
                    report.error(path, f"{where}: no catalog term {paper['programmeId']}.{paper['schemeId']}.{paper['termId']}")
                    continue
                if paper["subjectCode"] not in catalog.by_term[matches[0]]:
                    report.error(path, f"{where}: subject {paper['subjectCode']} is not in {'.'.join(matches[0])}")
                if paper["start"] >= paper["end"]:
                    report.error(path, f"{where}: start {paper['start']} is not before end {paper['end']}")
        result[doc["bodyId"]] = doc
    return result


# ---------------------------------------------------------------------------
# Whole-repo validation
# ---------------------------------------------------------------------------

@dataclass
class Validated:
    catalog: Catalog
    subjects: list[SubjectContent]
    exams: dict[str, dict]


def validate_all(report: Report) -> Validated | None:
    _media_refs.clear()
    catalog = load_catalog(report)
    if catalog is None:
        return None
    check_stray_folders(report)
    subjects = []
    for folder in find_subject_folders():
        content = load_subject(folder, catalog, report)
        if content:
            subjects.append(content)
    exams = load_exams(catalog, report)
    return Validated(catalog=catalog, subjects=subjects, exams=exams)


def coverage(validated: Validated) -> dict:
    with_content = {s.entry.id: s.meta["reviewed"] for s in validated.subjects}
    rows = {"theory subjects": 0, "with content": 0, "reviewed": 0}
    missing: list[str] = []
    for entry in validated.catalog.subjects.values():
        if entry.kind not in ("theory", "elective"):
            continue
        rows["theory subjects"] += 1
        if entry.id in with_content:
            rows["with content"] += 1
            if with_content[entry.id]:
                rows["reviewed"] += 1
        else:
            missing.append(entry.id)
    return {"counts": rows, "missing": sorted(missing)}


# ---------------------------------------------------------------------------
# Build output
# ---------------------------------------------------------------------------

def canonical(obj) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def generated_at() -> str:
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        from datetime import datetime, timezone
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cI"], cwd=ROOT, capture_output=True, text=True, check=True)
        if out.stdout.strip():
            return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        pass
    return "unreleased"


def write_file(path: Path, data: bytes) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    digest = sha256(data)
    return {"path": path.relative_to(OUTPUT).as_posix(), "bytes": len(data), "sha256": digest, "version": digest[:16]}


def build_output(validated: Validated) -> dict:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    packs_by_id = {s.entry.id: s for s in validated.subjects}

    def subject_row(stream, prog, scheme, term, subj) -> dict:
        sid = subject_id(stream["id"], prog["id"], scheme["id"], term["id"], subj["code"])
        row = {"id": sid, "code": subj["code"], "title": subj["title"], "kind": subj["kind"]}
        pack_id = sid
        if subj.get("linkedTheory"):
            row["linkedTheory"] = subj["linkedTheory"]
            pack_id = subject_id(stream["id"], prog["id"], scheme["id"], term["id"], subj["linkedTheory"])
        content = packs_by_id.get(pack_id)
        if content:
            row["pack"] = pack_id
            row["reviewed"] = content.meta["reviewed"]
        return row

    streams_out = []
    for stream in validated.catalog.streams:
        progs = []
        for prog in stream["programmes"]:
            schemes = []
            for scheme in prog["schemes"]:
                terms = []
                for term in scheme["terms"]:
                    terms.append({
                        "id": term["id"], "number": term["number"], "name": term["name"],
                        "subjects": [subject_row(stream, prog, scheme, term, s) for s in term["subjects"]],
                    })
                s_out = {k: v for k, v in scheme.items() if k != "terms"}
                s_out["terms"] = terms
                schemes.append(s_out)
            p_out = {k: v for k, v in prog.items() if k != "schemes"}
            p_out["schemes"] = schemes
            progs.append(p_out)
        streams_out.append({"id": stream["id"], "name": stream["name"], "programmes": progs})

    catalog_doc = {"contentFormat": CONTENT_FORMAT, "examBodies": validated.catalog.exam_bodies, "streams": streams_out}
    catalog_entry = write_file(OUTPUT / "catalog.json", canonical(catalog_doc))

    exam_entries = []
    for body_id, doc in sorted(validated.exams.items()):
        entry = write_file(OUTPUT / "exams" / f"{body_id}.json", canonical(doc))
        exam_entries.append({"bodyId": body_id, **entry})

    pack_entries = []
    for content in sorted(validated.subjects, key=lambda s: s.entry.id):
        entry = write_file(OUTPUT / "packs" / f"{content.entry.id}.json", canonical(content.pack))
        media = []
        for path in content.media:
            media.append(write_file(OUTPUT / "media" / content.entry.id / path.name, path.read_bytes()))
        pack_entries.append({"id": content.entry.id, "reviewed": content.meta["reviewed"], **entry, "media": media})

    manifest = {
        "contentFormat": CONTENT_FORMAT,
        "minAppVersion": MIN_APP_VERSION,
        "generatedAt": generated_at(),
        "catalog": catalog_entry,
        "exams": exam_entries,
        "packs": pack_entries,
    }
    (OUTPUT / "manifest.json").write_bytes(canonical(manifest))

    (PUBLIC / ".nojekyll").write_bytes(b"")
    (PUBLIC / "index.html").write_text(
        "<!doctype html><meta charset=utf-8><title>Study content</title>"
        "<p>Study content for the app. Start at <a href=\"v1/manifest.json\">v1/manifest.json</a>.</p>\n",
        encoding="utf-8",
    )
    return manifest
