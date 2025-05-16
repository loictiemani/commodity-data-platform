from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
import os

def fetch_energy_data():
    response = requests.get("https://api.eia.gov/example")
    data = response.json()
    df = pd.DataFrame(data["series"])
    os.makedirs("/opt/airflow/data/raw", exist_ok=True)
    df.to_csv("/opt/airflow/data/raw/eia.csv", index=False)

with DAG(
    dag_id="data_ingestion_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    ingest_task = PythonOperator(
        task_id="fetch_energy_data",
        python_callable=fetch_energy_data,
    )

    ingest_task