import psycopg2
from config import config

def update(change_need, new_element, local):
    global sql
    if change_need == 'last_name':
        sql = """
        update phonebookk
        set last_name = %s 
        where first_name = %s
        """
    elif change_need == 'first_name':
        sql = """
        update phonebookk
        set first_name = %s 
        where last_name = %s
        """
    else:
        sql = """
        update phonebookk
        set phone_number = %s 
        where first_name = %s
        """


    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (new_element, local))
     
        conn.commit()
        cur.close()

    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

a = input("Select the item you want to change(first_name, last_name, phone_number): ")

b = input(f"Enter new {a}: ")

if a == "first_name":
    c = input("Enter last_name of element you want to change: ")
elif a == 'phone_number':
    c = input('Enter first name of element you want to change: ')
else:
    c = input("Enter first_name of element you want to change: ")


update(a,b,c)


