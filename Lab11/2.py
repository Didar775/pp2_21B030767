from config import config
import psycopg2

# to chech user exist by name and surname

def check(first_name):
    sql1 = """
    SELECT EXISTS(SELECT * from phonebookk WHERE first_name = %s)
    """
   
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur1 = conn.cursor()
        cur1.execute(sql1,[first_name])
        f =cur1.fetchone()

      

        conn.commit()
        return(f[0])
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()



def insert_user(first_name, last_name, phone_number):
    sql = """
    INSERT INTO phonebookk(first_name, last_name, phone_number)
    VALUES(%s, %s, %s)
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,(first_name, last_name, phone_number))
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()


def update(phone_number, first_name):
    sql = """
    UPDATE phonebookk SET phone_number = %s where first_name = %s
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (phone_number, first_name))
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

first_name = input('Enter first_name: ')
last_name = input('Enter last_name: ')
phone_number = input('Enter phone number: ')

checked = check(first_name)

if checked == True:
    update(phone_number, first_name) 
else:
    insert_user(first_name, last_name,phone_number)






    
