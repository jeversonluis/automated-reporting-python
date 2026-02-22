# 🚀 Automated Crypto Market Reporting (Python + Google Sheets + Looker Studio)

This project demonstrates an end-to-end automated data reporting pipeline that collects cryptocurrency market data from the CoinGecko API, stores historical snapshots in Google Sheets, and visualizes insights through an interactive Looker Studio dashboard.

The solution was built as a data analytics portfolio project, focusing on automation, data modeling, and business-ready visualization.

---

## 📊 Project Overview

The pipeline retrieves daily market data for selected cryptocurrencies, including:

- Price (USD)
- Market Capitalization (USD)
- 24h Price Change (%)
- Snapshot timestamp

The data is stored in Google Sheets using two logical layers:

- Summary: latest market snapshot (overwrite)
- History: historical records (append-only, one record per asset per day)

Looker Studio connects directly to Google Sheets to provide real-time dashboards and time-series analysis.

---

## 🔧 Tech Stack

- Python
- CoinGecko Public API
- Pandas
- Google Sheets API
- Looker Studio
- GitHub

---

## 🔁 Automation Logic

- Fetches market data from the CoinGecko API
- Filters selected cryptocurrencies
- Cleans and standardizes numeric fields
- Appends historical data (one snapshot per asset per day)
- Overwrites summary snapshot
- Designed to run once per day

The pipeline is structured to support scheduling via GitHub Actions or local schedulers.

---

## 📁 Project Structure

automated-reporting-python/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
└── .github/
└── workflows/
└── daily_run.yml

---

## 📈 Dashboard

The Looker Studio dashboard includes:

- Total Market Capitalization KPI
- Asset price comparison
- Market capitalization distribution
- Daily price trend over time
- Daily market capitalization trend over time
- Interactive asset filters

Dashboard link:  
https://lookerstudio.google.com/reporting/862122b2-3bdb-496f-b75d-1e6b4e2a1bc0

---

## 🔐 Security Notes

- Google Service Account credentials are not versioned
- Sensitive files are excluded via .gitignore
- This repository contains only public-safe code

---

## 🎯 Purpose

This project showcases skills in:

- API data ingestion
- Data automation
- Historical data modeling
- Business-focused dashboards
- BI tool integration

It is intended for portfolio and demonstration purposes.

---

## 👤 Author

Jeverson Luis S. 
Data Analyst | BI | Automation  
GitHub: https://github.com/jeversonluis