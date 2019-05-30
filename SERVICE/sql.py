import re
import sqlite3
import random

#Открываем БД или создаём
conn = sqlite3.connect('sql.db')
#Курсор для работы
c = conn.cursor()
#Создание таблицы

k = c.execute("select * from users").fetchall()
d = c.execute("select * from competition").fetchall()
for i in range(350):
    print(k[i])
    print(d[i])
#Сохраняем
conn.commit()
#Закрываем курсор
c.close()
#Закрываем базу
conn.close()

