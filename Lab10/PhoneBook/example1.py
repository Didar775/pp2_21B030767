# \l  - list all databases
# \c database_name - connect to databases
# \dt - list of all tables
# \q -  quit

import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'onefit',
    user = 'onefit',
    password = 'onefit'
)


sql = "select id, user_type, subscription_id from authe_usertype where subscription _id = 63"
cursor = conn.cursor()
cursor.execute(sql)
all_rows = cursor.fetchall()

for row in all_rows:
    print(row)

cursor.close()
conn.close()