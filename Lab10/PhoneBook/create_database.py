import psycopg2
date_b = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'Zangar.2012'
)
date_b.autocommit = True
dt = date_b.cursor()
sql = ''' CREATE database Phone'''
dt.execute(sql)
print('Datebase created succesfully')