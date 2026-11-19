# Patient information database in MS Access

**Aim:** To create a database in MS Access to store patient information with the required fields.

## Principle

**MS Access** is a relational database management system. A **database** file holds **tables**; each table stores data about one subject in **records** (rows) and **fields** (columns). Each field has a **data type** (Short Text, Number, Date/Time, Yes/No, etc.) and properties (field size, format, validation rule, required). A **primary key** uniquely identifies each record. Designing the table correctly in **Design View** prevents wrong or duplicate entries.

## Requirements

Computer with MS Access (part of Microsoft Office).

## Procedure

1. Open MS Access → **Blank database** → File Name `Hospital.accdb` → choose folder → **Create**.
2. A new table opens. Go to **Home → View → Design View** and save the table as `Patient`.
3. Enter the fields:

| Field name | Data type | Properties |
| --- | --- | --- |
| PatientID | AutoNumber | Primary key |
| PatientName | Short Text | Field size 50; Required = Yes |
| Gender | Short Text | Lookup values: Male; Female; Other |
| DateOfBirth | Date/Time | Format: Short Date |
| Phone | Short Text | Field size 10; Input mask for 10 digits |
| Address | Long Text | |
| BloodGroup | Short Text | Lookup values: A+, A−, B+, B−, AB+, AB−, O+, O− |
| Diagnosis | Short Text | |
| AdmissionDate | Date/Time | Default value = Date() |
| Allergies | Long Text | |
| Weight_kg | Number | Validation rule: >0 And <300 |

4. Click on PatientID → **Design → Primary Key** (key symbol appears).
5. Set the properties shown in the lower pane (Field Size, Required, Validation Rule with Validation Text such as "Enter weight between 1 and 299 kg").
6. Save (Ctrl + S) and switch to **Datasheet View**.
7. Enter at least 10 patient records. Press Tab to move between fields; the record is saved automatically when you move to the next row.
8. Practise: sort by name (**Home → Ascending**), find a patient (**Home → Find**), filter by diagnosis (**Home → Filter**).
9. Close the table; the data stay stored in `Hospital.accdb`.

## Observations

| Item | Value |
| --- | --- |
| Database file | Hospital.accdb |
| Table | Patient |
| Number of fields | 11 |
| Primary key | PatientID (AutoNumber) |
| Records entered | ___ |
| Validation tested | Weight 0 was rejected with the message "___" |

## Result

A patient information database `Hospital.accdb` with a `Patient` table of ___ fields was created and ___ records were entered.

## Precautions

1. Choose a meaningful, unique primary key; do not use the patient name as key.
2. Choose correct data types (Date/Time for dates, Number for weight) so sorting and calculations work.
3. Use validation rules and required fields to stop wrong entries.
4. Keep patient data confidential; protect the file with a password if needed (File → Info → Encrypt with Password).
5. Take a backup copy of the database.

## Viva questions

1. **What is a field and a record?** A field is one column (kind of data); a record is one row (all data of one patient).
2. **What is a primary key?** A field whose value is unique and never blank for each record.
3. **Why use AutoNumber?** Access gives each new record a unique number automatically.
4. **Difference between Datasheet and Design View?** Datasheet View is for entering data; Design View is for defining fields and properties.
5. **What is a validation rule?** A condition that data must satisfy, e.g. weight >0 And <300.
6. **File extension of an Access database?** .accdb (older .mdb).
