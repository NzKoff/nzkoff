import requests
import re
import json

url = "https://pogoda.ngs.ru/"
r = requests.get(url)
start = re.split(r'au-cr-select__box _container_all_regions',r.text)
end = re.split(r'au-container-cities-in-region _container_cities_in_region',start[1])
region = re.findall(r'data-id="(\d{0,6})"',end[0])
for i in range(len(region)):
    data = json.dumps({"jsonrpc": "2.0", "method": "getCities", "params": ["region=" + region[i]], "id": 0})
    obl = requests.post("https://pogoda.ngs.ru/menu/json", data)
    dat = obl.json()
    try:
        for n in range(len(dat['result'])):
            urlc = dat['result'][n]['url']
            if "pogoda.45.ru" in urlc:
                print("Страница этого города недоступна")
            elif "pogoda.75.ru" in urlc:
                print("Страница этого города недоступна")
            else:
                if "https:" in urlc:
                    urlc = urlc[6:]
                urlc = "https:" + urlc
                r = requests.get(urlc)
                city = re.findall(r'vs-dropdown__switcher vs-dropdown_in-city" href="#" title="(\w{0,40}\-{0,3}\s{0,3}\w{0,10}\-{0,3}\s{0,3}\w{0,40})"', r.text)
                temp = re.findall(r'<span class="value__main">(\+{0,1}\&{0,2}\w{0,10}\;{0,2}\w{0,5})<', r.text)
                tempeed = temp[0]
                if 'minus' in temp[0]:
                    tempeed = "-" + temp[0][7:]
                info = "В городе: " + city[0] + ". Температура: " + tempeed
                print(info)
    except:
        print("")