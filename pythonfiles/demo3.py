#python 3.5
import urllib.request
response = urllib.request.urlopen('http://car.autohome.com.cn/config/series/3788.html')
html =str(response.read(),'gb2312')

#print(html)


import re
#regex=re.compile('{"seriesid":.*}]}]}]}')
regex=re.compile('"name":".*?"')
result=regex.findall(html)

print(result)



