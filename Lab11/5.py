import psycopg2
from config import config

def delete(item ,data):

    sql = f"DELETE FROM phonebookk where {item} = {data}"
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (item, data))
     
        conn.commit()
        cur.close()

    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

item = input("Enter item to deleting data from tables by first_name or phone_number: ")
data = input((f'Enter {item}: '))

delete(item, data)
        