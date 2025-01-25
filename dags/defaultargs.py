from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

argumentos_default = {
    'depends_on_past' : False,
    'start_date' : datetime(2025,1,23),
    'email' : ['teste@teste.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

dag = DAG('defaultargs', description="Default Args",
          default_args= argumentos_default,
        schedule_interval='@hourly',start_date=datetime(2025,1,23),
        catchup=False, default_view='graph', tags=['processo', 'tag', 'pipeline']) #se o catchup estiver como true, ele vai rodar tudo pra trás caso o start date estiver definido como uma data anterior a data atual do sistema

task1 = BashOperator(task_id="tks1",bash_command="sleep 5", dag = dag, retries=3)
task2 = BashOperator(task_id="tks2",bash_command="sleep 5", dag = dag)
task3 = BashOperator(task_id="tks3",bash_command="sleep 5", dag = dag)

task1 >> task2 >> task3
