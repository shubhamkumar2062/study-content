# Form to view, add, delete and modify patient records

**Aim:** To design a form in MS Access to view, add, delete and modify patient records in the database.

## Principle

A **form** is a database object that shows the fields of a table or query on a screen, usually one record at a time, in a friendly layout. It makes data entry easier and safer than typing directly into a table. **Navigation buttons** move between records, and **command buttons** (made with the Command Button Wizard) can add, delete, save or find records.

## Requirements

Computer with MS Access; the database `Hospital.accdb` with the `Patient` table from the previous practical.

## Procedure

1. Open `Hospital.accdb`. In the Navigation Pane select the `Patient` table.
2. **Create → Form Wizard** → Table: Patient → move all fields to "Selected Fields" (>>) → Next.
3. Choose the layout **Columnar** → Next → title `Patient Form` → **Modify the form's design** → Finish.
4. In **Design View**, arrange and resize the labels and text boxes; add a heading label in the Form Header ("Patient Record"); set font and colours from the Property Sheet.
5. **Add command buttons**: with **Use Control Wizards** on, choose **Design → Button** and draw it on the form. In the wizard select:
   - Record Navigation → Go to First / Previous / Next / Last Record;
   - Record Operations → **Add New Record**;
   - Record Operations → **Save Record**;
   - Record Operations → **Delete Record**;
   - Record Navigation → **Find Record**;
   - Form Operations → **Close Form**.
   Give each button a picture or text and a meaningful name (cmdAdd, cmdDelete…).
6. Save the form and switch to **Form View**.
7. **View**: use the navigation buttons to move through records.
8. **Add**: click *Add New Record*, enter the details, click *Save Record*.
9. **Modify**: go to a record, change a field (e.g. diagnosis), click *Save Record*.
10. **Delete**: go to a record, click *Delete Record*, confirm "Yes".
11. Open the `Patient` table and check that the additions, changes and deletion appear.

## Observations

| Operation | Record (PatientID) | Result seen in table |
| --- | --- | --- |
| View | 1 → 10 | All records displayed one by one |
| Add | ___ | New record present |
| Modify | ___ | Diagnosis changed to ___ |
| Delete | ___ | Record removed |

## Result

A patient form with navigation and command buttons was designed, and records were viewed, added, modified and deleted through it.

## Precautions

1. Base the form on the correct table or query.
2. Confirm before deleting; deleted records cannot be undone.
3. Do not let users edit the AutoNumber primary key (set Locked = Yes for that text box).
4. Save the form design before switching views.

## Viva questions

1. **What is a form in Access?** A screen object for entering, viewing and editing data, usually one record at a time.
2. **Name the form layouts.** Columnar, Tabular, Datasheet, Justified.
3. **What are navigation buttons?** Controls that move to the first, previous, next, last or new record.
4. **How is a command button created?** Design → Button with Control Wizards on, then choose the action in the wizard.
5. **Form vs report?** A form is for entering and editing on screen; a report is for formatted, printed output.
6. **What is the Property Sheet?** A pane listing properties (format, data, events) of the selected control.
