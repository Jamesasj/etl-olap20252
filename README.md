comando para pyenv
```
 python -m venv .venv
```

./Script para ativar o ambiente virtual
```
instalar dependências
``` 
pip install pandas
pip install numpy
pip freeze > requirements.txt
pip install -r requirements.txt
```

comando para instalar o MS SQL Server

```bash
docker run -e "ACCEPT_EULA=Y" -e  "MSSQL_SA_PASSWORD=Senha123" -p 1433:1433 --name sql1 --hostname sql1 -d mcr.microsoft.com/mssql/server:2019-latest
```

- Apos iniciar o banco de dado sera necessario restartar o backup do banco de dados AdventureWorks

https://superset.apache.org/docs/using-superset/exploring-data/
