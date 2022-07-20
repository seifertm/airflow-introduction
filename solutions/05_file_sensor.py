from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor


def print_name(ti):
    name = ti.xcom_pull()
    return f"Hello {name}!"


with DAG(
    "my_first_dag",
    schedule_interval="*/3 * 21 07 *",
    start_date=datetime(2022, 7, 1),
    max_active_runs=1,
    catchup=False,
) as dag:
    sensor = FileSensor(task_id="wait_for_file", filepath="run_dag")
    t1 = BashOperator(task_id="a", bash_command="echo Michael")
    t2 = PythonOperator(task_id="b", python_callable=print_name)
    t3 = EmptyOperator(task_id="d")

    sensor >> t1 >> t2 >> t3
