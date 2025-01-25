from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('quarta_dag', description="Nossa quarta DAG", 
         schedule_interval=None,start_date=datetime(2025,1,23), 
         catchup=False) as dag: #se o catchup estiver como true, ele vai rodar tudo pra trás caso o start date estiver definido como uma data anterior a data atual do sistema

    task1 = BashOperator(task_id="tks1",bash_command="sleep 5")
    task2 = BashOperator(task_id="tks2",bash_command="sleep 5")
    task3 = BashOperator(task_id="tks3",bash_command="sleep 5")

    task1.set_upstream(task2)
    task2.set_upstream(task3)
    
