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

## 🚀 Areas for Improvement

| Area              | Potential Upgrade                                  |
|-------------------|----------------------------------------------------|
| Data Persistence  | Switch from CSV to SQLite for better querying      |
| Input Validation  | Add checks for numbers and required fields         |
| Visualization     | Use `matplotlib` to graph amounts/loss by country  |
| User Experience   | Add confirmation prompts and undo options          |
| Reporting         | Export filtered views or summaries to PDF/CSV      |
| Scalability       | Use `pandas` for complex filtering and grouping    |
| GUI Option        | Add Tkinter or Flask Web Interface for friendliness|

---