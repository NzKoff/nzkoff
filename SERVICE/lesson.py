import sqlite3
import re
import random
conn = sqlite3.connect('sql2.db')
c = conn.cursor()

c.execute("CREATE TABLE if NOT EXISTS users(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
          "login TEXT NOT NULL, password TEXT NOT NULL, name TEXT NOT NULL, "
          "years NUMBER NOT NULL, city TEXT NOT NULL,number NUMBER NOT NULL,"
          "email TEXT NOT NULL)")

c.execute("CREATE TABLE if NOT EXISTS competition(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
          "login TEXT NOT NULL, place NUMBER NOT NULL, nombercomp NUMBER NOT NULL)")

logined = re.findall("(\w{0,50})\n",open('login.txt').read())
passed = re.findall("(\w{0,50})\n",open('passwords.txt').read())
cityed = re.findall("(\w{0,50})\n",open('city.txt').read())
named = re.findall("(\w{0,50})\n",open('name.txt').read())
mailed = ['@mail.ru','@gmail.com','@yandex.ru','@ngs.ru','@nzkoff.com']
for i in range(350):
    c.execute("INSERT INTO users(login, password, name, number, city, years, email) "
              "values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".
            format(logined[i], passed[i], named[random.randint(0, (len(named) - 1))],
                   int("89" + str(random.randint(100000000, 999999999))),
               cityed[random.randint(0, len(cityed)-1)], 16 + random.randint(0, 10),
                   logined[i]+mailed[random.randint(0,4)]))
    c.execute("INSERT INTO competition(login, place, nombercomp) values "
              "('{0}', '{1}', '{2}')".format(logined[i], i % 50 + 1,i // 50 + 1))

conn.commit()
c.close()
conn.close()