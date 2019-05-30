import re
import sqlite3
import random

#Открываем БД или создаём
conn = sqlite3.connect('sql.db')
#Курсор для работы
c = conn.cursor()
#Создание таблицы

c.execute("CREATE TABLE if NOT EXISTS users(id INTEGER NOT NULL"
          " PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, "
          "password TEXT NOT NULL, "
          "name TEXT NOT NULL, number NUMBER NOT NULL, "
          "city TEXT NOT NULL, years NUMBER NOT NULL)")
c.execute("CREATE TABLE if NOT EXISTS competition(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, place NUMBER NOT NULL, "
          "nombercomp NUMBER NOT NULL)")
logined = re.findall("\n(\w{0,50})",open('login.txt').read())
passed = re.findall("\n(\w{0,50})",open('passwords.txt').read())
cityed = re.findall("(\w{0,50})\n",open('city.txt').read())
named = re.findall("(\w{0,50})\n",open('name.txt').read())
NUM = ['Honda', 'Toyota', 'Ford', 'Mersedes', 'BMW']
NUM2 = [2012, 2011, 2015, 2011, 2014]
for i in range(350):
    c.execute("INSERT INTO users(username, password, name, number, city, years) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".
              format(logined[i], passed[i], named[random.randint(0,(len(named)-1))], int("89"+str(random.randint(100000000,999999999))),
                     cityed[random.randint(0,9)], 16+random.randint(0,10)))
    c.execute("INSERT INTO competition(username, place, nombercomp) values ('{0}', '{1}')".format(logined[i], i % 50 + 1, i // 50 + 1))
#Сохраняем
conn.commit()
#Закрываем курсор
c.close()
#Закрываем базу
conn.close()

