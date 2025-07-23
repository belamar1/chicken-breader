# 🐔 Chicken-UI PID

A command-line based Chicken Record Management System for breeders, designed as a proof of concept (POC) to demonstrate how a paper-based record-keeping system can be modernized into a digital one. Built using Python and designed for Windows and macOS environments.

---

## 📋 Features

Interactive menu options:

0 - Exit
1 - View All Records
2 - Filter Records by Country
3 - Add New Chicken Record
4 - Update Existing Record
5 - Delete a Record
6 - Show Summary (Total Chickens, Losses)



---

## 🛠️ Tools & Tech Stack

| Tool     | Purpose                              |
|----------|--------------------------------------|
| Python   | Core language for app logic          |
| VS Code  | IDE for development                  |
| Git      | Local version control                |
| GitHub   | Cloud repository and documentation   |
| CSV      | Lightweight persistent data storage  |

---

## 🔄 System Workflow (Input → Process → Output)

        ┌────────────────────────────┐
        │     USER INPUT (CLI)       │
        └────────────┬───────────────┘
                     │
    ┌────────────────▼────────────────┐
    │         PROCESSING LOGIC        │
    │ - Load CSV                      │
    │ - Filter by Country             │
    │ - Add/Edit/Delete Entries       │
    │ - Calculate Total, Loss         │
    └────────────────┬───────────────┘
                     │
           ┌─────────▼─────────┐
           │     OUTPUT TO     │
           │  Terminal Screen  │
           └───────────────────┘


---

## 🌍 Sample Output (Filtered by Country)

Country: Peru
Breed Name Amount Loss
Inca Luna 8 0
Total Chickens: 8 Total Loss: 0


---
🚀 Areas for Improvement (Updated)

## 🚀 Areas for Improvement (Updated)

| Area              | Current Progress                                 | Potential Upgrade                                                                 |
|-------------------|--------------------------------------------------|------------------------------------------------------------------------------------|
| ✅ Input Validation  | Regex-based checks for all fields added         | Expand to include date/time validation and prevent duplicates                     |
| ✅ User Experience   | Clear prompts, confirmations, smart defaults    | Add undo support, keyboard shortcuts, and improved error messages                 |
| Data Persistence  | CSV used for lightweight storage                 | Switch to SQLite or TinyDB for structured, scalable querying                      |
| Visualization     | Text-based terminal output                       | Use `matplotlib` or `seaborn` to graph trends by country, breed, and loss         |
| Reporting         | CLI summary with totals                          | Export to CSV, PDF, or Excel using `pandas`, `reportlab`, or `xlsxwriter`         |
| Scalability       | Works well for small local files                 | Integrate `pandas` for filtering, grouping, and real-time analytics               |
| GUI Option        | CLI-only menu interface                          | Build a GUI using `Tkinter` or a lightweight Flask web dashboard                  |
| Advanced Filters  | Filter by country (regex-based)                  | Add multi-field filters (e.g., country + breed), amount/loss range queries        |
| Data Integrity    | Input normalized and validated                   | Add audit logging and change tracking (e.g., who edited what, when)              |

# ☁️ Serverless ELT Pipeline (AWS Lambda)
To scale the Chicken-UI data processing for larger datasets or future integrations (e.g., dashboards, cloud storage, schools uploading data), we propose an AWS Lambda-powered ELT pipeline.

🛠 Tools & Services
Stage	Service	Role
Extract	Amazon S3 + Lambda	Triggered when a new chicken_data.csv is uploaded to S3
Load	Lambda + RDS/DynamoDB	Loads raw data into a staging table or NoSQL collection
Transform	Lambda or AWS Glue	Cleans, validates (e.g., regex), and normalizes the data
Store	Amazon RDS/Redshift	Stores clean records for reporting and querying
Analytics	QuickSight or Athena	Used to visualize trends like loss by country or breed

# Pipeline flow:

User uploads CSV to S3
        ↓
Lambda Function (Extract + Load)
        ↓
RDS / DynamoDB Staging Table
        ↓
Lambda Function (Transform + Clean)
        ↓
Final Database / Data Warehouse
        ↓
Optional: Dashboards (QuickSight) or API layer

🔍 Example Use Case

field teams upload chicken records as CSV files.

AWS Lambda automatically processes the files.

Cleaned data is sent to a cloud database (PostgreSQL or DynamoDB).

Admins or educators view data via dashboards or reports.

✅ Why Lambda?
No server maintenance

Auto-scales with file size

Secure via IAM & S3 triggers

Perfect for educational + community-led deployments