from numpy import size
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
def get_info_certain(sizee):
    sql = f'SELECT * FROM phonebookk'

    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchmany(sizee)
        for row in rows:
            print(row)

        
    
    except Exception as e:
        print(str(e))


get = input('What you want to get(all_record,first_name, last_name, phone_number,fetchone): ')

if get == 'fetchone':
    sizee = int(input('Enter size: '))
    get_info_certain(sizee)
else:
    get_info_all(get)


