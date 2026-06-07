from airflow import DAG 
from airflow.operators.python import PythonOperator 
from datetime import datetime


def hello_world():
    print("Project 6 Airflow is working!"
) 

default_args = { 
    "owner": "Priyanka",
}

with DAG(
    dag_id="test_project6_dag", 
    default_args=default_args, 
    start_date=datetime(2026, 5, 19), 
    schedule_interval=None,
    catchup=False,
) as dag:

    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=hello_world,
    )
