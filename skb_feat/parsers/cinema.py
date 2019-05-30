import requests
import re
import datetime
import sqlite3
import time
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
conn = sqlite3.connect('db.db')
c = conn.cursor()
for daynum in range(3):
    date = datetime.datetime.today()
    day = int(date.day) + daynum
    if date.month <10 :
        date = str(date.year) + "0" + str(date.month)
        if day <10:
             date+="0"
        date+=str(day)
    else:
        date = str(date.year) + str(date.month)
        if day <10:
             date+="0"
        date+=day
    url = "https://nsk.kinoafisha.info/afisha/schedule/?order=movie&date%5B%5D={}&time=all&movies=0&cinemas=0&tickets=0&price=".format(date)
    s = requests.get
    r= s(url,headers=headers)
    r.encoding = 'utf-8'
    kawdkawfkawd = re.split(r'<form data-modules="Accordion" class="accordion borderColor bottom50" action="">',r.text)
    inamefilm = re.split(r'"><span class="link link-filmsName"><span class="link_border">',kawdkawfkawd[0])
    for i in range(len(inamefilm)-1):
        cite = re.split(r'<a href="',inamefilm[i])
        cite = "https:" + str(cite[-1])
        kek = s(cite, headers=headers)
        kek.encoding = 'utf-8'
        if (re.findall(r'<span class="movieInfoV2_descText">', kek.text) != []):
            idesc = re.split(r'<span class="movieInfoV2_descText">\s{0,50}<p\s{0,5}\w{0,10}\={0,1}\"{0,1}\w{0,10}\-{0,1}\w{0,10}\:{0,1}\w{0,10}\"{0,1}>',kek.text)
            desc = re.split(r'</p>',idesc[1])
        else:
            desc[0] = "Артхаус"
        namefilm = re.split(r'</span></span></a>',inamefilm[i+1])
        icinemaname = re.split(r'class="link_border">',namefilm[1])
        for k in range(len(icinemaname)-1):
            cinemaname = re.split(r'</span></a>', icinemaname[k+1])
            if (len(re.findall(r'session2_price', cinemaname[1])) == len(re.findall(r'session2_time', cinemaname[1]))):
                itime = re.split(r'"session2_time">',cinemaname[1])
                for d in range(len(itime)-1):
                    timew = re.split(r'</span>',itime[d+1])
                    cost = re.split(r'<span class="session2_price">',timew[1])
                    cost = re.split(r'\s{1,5}',cost[1])
                    print(str(namefilm[0]) + " " + str(cinemaname[0]) + " " + timew[0] + " " + cost[0] + " " + desc[0])
                    date = datetime.datetime.today()
                    month = date.month
                    year = date.year
                    day = int(date.day) + daynum
                    date = str(day)+ "." + str(date.month) + "." + str(date.year)
                    date = ""
                    if day < 10:
                        date = "0"
                    date = date + str(day) + "."
                    if month < 10:
                        date += "0" + str(month) + "." + str(year)
                    else:
                        date += str(month) + "." + str(year)
                    c.execute("INSERT INTO events(time, people, cost, desc, place,category,date) values ('{0}', '{1}','{2}', '{3}', '{4}', '{5}', '{6}')".format(str(timew[0]),0,int(cost[0]),str(desc[0]),str(cinemaname[0]), "Кино", str(date)))
    r.close()
    kek.close()
conn.commit()
c.close()
conn.close()
