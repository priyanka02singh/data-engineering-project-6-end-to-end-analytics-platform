# 📊 Project 6: End-to-End Analytics Platform (Batch + Streaming + ML + Warehouse)

## 📌 Overview

This project implements a production-style end-to-end data platform that integrates:

- Batch data processing pipelines (ETL)
- Data warehouse modeling (star schema using dbt)
- Workflow orchestration using Apache Airflow
- Machine learning feature pipeline
- Structured analytics layer for reporting

It simulates a modern data platform architecture used in real companies for analytics, reporting, and predictive modeling.

---

## 🏗️ System Architecture
```text
Raw Data (CSV / Simulated Sources)
        ↓
ETL Layer (Python Scripts)
        ↓
Staging Tables (PostgreSQL)
        ↓
Airflow Orchestration (DAGs)
        ↓
dbt Transformation Layer
        ↓
Data Warehouse (Fact + Dimension Tables)
        ↓
Feature Engineering Layer
        ↓
Machine Learning Pipeline
        ↓
Analytics / Prediction Output
```

---

## ⚙️ Key Components

### 📥 1. Data Ingestion Layer

- Loads raw datasets from data/raw/
- Prepares structured inputs for processing

### 🔄 2. ETL Processing Layer

- Python-based transformation logic
- Cleans missing values and standardizes schema
- Prepares staging-ready datasets

### 🏛️ 3. Data Warehouse Layer (dbt)

- Implements star schema design
- Fact tables: orders
- Dimension tables: customers, products, payments
- Ensures analytics-ready structure

###🤖 4. Machine Learning Layer

- Feature engineering from warehouse tables
- Model training pipeline
- Stores trained model (model.pkl)
- Supports prediction workflows
  
### 🧠 5. Orchestration Layer (Airflow)
- Automates full pipeline execution
- Manages task dependencies
- Ensures reproducibility and scheduling

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

dags/              → Airflow workflows
scripts/           → ETL + ML pipeline logic
data/raw/          → Raw input datasets
dbt/               → Data warehouse models
models/            → Trained ML models
docker-compose.yml → Infrastructure setup
requirements.txt   → Dependencies

## 🚀 Execution Modes

### ▶ Manual Execution
```bash
python scripts/load_raw_data.py
python scripts/train_model.py
```
### ▶ Airflow Execution

Triggered via:
```bash
dags/warehouse_pipeline.py
```
---

## 🧠 Key Engineering Highlights

- End-to-end data platform simulation
- Hybrid architecture (batch + warehouse + ML)
- dbt-based warehouse modeling
- Airflow orchestration layer
- Production-style modular design
- Scalable data engineering structure

---

## 🚀 Outcome

This project demonstrates a real-world analytics platform architecture combining:

- Data engineering (ETL pipelines)
- Data warehousing (dbt star schema)
- Workflow orchestration (Airflow)
- Machine learning integration

It represents how modern data platforms are structured in production environments.
