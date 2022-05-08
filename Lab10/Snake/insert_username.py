from tokenize import PseudoExtras
from config import config
import psycopg2

def check(username):
    sql = """
    SELECT EXISTS(SELECT * from snake WHERE username = %s)
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,[username])
        l =cur.fetchone()
        conn.commit()
        return(int(l[0]))
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()


def insert_user(username, user_score, user_level):
    sql = """
    INSERT INTO snake(username, user_score, user_level)
    VALUES(%s, %s, %s)
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,(username, user_score, user_level))
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()


def update(username, user_score, user_level):
    sql = """
    UPDATE snake SET user_score = %s, user_level = %s where username = %s
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_score, user_level,username))
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()




    
