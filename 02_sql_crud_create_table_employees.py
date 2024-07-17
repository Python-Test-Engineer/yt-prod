import psycopg2

# Establishing the connection
# environment:
#   - POSTGRES_DB=prod_db
#   - POSTGRES_USER=prod_user
#   - POSTGRES_PASSWORD=prod_pwd

conn = psycopg2.connect(
    database="prod_db",
    user="prod_user",
    password="prod_pwd",
    host="localhost",
)
if conn:
    print(f"Conn: {conn}\n")
else:
    print("NO CONNECTION\n")

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
    print(f"{TABLE_NAME} table created successfully........\n")

except Exception as e:
    print(f"Error {e}")

cursor.close()
conn.close()
print("PostgreSQL connection is closed")
