# 🚖 Goodcabs Data Engineering Project

## 📌 Overview

This project focuses on building a data pipeline for **Goodcabs transportation data** using Databricks and Spark Declarative Pipelines (SDP).

It follows the **Medallion Architecture (Bronze, Silver, and Gold)** to ingest raw data, clean and transform it, and prepare it for analytics.

## 🛠️ Tech Stack

- Databricks
- Apache Spark & PySpark
- Spark Declarative Pipelines (SDP)
- Delta Lake
- SQL
- Auto Loader

## 🏗️ Architecture

**Bronze → Silver → Gold**

- **Bronze Layer:** Ingests raw trip and city data from CSV files using Auto Loader.
- **Silver Layer:** Cleans and transforms data, applies data quality checks, and handles CDC using SCD Type 1.
- **Gold Layer:** Creates analytics-ready views by combining trip, city, and calendar data.

## 📂 Project Structure

```text
├── data/
│   ├── city/
│   └── trips/
│       ├── Full Load/
│       └── Incremental Load/
│
└── codes/
    ├── bronze/
    ├── silver/
    ├── gold/
    └── project_setup.ipynb
```

## 📊 Dataset

The project uses two primary datasets:

- **Trips:** Trip ID, date, city, passenger category, distance travelled, fare amount, and driver/passenger ratings.
- **City:** City ID and city name.

A calendar dimension is also used to enrich trip data with date-related attributes.

## ⚙️ Key Features

- Incremental data ingestion using Auto Loader.
- Data cleaning and transformation using PySpark.
- Data quality expectations and validation.
- Change Data Capture (CDC) and SCD Type 1.
- Delta Lake optimization and Change Data Feed.
- Gold-layer analytical views using SQL.

## 📈 Analytics

The Gold layer supports analysis of:

- Trip volume by city.
- Fare revenue by city.
- Monthly trip trends.
- Average trip distance.
- Driver and passenger ratings.
- Weekday, weekend, and holiday trends.

## 🎯 Learning Outcomes

- Understanding Medallion Architecture.
- Building pipelines with Spark Declarative Pipelines.
- Working with PySpark, SQL, and Delta Lake.
- Implementing incremental loads and CDC.
- Adding data quality checks.
- Creating analytics-ready datasets.

## 🚀 Future Improvements

- Build interactive dashboards.
- Implement pipeline monitoring and automated testing.
- Develop additional business analytics.

## 📚 Resources

- [Databricks Documentation](https://docs.databricks.com/)
- [Spark Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/)
- [Delta Lake Documentation](https://docs.delta.io/)

---

*Hands-on practice project exploring data engineering concepts using Databricks, PySpark, SDP, and SQL.*
