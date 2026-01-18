# 📈 IDR Exchange Rate Tracker (Automated ETL)

This repository hosts an automated ETL (Extract, Transform, Load) pipeline that tracks the daily exchange rate between the **US Dollar (USD)** and **Indonesian Rupiah (IDR)**.

The project demonstrates a serverless data pipeline architecture using **GitHub Actions** to automate data fetching and version control.

## 🚀 How It Works

This project runs completely on GitHub infrastructure without needing an external server (VPS).

1.  **Extract:** A Python script fetches real-time financial data from the public [Frankfurter API](https://www.frankfurter.app/).
2.  **Transform:** The data is processed and formatted into a structured CSV format with timestamps.
3.  **Load:** The new data point is appended to the historical dataset (`data/exchange_rates.csv`).
4.  **Automation:** The process is triggered automatically every day at 00:00 UTC via **GitHub Actions**.

## 🛠 Tech Stack

* **Python:** For data extraction and manipulation (Pandas, Requests).
* **GitHub Actions:** For CI/CD automation and scheduling (Cron).
* **Git:** For version control and data history management.
* **CSV:** For flat-file storage (Data Lake simulation).

## 📂 Project Structure

```bash
├── .github/workflows
│   └── daily_run.yml    # Configuration for the automation (Cron Job)
├── data
│   └── exchange_rates.csv # The dataset (Historical Data)
├── main.py              # The Python ETL script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation