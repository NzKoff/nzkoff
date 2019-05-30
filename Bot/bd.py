import sqlite3

#Открываем БД или создаём
conn = sqlite3.connect('bot.db')
#Курсор для работы
c = conn.cursor()
#Создание таблицы
c.execute("CREATE TABLE if NOT EXISTS bot(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, chatid NUMBER NOT NULL, flag1 TEXT NOT NULL, flag2 TEXT NOT NULL, flag3 TEXT NOT NULL, flag4 TEXT NOT NULL, flag5 TEXT NOT NULL, flag6 TEXT NOT NULL, flag7 TEXT NOT NULL, answer TEXT NOT NULL, teamnum NUMBER NOT NULL)")
c.execute("CREATE TABLE if NOT EXISTS flags(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, flag TEXT NOT NULL)")
c.execute("CREATE TABLE if NOT EXISTS answer(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, flag TEXT NOT NULL, teamnum NUMBER NOT NULL)")
#Сохраняем
conn.commit()
#Закрываем курсор
c.close()
#Закрываем базу
conn.close()

