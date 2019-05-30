import sqlite3
co=sqlite3.connect('fvtttttttt.db')
c=co.cursor()
c.execute("CREATE TABLE if not exists `userers` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `login` TEXT NOT NULL, `password` TEXT NOT NULL, `number` INTEGER NOT NULL, `age` INTEGER NOT NULL, `mail` TEXT NOT NULL )")
c.execute("CREATE TABLE if not exists `comptetition` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `login` TEXT NOT NULL, `place` INTEGER NOT NULL, `competition` INTEGER NOT NULL )")
#c.execute("insert into userers(login,password,number,age,mail) values ('ktttttttt97644','lol0975','89241552434','18','adkawdaw@mail.ru')")
#c.execute("insert into comptetition(login,place,competition) values ('ktttttttt97644','1','1')")
data=c.execute("select login from comptetition where place = 1").fetchall()
print(data)
co.commit()
c.close()
co.close()

