from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.empty import EmptyOperator


with DAG(
    "my_first_dag",
    schedule_interval=None,
    start_date=datetime(2022, 7, 1),
    catchup=False,
) as dag:
    t1 = EmptyOperator(task_id="a")
    t2 = EmptyOperator(task_id="b")
    t3 = EmptyOperator(task_id="c")
    t4 = EmptyOperator(task_id="d")

    t1 >> [t2, t3] >> t4
