import sqlite3
from api.db_handle import *
conn = sqlite3.connect('general.db')
c = conn.cursor()
info = c.execute("SELECT * FROM events").fetchall()
c.close()
conn.close()
print(info,"\n")

for i in info:
    data = {
        "id":i[0],
        "time_start":i[1],
        "count_persons": i[2],
        "price" : i[3],
        "description":i[4],
        "address":i[5],
        "name" : i[6],
        "date":i[7]
    }
    add_info(data)


