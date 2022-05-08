import psycopg2
from config import config
 
def create_table():
    command = """
        CREATE TABLE Phonebookk (
            First_name VARCHAR (100) UNIQUE NOT NULL,
            Last_name VARCHAR (100)  UNIQUE NOT NULL,
            Phone_number VARCHAR (100) UNIQUE NOT NULL
        );
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
    
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
create_table()