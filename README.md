# 🚀 Automated Crypto Market Reporting

An end-to-end **automated data pipeline** for collecting, storing, and visualizing cryptocurrency market data using **Python, Google Sheets, and Looker Studio**.

This project demonstrates how to build a lightweight yet production-ready reporting solution that connects data extraction, data storage, and business intelligence visualization.

---

## 🧠 Project Overview

The goal of this project is to **automate the monitoring of cryptocurrency market data** and make it easily accessible through an interactive dashboard.

The pipeline:
- Collects market data from a public API;
- Stores historical records in Google Sheets;
- Feeds a dynamic dashboard built in Looker Studio.

This solution can be adapted to many other business use cases that require **scheduled data extraction and reporting**.

---

## 📊 Tech Stack

| Tool | Purpose |
|------|--------|
| Python | Data extraction and processing |
| CoinGecko API | Cryptocurrency market data source |
| Google Sheets API | Data storage and historical tracking |
| Looker Studio | Interactive dashboards and visual analytics |
| GitHub Actions | Automated scheduled execution |

---

## 🔄 Data Flow Architecture

1. **Data Extraction (Python)**
   - Connects to the CoinGecko API
   - Retrieves current market data (prices, market cap, volume, etc.)
   - Applies basic transformations and formatting

2. **Data Storage (Google Sheets)**
   - Appends new records daily
   - Maintains historical data over time
   - Acts as a centralized data source

3. **Data Visualization (Looker Studio)**
   - Connects directly to Google Sheets
   - Displays interactive charts and KPIs
   - Enables trend analysis and asset comparison

---

## 📈 Live Dashboard

👉 Access the interactive dashboard here:  
**Looker Studio – Crypto Market Report**  
https://lookerstudio.google.com/reporting/862122b2-3bdb-496f-b75d-1e6b4e2a1bc0

The dashboard allows users to:
- Track price evolution over time
- Compare multiple cryptocurrencies
- Analyze market capitalization trends
- Explore historical performance interactively

---

## ⚙️ Automation

The project is designed to run automatically using **GitHub Actions**, enabling:
- Scheduled execution (e.g. daily updates)
- Hands-free data refresh
- Reliable and repeatable reporting

This approach simulates a real-world automated reporting pipeline used in data teams.

---

## 📁 Repository Structure

automated-reporting-python/
├── main.py # Main data extraction and loading script
├── config.py # Configuration and environment variables
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .github/
└── workflows/
└── daily_run.yml # Scheduled automation workflow


> Sensitive credentials are excluded from version control and handled securely.

---

## 💡 Why This Project Matters

This project demonstrates practical skills in:
- API integration
- Data automation and scheduling
- Simple ETL pipeline design
- Business Intelligence and dashboarding
- Cloud-based tools commonly used by data teams

It reflects real-world scenarios where analysts need to **bridge data engineering and analytics**.

---

## 🎯 Use Cases

- Market monitoring dashboards  
- Automated executive reports  
- Financial or investment tracking  
- Proof of concept for data automation pipelines  

---

## 📌 Possible Extensions

Although no changes are required, this project could easily be extended to:
- Add more assets or APIs
- Store data in a database instead of Sheets
- Apply advanced transformations
- Create alerts based on market conditions

---

## 👤 Author

**Jeverson Luis S.**  
Python Automation Specialist | Google Sheets & Workspace Automation | API Integrations | Data Automation Freelancer

Feel free to explore the repository and dashboard to understand the full workflow.
