#python 3.5
#取出一款车所有specid
import codecs
import urllib.request

###########################
#seriesid='3786'          #
###########################

response = urllib.request.urlopen('http://car.autohome.com.cn/config/series/3786.html')
html =str(response.read(),'gb2312')


import re

regex=re.compile('specsList.*?]')
result=regex.findall(html)


specidlist=re.compile('"specid":\d*')

specidresult=specidlist.findall(result[0])#总共有3条匹配的，取出一条提取specid

content=''
for string in specidresult:
    content=content+string+"\n"

content=content.replace('"specid":','')


f=codecs.open('D:/specid.txt','w','utf-8')
f.write(content)
f.close()