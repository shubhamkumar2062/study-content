# HTML web page showing personal information

**Aim:** To create a web page using HTML that displays personal information.

## Principle

**HTML (HyperText Markup Language)** describes the structure of a web page with **tags** such as `<h1>` for a heading, `<p>` for a paragraph, `<table>` for a table and `<img>` for an image. The file is written in a plain text editor, saved with the extension `.html`, and opened in a web browser, which reads the tags and displays the page. Simple styling can be added with CSS.

## Requirements

Computer with a text editor (Notepad, Notepad++ or VS Code) and a web browser (Chrome, Edge, Firefox); a photograph file (e.g. `photo.jpg`) in the same folder.

## Procedure

1. Create a folder `MyPage` and copy your photo into it as `photo.jpg`.
2. Open Notepad and type the following code (replace the details with your own):

```text
<!DOCTYPE html>
<html>
<head>
  <title>My Profile</title>
  <style>
    body  { font-family: Arial; background-color: #f4f8fb; margin: 30px; }
    h1    { color: #1a4d80; }
    table { border-collapse: collapse; }
    td, th { border: 1px solid #999; padding: 6px 12px; }
  </style>
</head>
<body>
  <h1>Personal Information</h1>
  <img src="photo.jpg" alt="My photograph" width="120">
  <table>
    <tr><th>Name</th><td>Your name</td></tr>
    <tr><th>Course</th><td>B.Pharm, Semester II</td></tr>
    <tr><th>College</th><td>Your college</td></tr>
    <tr><th>E-mail</th><td>yourname@example.com</td></tr>
  </table>
  <h2>Hobbies</h2>
  <ul>
    <li>Reading</li>
    <li>Cricket</li>
  </ul>
  <h2>Education</h2>
  <ol>
    <li>Senior Secondary (Class XII)</li>
    <li>Secondary (Class X)</li>
  </ol>
  <p>Visit <a href="https://www.pci.nic.in">Pharmacy Council of India</a></p>
</body>
</html>
```

3. Save with **File → Save As**, file name `index.html`, "Save as type: All files", encoding UTF-8, in the `MyPage` folder.
4. Double-click `index.html` (or open it in the browser) and check the page.
5. Make changes in Notepad, save, and press **Refresh (F5)** in the browser to see them.
6. Take a printout of the code and of the page (Ctrl + P in the browser).

## Observations

| Tag used | Purpose | Seen on the page as |
| --- | --- | --- |
| `<title>` | Page title | Text on the browser tab |
| `<h1>`, `<h2>` | Headings | Large bold headings |
| `<img>` | Image | Photograph |
| `<table>`, `<tr>`, `<th>`, `<td>` | Table | Details in rows |
| `<ul>`, `<ol>`, `<li>` | Lists | Bullet and numbered lists |
| `<a href>` | Hyperlink | Clickable link |
| `<style>` | Internal CSS | Colours, font, borders |

## Result

A web page showing personal information was created in HTML and displayed in the browser.

## Precautions

1. Save the file with the `.html` extension, not `.txt`.
2. Close every tag and nest tags correctly.
3. Keep the image in the same folder or give the correct path; write the file name exactly (case matters on servers).
4. Do not put sensitive personal data (phone, address) on a public page.

## Viva questions

1. **What does HTML stand for?** HyperText Markup Language.
2. **What is the difference between `<head>` and `<body>`?** `<head>` holds information about the page (title, styles); `<body>` holds what is shown.
3. **What is an attribute?** Extra information inside a tag, e.g. `src` and `alt` in `<img>`.
4. **What is the use of the `alt` attribute?** It gives text shown if the image cannot load and is read by screen readers.
5. **What is the difference between `<ul>` and `<ol>`?** `<ul>` gives bullets; `<ol>` gives numbers.
6. **What is CSS?** Cascading Style Sheets, used to set colours, fonts and layout.
