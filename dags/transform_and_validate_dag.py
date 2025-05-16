from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="transform_and_validate",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    transform = BashOperator(
        task_id="run_spark_job",
        bash_command="python /opt/airflow/src/transformation/spark_job.py"
    )

    validate = BashOperator(
        task_id="run_ge_validation",
        bash_command="python /opt/airflow/src/validation/run_validations.py"
    )

    transform >> validate
