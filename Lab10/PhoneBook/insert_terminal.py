import psycopg2
from config import config

def insert(first_name,  last_name, phone_number):
    sql = """
    INSERT INTO phonebookk(first_name, last_name, phone_number)
    VALUES(%s, %s, %s);
    """
    
    conn = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (first_name,  last_name, phone_number))

        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
    


f = input()
l = input()
n = input()
insert(f, l, n)