import psycopg2
from config import config

def create_table():
    sql = """
        CREATE TABLE snake(
        Username VARCHAR (50) UNIQUE NOT NULL ,
        User_score VARCHAR (50) NOT NULL,
        User_level VARCHAR (50) NOT NULL
        );

    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

create_table()
