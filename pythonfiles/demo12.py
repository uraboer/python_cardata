#python 3.5
#取出A分类下所有seriesid号(拼接url使用)
import codecs
import urllib.request

###########################
seriesid='A'             #
###########################

response = urllib.request.urlopen('http://www.autohome.com.cn/grade/carhtml/'+seriesid+'.html')
html =str(response.read(),'gb2312')


import re

regex=re.compile('"s\d*?"')
result=regex.findall(html)

content=''
for string in result:
    content=content+string+"\n"

content=content.replace('"','')
content=content.replace('s','')

f=codecs.open('D:/seriesid.txt','w','utf-8')
f.write(content)
f.close()



