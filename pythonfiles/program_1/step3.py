#python 3.5
#取出一款汽车（根据specid）的所有属性值
import codecs
import urllib.request

###########################
htmlid='3786'             #
###########################

response = urllib.request.urlopen('http://car.autohome.com.cn/config/series/'+htmlid+'.html')
html =str(response.read(),'gb2312')


import re

###########################
specid='27306'            #
###########################

regex=re.compile('{"specid":'+specid+',"value":".*?"')
result=regex.findall(html)

content=''
for string in result:
    content=content+string+"\n"

content=content.replace('{"specid":'+specid+',"value":','')

content=content.replace('"','')

f=codecs.open('D:/value.txt','w','utf-8')
f.write(content)
f.close()



