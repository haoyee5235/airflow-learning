from datetime import datetime, timedelta
from airflow import DAG 
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'haoyee',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id = "first_dag_v1",
    default_args = default_args,
    description = "The first Airflow DAG",
    start_date = datetime(2023, 7, 15),
    schedule_interval = '@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = 'echo Hello World, this is our first task'
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = 'echo Hello World, this is our first task'
    )

    task1.set_downstream(task2)

