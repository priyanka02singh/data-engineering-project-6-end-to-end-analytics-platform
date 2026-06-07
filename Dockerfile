FROM apache/airflow:2.8.1

USER root

RUN apt-get update && apt-get install -y gcc python3-dev git

USER airflow

RUN pip install pandas sqlalchemy psycopg2-binary dbt-core dbt-postgres