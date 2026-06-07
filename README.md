# 📊 Project 6: End-to-End Analytics Platform (Batch + Streaming + ML + Warehouse)

## 📌 Overview

This project implements a production-style end-to-end data platform that integrates modern data engineering components into a unified system.

It combines:
- Batch ETL pipelines
- Data warehouse modeling (dbt)
- Workflow orchestration (Apache Airflow)
- Machine learning pipeline integration

The system simulates a real-world analytics platform used for business intelligence and predictive analytics.

---

## 🏗️ System Architecture

```text
Raw Data (CSV Sources)
        ↓
Python ETL Layer (Extraction + Cleaning)
        ↓
Staging Tables (PostgreSQL)
        ↓
Apache Airflow (Orchestration Layer)
        ↓
dbt Transformation Layer
        ↓
Data Warehouse (Star Schema)
        ↓
Feature Engineering Layer
        ↓
Machine Learning Model Training
        ↓
Prediction / Analytics Output
```

---

## ⚙️ Key Components

### 📥 1. Data Ingestion Layer

- Loads raw datasets from data/raw/
- Prepares structured inputs for processing

### 🔄 2. ETL Processing Layer

- Python-based transformation logic
- Handles missing values and schema normalization
- Prepares data for warehouse ingestion

### 🏛️ 3. Data Warehouse Layer (dbt)

- Implements star schema architecture
- Fact tables: orders
- Dimension tables: customers, products, payments
- Ensures analytics-ready structure

###🤖 4. Machine Learning Layer

- Feature engineering from warehouse tables
- Model training using structured datasets
- Saves trained model (model.pkl)
- Enables prediction pipeline
  
### 🧠 5. Orchestration Layer (Airflow)
- Automates full pipeline execution
- Manages task dependencies
- Ensures reproducible workflows

---

## 🧰 Tech Stack

- Python (ETL + ML)
- SQL (Data modeling)
- Apache Airflow (Orchestration)
- dbt (Data transformations)
- PostgreSQL (Warehouse)
- Docker (Containerization)
- Pandas / Scikit-learn (ML)

---

## 🔄 Pipeline Flow

Extract → Transform → Load → Staging → dbt Models → Warehouse → Features → ML Model → Output

---

## 📁 Project Structure

dags/              → Airflow DAGs
scripts/           → ETL + ML pipelines
data/raw/          → Raw datasets
dbt/               → Data warehouse models
models/            → ML models
docker-compose.yml → Infrastructure setup
requirements.txt   → Dependencies

## 🚀 Execution Modes

### ▶ Manual Execution
```bash
python scripts/load_raw_data.py
```
### ▶ Airflow Execution

Triggered via:
```bash
dags/warehouse_pipeline.py
```
---

## 🧠 Key Engineering Highlights

- Production-style data platform design
- Batch + warehouse + ML integration
- dbt-based analytics engineering
- Airflow orchestration
- Modular and scalable architecture

---

## 🚀 Outcome

This project demonstrates a complete modern data platform that integrates:

- Data engineering pipelines
- Data warehouse modeling
- Workflow orchestration
- Machine learning workflows
  
It reflects how real-world analytics platforms are built in production systems.
