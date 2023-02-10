from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator


main_dag_id = 'scheduler_cleanup'


args = {
    'owner': 'linhai',
    'start_date': datetime(2021, 7, 21),
    'provide_context': True
}



with DAG(
        main_dag_id,        
        catchup=False,
        concurrency=4,
        schedule='@daily',
        owner_links={"linhai": "https://www.hahalolo.com/@linhxt"},
        default_args=args) as dag:

        clean_scheduler_logs = BashOperator(task_id='clean_scheduler_logs',
                            bash_command="find $AIRFLOW_HOME/logs/scheduler -type f -mtime +7 -delete")
       

        clean_scheduler_logs