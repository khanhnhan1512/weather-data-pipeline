import sys
import os
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/api-request/src')

def safe_callable():
    from insert_records import main
    return main()

def example_task():
    print("This is an example task.")

default_args = {
    'description': 'A DAG to orchestrate data',
    'start_date': datetime(2025, 9, 16),
    'catchup': False,
}

dag = DAG(
    dag_id='weather-pipeline-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_callable
    )

    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(source='/home/nhan1512/weather-data-pipeline/dbt/my_project',
                  target='/usr/app',
                  type='bind'),
            Mount(source='/home/nhan1512/weather-data-pipeline/dbt/profiles.yml',
                  target='/root/.dbt/profiles.yml',
                  type='bind')
        ],
        network_mode='weather-data-pipeline_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success',
    )

    task1 >> task2