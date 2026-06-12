# 🚢 Titanic Data Pipeline and Power BI Dashboard

## 📌 Project Overview

This project demonstrates an end-to-end data analytics workflow using the Titanic dataset. The data was cleaned and processed using Python and SQLite, and an interactive Power BI dashboard was created to visualize passenger demographics and survival trends.

---

## 🛠 Technologies Used

- Python
- Pandas
- SQLite
- Power BI Desktop
- Power Query
- DAX

---

## 🔄 ETL Process

### 1. Data Extraction
- Loaded Titanic dataset using Pandas.

### 2. Data Cleaning
- Handled missing values.
- Removed unnecessary data inconsistencies.
- Created new feature: **FamilySize**.

### 3. Data Storage
- Stored processed data into SQLite database.

### 4. Data Analysis
- Performed SQL queries for analysis.
- Generated insights from passenger data.

---

## 📊 Power BI Dashboard

An interactive dashboard was developed in Power BI to analyze passenger information and survival patterns.

### Dashboard Features

- Total Passengers KPI
- Survival Rate Analysis
- Passenger Class Distribution
- Gender-wise Survival Comparison
- Age Distribution Analysis
- Interactive Filters and Slicers

---

## 📈 Key Insights

- Female passengers had a higher survival rate than male passengers.
- First-class passengers had better survival chances.
- Survival rates varied across different age groups.
- Passenger class significantly influenced survival outcomes.

---

## 📁 Project Files

| File | Description |
|--------|-------------|
| pipeline.py | Main ETL script |
| titanic.csv | Titanic dataset |
| Titanic.pbix | Power BI dashboard |
| README.md | Project documentation |

---

## 🚀 How to Run

### Python Pipeline

```bash
pip install pandas
python pipeline.py
```

### Power BI Dashboard

1. Open `Titanic.pbix` in Power BI Desktop.
2. Refresh the dataset if required.
3. Explore the interactive dashboard.

---

## 📷 Dashboard Preview

Add your dashboard screenshot here:

```md
![Titanic Dashboard](dashboard.png)
```

---

## 🎯 Outcome

Successfully built a beginner-friendly end-to-end Data Analytics project covering:

- Data Cleaning
- ETL Pipeline
- SQL Analysis
- Data Visualization
- Business Intelligence Reporting

This project demonstrates practical skills in Python, SQL, and Power BI for data analytics and business intelligence applications.
