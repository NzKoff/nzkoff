import sqlite3
import hashlib
import psycopg2

from psycopg2.extras import RealDictCursor
general_db_file_location = "database_files/general.db"


def sql_execute(sql_give):
    conn = psycopg2.connect(dbname='feat', user='feat', password='feat', host='localhost')
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    answer = None

    # print(sql_give)
    cursor.execute(sql_give)
    conn.commit()
    try:
        answer = cursor.fetchall()
    except:
        pass
    finally:
        conn.close()
        cursor.close()
        return answer



# def db_cmp_passwd(login, passwd):
#
#
#     hash = _c.execute("select passwd from users where login = " + login + ";").fetchone()
#     result = hash[0][0] == hashlib.sha256(passwd.encode()).hexdigest()
#     _conn.close()
#
#     return result
#
#
# def db_check_user(login, passwd):
#     _conn = sqlite3.connect(general_db_file_location)
#     _c = _conn.cursor()
#
#     hash = _c.execute("select count(*) from users where login = " + login + ";").fetchall()
#     result = hash[0][0] == hashlib.sha256(passwd.encode()).hexdigest()
#     _conn.close()
#
#     return result


def db_add_user(data):


    sql  ="""INSERT INTO user10(login, password,firstname,secondname)
             VALUES('{login}','{password}','{firstname}','{secondname}')
    """.format(**data)
    sql_execute(sql)


def get_id_user(data):
    sql = """SELECT id
             from user10
             where login = '{login}' and 
             password = '{password}'""".format(**data)
    return sql_execute(sql)[0]


def add_info(data):
    sql = """
            INSERT INTO events(id,time_start,count_persons,price,description,address,name,date)
            VALUES({id},'{time_start}','{count_persons}',{price},'{description}','{address}','{name}','{date}'::DATE)
    """.format(**data)
    sql_execute(sql)


def get_info():
    sql = """
          SELECT id,time_start,count_persons,price,description,address,name,date :: text
          from events
    
    """
    return sql_execute(sql)


# def db_delete_user(login):
#     _conn = sqlite3.connect(general_db_file_location)
#     _c = _conn.cursor()
#
#     _c.execute("delete from users where login =  '" + login + "'; ")
#
#     _conn.commit()
#     _conn.close()




#print(verify("roma_lox", "degenerat"))

#print(hashlib.sha256("degenerat".encode()).hexdigest())