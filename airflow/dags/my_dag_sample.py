import datetime

from airflow.sdk import dag, task
import requests
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


@dag(
     start_date=datetime.datetime(2025, 9, 29), 
     schedule="@daily", 
     tags=["example", "james"]
    )
def sample_dag_james():
  

    @task()
    def obter_usuarios():
        res = requests.get("https://jsonplaceholder.typicode.com/users").json()
        res = {"users": [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"}
        ]}
        return res
    

    insert_users = SQLExecuteQueryOperator(
        task_id="insert_usuarios",
        conn_id="dw_corp",
        sql="insert into usuarios (name, email) values ('%(name)', '%(email)')",
        params=obter_usuarios,
    )

  

    obter_usuarios >> insert_users


sample_dag_james()