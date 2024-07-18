import traceback
import psycopg2
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.traceback import install

install()  # This will replace the default traceback with a rich traceback

console = Console()
# Load environment variables from .env file
load_dotenv()

# Access the variables
environment = os.getenv("ENVIRONMENT")
if environment == "PROD":
    host = os.getenv("PROD_HOST")
    user = os.getenv("PROD_USER")
    pwd = os.getenv("PROD_PWD")
    db = os.getenv("PROD_DB")
    port = os.getenv("PROD_PORT")
else:
    host = os.getenv("DEV_HOST")
    user = os.getenv("DEV_USER")
    pwd = os.getenv("DEV_PWD")
    db = os.getenv("DEV_DB")
    port = os.getenv("DEV_PORT")

console.print(environment, host, user, pwd, db, port)
try:
    conn = psycopg2.connect(
        database=db,
        user=user,
        password=pwd,
        host=host,
        port=port,
    )
    console.print(f"[green]Conn: {conn}\n[/green]")
except Exception as e:
    console.print(f"Error {e}")
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
console.rint("[blue bold]PostgreSQL connection is closed[/]")
