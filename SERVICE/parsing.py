import requests
import re

r = requests.get('https://pogoda.ngs.ru/berezovka')
start = re.split(r'Популярные города',r.text)
end = re.split(r'au-cr-select__box _container_all_regions',start[1])
citys = re.findall(r'data-url="\w{0,6}.{0,1}(//\w{0,10}\.\w{0,10}\-{0,1}\w{0,10}\.\w{0,10}.{0,1}\w{0,30})"',end[0])
print(len(citys))
for i in range(len(citys)):
    if "pogoda.45.ru" in citys[i]:
        print("Страница этого города недоступна")
    elif "pogoda.75.ru" in citys[i]:
        print("Страница этого города недоступна")
    else:
        citys[i] = 'https:' + citys[i]
        print(citys[i])
        r = requests.get(citys[i])
        city = re.findall(r'vs-dropdown__switcher vs-dropdown_in-city" href="#" title="(\w{0,40}\-{0,3}\s{0,3}\w{0,10}\-{0,3}\s{0,3}\w{0,40})"', r.text)
        temp = re.findall(r'<span class="value__main">(\+{0,1}\&{0,2}\w{0,10}\;{0,2}\w{0,5})<', r.text)
        tempeed = temp[0]
        if 'minus' in temp[0]:
            tempeed = "-" + temp[0][7:]
        info = "В городе: " + city[0] + ". Температура: " + tempeed
        print(info)