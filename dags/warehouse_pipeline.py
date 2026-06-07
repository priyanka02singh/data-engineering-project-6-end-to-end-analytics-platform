from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "Priyanka",
}

DBT_SETUP = """
pip install --user dbt-core dbt-postgres &&
export PATH=$PATH:/home/airflow/.local/bin
"""

with DAG(
    dag_id="warehouse_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 5, 19),
    schedule_interval=None,
    catchup=False,
) as dag:

    load_raw_data = BashOperator(
        task_id="load_raw_data",
        bash_command="""
        cd /opt/airflow &&
        python3 scripts/load_raw_data.py
        """
    )

    run_dbt_models = BashOperator(
        task_id="run_dbt_models",
        bash_command="""
        cd /opt/airflow/dbt/ecommerce_warehouse &&
        dbt run --profiles-dir /opt/airflow/dbt_profiles
        """
    )

    run_dbt_tests = BashOperator(
        task_id="run_dbt_tests",
        bash_command="""
        cd /opt/airflow/dbt/ecommerce_warehouse &&
        dbt test --profiles-dir /opt/airflow/dbt_profiles
        """,
        dag=dag,
    )

    load_raw_data >> run_dbt_models >> run_dbt_tests