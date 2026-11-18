# Study content

Notes, rated question banks, MCQs, mock tests, practical guides and exam date sheets for the study app. Covers Pharmacy, Nursing, Education and degree courses.

This repo is the app's only data source. People edit `source/`. A script checks it and builds `public/v1/`, which GitHub Pages hosts and the app downloads.

> The app and this content are independent. They are not made by, or affiliated with, any college, university or board. Always confirm exam dates on the official site linked in each date sheet.

## Layout

```text
source/
  exam-bodies.json                 HPTU, HPTSB, AMRU, HPU: names and official sites
  catalog/<stream>.json            stream > programme > scheme > term > subjects
  exams/<body>.json                date sheets, with the official PDF link
  subjects/<stream>/<programme>/<scheme>/<term>/<code>/
    subject.json                   code, title, units, which files hold the notes, reviewed flag
    notes/*.md                     one Markdown file per unit, plus extras (revision sheet, …)
    questions.json                 short / long / very-short questions, marks, probability, answer
    mcqs.json                      options, correct option (counted from 0), explanation
    mocktests.json                 paper pattern: sections, marks, how many to attempt, time
    practicals/*.md                experiments with viva questions
    media/                         images used by the notes (svg, webp, png)
schema/                            the rules every file must follow
scripts/validate.py                check everything
scripts/build.py                   check, then write public/v1/
```

The subject folder name is the subject code in lower case, with anything that is not a letter or digit turned into `-`. For example, `BP301T` becomes `bp301t`.

## Ids never change

A subject's id is `stream.programme.scheme.term.code`, for example `pharmacy.bpharm.pci.sem3.bp301t`. Phones store bookmarks and progress against these ids, and question and MCQ ids inside a subject. **Never rename or reuse an id once it has been published.** To retire something, delete it; don't give its id to something else.

## Editing

1. Change or add files under `source/`. Edit them in the GitHub website or on your computer.
2. Run the checks (Python 3.9 or newer, nothing to install):

   ```sh
   python3 scripts/validate.py
   python3 scripts/validate.py --list-missing   # which subjects still have no content
   ```

3. Commit to `main`. GitHub Actions runs the same checks, builds `public/`, and publishes it to GitHub Pages in about a minute. If a check fails, nothing is published, and the old content stays live.

Changes from other people should come in as pull requests. The checks run on every pull request, so problems show before anything is merged.

### Writing notes

- Plain Markdown. Headings, lists, tables, `**bold**`, and fenced code blocks for text diagrams all work.
- Images: put the file in the subject's `media/` folder and link it as `![Benzene ring](media/benzene.svg)`. Web links to images are rejected, so the app can show every image offline.
- A note can start with front-matter (`---` lines with `key: value`). The app ignores it; use it for your own remarks.

### Questions and probability

`probability` is `high`, `medium` or `low`. It is an estimate of how likely the question is in the university exam, based on past papers and syllabus weight. It is not a promise, and the app says so.

### Reviewed

A subject's `reviewed` flag stays `false` until a teacher of that subject has checked it. Release builds of the app show only reviewed subjects.

## What the build writes

```text
public/v1/manifest.json            version, size and sha256 of everything below
public/v1/catalog.json             the full stream > … > subject tree, with exam bodies
public/v1/exams/<body>.json        date sheets
public/v1/packs/<subjectId>.json   everything for one subject in one file
public/v1/media/<subjectId>/<file> images
```

JSON is written with sorted keys and no extra spaces, so unchanged content always gives the same bytes and the same hashes. A file's `version` is the first 16 characters of its sha256, so it changes exactly when the content changes.

## How the app uses it

Base URL: `https://<github-user>.github.io/<repo>/v1/` (or a custom domain pointed at Pages).

Backup URL, used by the app only when the main one fails: `https://cdn.jsdelivr.net/gh/<github-user>/<repo>@published/v1/`. The publish workflow copies the built files to the `published` branch on every change and clears jsDelivr's cache for the changed files.

| Request | When |
| --- | --- |
| `manifest.json` | at launch and about once a day |
| `catalog.json` | when `manifest.catalog.version` differs from the app's copy |
| `exams/<body>.json` | when that entry's `version` differs |
| `packs/<subjectId>.json` | when that pack's `version` differs |
| `media/<subjectId>/<file>` | the first time the subject is opened, or on "download for offline" |

1. The app ships with a copy of `public/v1/` without the images, so it works offline from the first launch.
2. On sync, it downloads only the files whose `version` changed, checks each one's `sha256`, and swaps them in together. If anything fails, it keeps the old copy.
3. `minAppVersion` in the manifest tells apps that are too old to read the content to update.
4. A change older apps can't read gets published under `/v2/` while `/v1/` keeps being published (`CONTENT_FORMAT` in `scripts/content_lib.py`).

## Publishing setup (once)

1. Create an empty public GitHub repo (for example `study-content`) and push this one to it.
2. In the repo: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Push to `main`. The site appears at `https://<github-user>.github.io/<repo>/`.
4. Optional: add a custom domain under **Settings → Pages**. You can then move hosting later (for example to Cloudflare Pages) without changing the app.
