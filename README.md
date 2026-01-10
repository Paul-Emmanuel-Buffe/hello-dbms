# Hello DBMS+

## Executive Summary

**Hello DBMS+** is a collective academic project exploring relational database management systems through hands-on SQL analytics and a data-driven web application.  
The project combines **PostgreSQL**, **SQL analytical queries**, **exploratory data analysis**, and a **pedagogical Flask application** to compute and visualize carbon footprint indicators based on electricity production data.

It is designed as a practical demonstration of how structured data, relational modeling, and SQL can be leveraged to support analytical use cases and data-driven applications.

---

## Project Context

With global data volumes growing exponentially, the ability to design, query, and analyze structured data remains a core skill for Data Analysts, BI profiles, and Data Engineers.  
This project was developed as part of the **DBMS+ curriculum** and focuses on applying database concepts to a concrete environmental use case: **carbon footprint estimation from electricity production mixes**.

---

## Learning Objectives

This project addresses the following competencies:

- Relational database concepts and DBMS fundamentals  
- PostgreSQL usage and SQL analytical querying  
- Data exploration and preparation  
- Use of SQL as an analytical computation engine  
- Data-driven application development  
- Visualization of analytical results  
- Clear and documented data assumptions  

---

## Project Architecture

```text
.
├── big_job_carbonfootprint_project/
│   ├── app.py                 # Flask application
│   ├── static/                # CSS, JS, assets
│   ├── templates/             # HTML templates
│   └── __pycache__/
│
├── data/
│   └── raw/                   # Raw CSV datasets (evolving)
│
├── notebooks/                 # EDA, SQL exercises, data preparation
│
└── README.md
````

### Data Flow

```text
CSV datasets
   ↓
PostgreSQL (local)
   ↓
SQL queries (EDA, analytics, calculations)
   ↓
Notebooks & Flask application
   ↓
Interactive visualizations and indicators
```

---

## Data Sources

The project relies on CSV datasets describing:

* Electricity production by energy source
* Country-level contextual information

The `data/raw` directory is designed to evolve and may contain additional datasets as the project grows.

---

## Database & SQL Usage

* **DBMS**: PostgreSQL (local instance)
* **SQL role**:

  * Exploratory analysis
  * Data preparation
  * Analytical computations

### SQL Concepts Applied

* Common Table Expressions (CTE)
* Aggregations and percentage calculations
* Analytical transformations
* Multi-step computations directly in SQL

SQL is intentionally used as a **core analytical layer**, not only as a storage solution.

---

## Notebooks

The `notebooks` directory contains Jupyter notebooks used for:

* Exploratory Data Analysis (EDA)
* Data preparation
* SQL exercises connected to PostgreSQL
* Pedagogical experimentation and validation of assumptions

This work is **collective** and designed to be incremental and extensible.

---

## Flask Application

The project includes a **pedagogical Flask web application** located in:

```text
big_job_carbonfootprint_project/app.py
```

### Application Objectives

* Retrieve analytical results from PostgreSQL
* Perform SQL-driven carbon footprint calculations
* Visualize electricity mix and CO₂ emissions
* Make environmental indicators understandable and comparable

### Key Features

* Country-level electricity mix analysis
* CO₂ emissions estimation using IPCC emission factors
* Tree planting equivalence calculation
* Interactive visualizations (Plotly):

  * Pie charts
  * Bar charts
  * Stacked bar charts

### Available Routes

* `/` – Global overview
* `/observations` – Energy mix distribution
* `/analyse` – Carbon footprint analysis by country
* `/methodologie` – Methodology and assumptions

The application is **voluntarily non-production-oriented** and focuses on clarity, pedagogy, and analytical reasoning.

---

## Getting Started

### Prerequisites

* Python 3.x
* PostgreSQL (local instance)
* Jupyter Notebook

### PostgreSQL Connection (Notebooks)

PostgreSQL is accessed from notebooks using `ipython-sql`.

Connection credentials are **not stored in the repository**.

---

### Running the Flask Application

```bash
python big_job_carbonfootprint_project/app.py
```

---

## Limitations & Perspectives

* Dataset scope is limited and primarily pedagogical
* No production-level security or performance optimization
* The project is designed as a learning and demonstration tool

Future improvements may include:

* Dataset enrichment
* Advanced relational modeling
* Extended analytical indicators
* Introduction of data governance and regulatory considerations

---

## Authors

Academic group project conducted as part of the **DBMS+ curriculum**.

* Aida Niang
* Khady Ndiaye
* Paul-Emmanuel Buffe

```