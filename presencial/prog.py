import requests
# jsonplaceholder
result = requests.get("https://jsonplaceholder.typicode.com/posts")
data = result.json()
print(data)

import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=mydatabase user=myuser password=mypassword")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("""create table public.myposts(
            id int,
            user_id int,
            title varchar(500)
            )""")
conn.commit()
# Close the cursor and connection
cur.close()
conn.close()


cur.execute("""INSERT INTO public.myposts (id, user_id, title) VALUES (%s, %s, %s)""", (1,10, "curso da aws e maravilhoso, mas o trabalho e top"))