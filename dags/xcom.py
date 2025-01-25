from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.python import PythonOperator


dag = DAG('exemplo_xcom', description="Primeiro xcom",
        schedule_interval=None,start_date=datetime(2025,1,23),
        catchup=False) #se o catchup estiver como true, ele vai rodar tudo pra trás caso o start date estiver definido como uma data anterior a data atual do sistema

def task_write(**kwarg):
    kwarg['ti'].xcom_push(key='valorxcom1', value=10200)

task1 = PythonOperator(task_id="tks1", python_callable=task_write, dag = dag)

def task_read(**kwarg):
    valor = kwarg['ti'].xcom_pull(key='valorxcom1')
    print(f"valor recuperado: {valor}")

task2 = PythonOperator(task_id="tks2", python_callable=task_read, dag = dag)

task1 >> task2
