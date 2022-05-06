import psycopg2
from config import host , user , password , db_name

try:
    # connect to exist database
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'

        )
        print(f'SERVER')

    
except Exception as ex:
    print("[INFO] error while working with PostgreSQL", ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')