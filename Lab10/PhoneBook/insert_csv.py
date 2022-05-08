import psycopg2, csv
from config import config

with open('nomer.csv', 'r') as folder:
    l = list(csv.reader(folder))

def insert_user_list(user_list):
    sql = """
    insert into phonebookk(first_name, last_name, phone_number) values (%s, %s, %s);

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


insert_user_list(l)