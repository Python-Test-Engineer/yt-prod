import psycopg2
from dotenv import load_dotenv
import os
from rich.console import Console

console = Console()
# Load environment variables from .env file
load_dotenv()

# Access the variables
prod_host = os.getenv("PROD_HOST")
prod_user = os.getenv("PROD_USER")
prod_pwd = os.getenv("PROD_PWD")
prod_db = os.getenv("PROD_DB")
prod_port = os.getenv("PROD_PORT")
console.print(prod_host, prod_user, prod_pwd, prod_db)

conn = psycopg2.connect(
    database=prod_db,
    user=prod_user,
    password=prod_pwd,
    host=prod_host,
    port=prod_port,
)
# conn = psycopg2.connect(
#     database="dev_db",
#     user="dev_user",
#     password="dev_pwd",
#     host="localhost",
#     port="6543",
# )
if conn:
    console.print(f"[green]Conn: {conn}\n[/green]")
else:
    console.print(f"[red]NO CONNECTION[/red]")

cursor = conn.cursor()

TABLE_NAME = "employees"

cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

# Creating table as per requirement
sql = f"""CREATE TABLE {TABLE_NAME} (
			name VARCHAR(255) NOT NULL,
            state VARCHAR(255) NOT NULL
            
)"""

try:
    cursor.execute(sql)
    conn.commit()
    print(f"{TABLE_NAME} table created successfully........\n")

except Exception as e:
    print(f"Error {e}")

try:
    sql = f"""
    ALTER TABLE IF EXISTS public.employees
    ADD CONSTRAINT "unique employees constraint" UNIQUE (name);
            
    """
    cursor.execute(sql)
    conn.commit()
    print(f"{TABLE_NAME} table altered successfully........\n")

except Exception as e:
    print(f"Error {e}")

cursor.close()
conn.close()
print("PostgreSQL connection is closed")
