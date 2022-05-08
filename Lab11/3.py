import psycopg2
from config import config

def insert():
    n = int(input('Enter the number of users to enter: '))
    sql = """
    INSERT INTO phonebookk(first_name, last_name, phone_number)
    VALUES(%s, %s, %s);
    """
    
    conn = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for i in range(n):
            l = list(map(str,input().split()))
            cur.execute(sql, (l[0], l[1], l[2]))

        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
    


insert()