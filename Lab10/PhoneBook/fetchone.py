import psycopg2
from config import config

#to get all record
def get_info_all(get_what):

    if get_what == 'all_record':
        sql = 'SELECT * FROM phonebookk' 
    else:
        sql = f'SELECT {get_what} FROM phonebookk'
        

    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
     
        cur = conn.cursor()
        cur.execute(sql)
        table = cur.fetchall()

        for row in table:
            print(row)
        conn.commit()
      
      
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()



# to get cettain record
def get_info_certain(item , username):
    sql = f'SELECT * FROM phonebookk WHERE'

    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()

        print(row)
    
    except Exception as e:
        print(str(e))


get = input('What you want to get(all_record,first_name, last_name, phone_number,fetchon): ')

if get == 'fetchone':
    item = input('Querying data from the tables with last_name or first_name: ')
    username = input(f'Enter {item}: ')
    get_info_certain(item, username)
    
else:
    get_info_all(get)


