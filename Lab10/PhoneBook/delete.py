import psycopg2
from config import config

def delete(username):

    sql = "DELETE FROM phonebookk where first_name = %s"
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, [username])
     
        conn.commit()
        cur.close()

    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

first_name = input("Enter first name of item which you want to delete: ")
delete(first_name)
        