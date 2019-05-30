import requests
import re
rmd = [requests.get('https://pogoda.ngs.ru/kaliningrad'), requests.get('https://pogoda.29.ru/'),
     requests.get('https://pogoda.ngs.ru/'), requests.get('https://pogoda.ngs23.ru/anapa')]
for k in range(4):
    r = rmd[k]
    citys = re.split(r'cit\w{0,10}\-{0,3}\w{0,10}\"\shref="',r.text)
    temps = re.split(r'value__main">',r.text) + re.split(r'temp">',r.text)[1:]
    city = []
    temp = []
    if (len(citys) == len(temps)):
        for i in range(1,len(citys)):
            cityy = citys[i]
            city.append(cityy)
            tempp = temps[i]
            temp.append(tempp)
            cityse = re.split(r'title="', city[i-1])
            cityd = re.split(r'"', cityse[1])
            tempd = re.split(r'<', temp[i-1])
            tempeed = tempd[0]
            if 'minus' in tempd[0]:
                tempeed = "-" + tempd[0][7:]
            print("Город: " + cityd[0] + ". Температура: " + tempeed)
    print("\n")