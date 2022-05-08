import psycopg2
from config import config

def Limit(item1,item2):
    sql = f'SELECT * FROM phonebookk  LIMIT {item2} OFFSET {item1}'

    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(sql)
        rows = list(cur.fetchall())

        for row in rows:
            print(*row)
    
    except Exception as e:
        print(str(e))


l = list(map(int,input('Enter offset and limit of querying data: ').split()))
Limit(l[0], l[1])