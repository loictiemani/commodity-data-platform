from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.ingestion.eia_api_ingest import fetch_eia_data
from src.transformation.spark_transforms import transform_data
from src.ingestion.web_scraper import scrape_oil_news


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'commodity_data_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['commodity', 'ETL']
) as dag:

    ingest_task = PythonOperator(
        task_id='ingest_eia_data',
        python_callable=fetch_eia_data
    )

    transform_task = PythonOperator(
        task_id='transform_data_spark',
        python_callable=transform_data
    )
    ingest_task_web = PythonOperator(
        task_id='ingest_web_srape',
        python_callable=scrape_oil_news
    )

    [ingest_task,ingest_task_web] >> transform_task
