import psycopg2
from config import config

def update_user(user_id, username):
    sql = """
    update accounts
    set adress = %s
    where username = %s
    """
    conn = None
   
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_id, username))
     
        conn.commit()
        cur.close()

    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

id = input()
username = input()
update_user(id, username)
    