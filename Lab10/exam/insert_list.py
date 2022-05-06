import psycopg2
from config import config

def insert_user_list(user_list):
    sql = """
    insert into accounts(username, adress) values (%s, %s);

    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql,(user_list))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

l = [
    ("dis5", "das8@gmail.com"),
    ("dias10", "dias10@gmail.com"),
    ("dias5", "dis3@gmail.com"),
    ("das4", "dis4@gmail.com"),
]
insert_user_list(l)