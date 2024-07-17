import psycopg2
import string
import random


def get_random_string(n):
    result = "".join(random.choices(string.ascii_uppercase + string.digits, k=n1))
    return result


try:
    conn = psycopg2.connect(
        database="prod_db",
        user="prod_user",
        password="prod_pwd",
        host="localhost",
    )
    # conn = psycopg2.connect(
    #     database="dev_db",
    #     user="dev_user",
    #     password="dev_pwd",
    #     host="localhost",
    #     port="6543",
    # )
    cursor = conn.cursor()
    for i in range(2000):
        n1 = random.randint(5, 15)
        n2 = random.randint(3, 10)
        postgres_insert_query = (
            """ INSERT into employees (name, state) VALUES (%s, %s)"""
        )
        record_to_insert = (get_random_string(n1), get_random_string(n2))
        cursor.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into employees table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into employees table", error)

finally:
    # closing database connection.
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")
