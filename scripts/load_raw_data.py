from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine(
    "postgresql://airflow:airflow@postgres:5432/warehouse_db"
)

customers = pd.read_csv("/opt/airflow/data/raw/customers.csv")
products = pd.read_csv("/opt/airflow/data/raw/products.csv")
orders = pd.read_csv("/opt/airflow/data/raw/orders.csv")
payments = pd.read_csv("/opt/airflow/data/raw/payments.csv")

customers.columns = customers.columns.str.strip()
products.columns = products.columns.str.strip()
orders.columns = orders.columns.str.strip()
payments.columns = payments.columns.str.strip()

with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE raw_orders CASCADE"))
    conn.execute(text("TRUNCATE TABLE raw_customers CASCADE"))
    conn.execute(text("TRUNCATE TABLE raw_products CASCADE"))
    conn.execute(text("DROP TABLE IF EXISTS raw_payments CASCADE"))

customers.to_sql("raw_customers", engine, if_exists="append", index=False)
products.to_sql("raw_products", engine, if_exists="append", index=False)
orders.to_sql("raw_orders", engine, if_exists="append", index=False)
payments.to_sql("raw_payments", engine, if_exists="append", index=False)

print("Raw e-commerce data loaded successfully!")