# 🧑‍💼 Employee Data Generator (India)

A Python script that generates a realistic **synthetic dataset of 1,000 Indian employee records** using the `Faker` library — built for practicing data analysis, Excel dashboards, Power BI, and SQL without touching any real personal data.

## 📋 Description
This project uses `Faker` and `random` to fabricate an HR-style employee dataset — names, contact details, department, salary, banking info, and more — then exports it to an Excel file using `pandas`. It's a safe, ready-to-use dataset for data analytics practice, and a natural first step before building a dashboard on top of it.

## ⚙️ Features
- Generates **1,000 unique employee records**
- Indian-context data (names, cities, phone numbers) via `Faker('en_in')`
- Fields generated:
  - Employee Name, Employee ID, Email, Phone Number
  - City, Region (North / South / East / West)
  - Department (IT, HR, Sales, Finance, Marketing, Management, Supervisor, Operations, Customer Service, Administration)
  - Salary (₹20,000–₹40,000), Age (25–45)
  - Date of Joining (2016–2025)
  - Employment Type (Full-Time / Part-Time)
  - Bank Account Number & IFSC Code
- Exports directly to `.xlsx` using `pandas.DataFrame.to_excel()`

## 🛠️ Tech Stack
- Python 3
- pandas
- Faker
- random, datetime (standard library)

## 🚀 How to Run
```bash
pip install pandas faker openpyxl
python project.py
```
This creates `Employee Sheet_Data.xlsx` in the same folder.

## 📊 Sample Output

| Employee Name | Department       | City       | Region | Salary | Employment Type |
|----------------|------------------|------------|--------|--------|------------------|
| Aachal Vaidya  | Customer Service | New Delhi  | South  | 36411  | Part-Time        |
| Aadi Arya      | Marketing        | Hazaribagh | South  | 21994  | Full-Time        |
| Aadi Dhawan    | Sales            | Mathura    | North  | 25109  | Full-Time        |

## 💡 Use Cases
- Practice data cleaning, EDA, pivot tables, and Excel/Power BI dashboards
- Safe dataset for SQL practice (no real personal data involved)
- Base dataset for a data analytics dashboard project

## 🔮 Future Scope
- Add validation to guarantee unique Employee IDs
- Add more departments/job roles for richer analysis
- Auto-generate summary charts alongside the Excel export

## 👤 Author
**Rehan** — BCA Data Science student, IMT College, Faridabad
GitHub: [rehan2641](https://github.com/rehan2641)

---

### 📝 One-line Summary
Generates a synthetic dataset of 1,000 Indian employee records (name, salary, department, contact & bank details) using Python's Faker library, exported to Excel for data analytics practice.

### 🏷️ Short Description (for GitHub repo field)
Python + Faker + pandas script that generates a synthetic 1,000-row Indian employee dataset and exports it to Excel — built for data analytics practice.
