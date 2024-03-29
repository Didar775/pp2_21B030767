import psycopg2
from config import config

def insert(name, email):
    sql = """
    INSERT INTO accounts(username, adress)
    VALUES(%s, %s) RETURNING user_id;
    """
    
    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name,  email))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
    
    return user_id 

s = input()
l = input()
insert(s, l)