#python 3.5
#取出所有汽车参数字段187左右
import codecs
import urllib.request

###########################
htmlid='3786'             #
###########################

response = urllib.request.urlopen('http://car.autohome.com.cn/config/series/'+htmlid+'.html')
html =str(response.read(),'gb2312')


import re

regex=re.compile('{"name":".*?","valueitems"')
result=regex.findall(html)

content=''
linesnum=1 #插入数据库时range从1算起，所以要加一
#统计参数字段的行数，因为value值可能取到后面颜色部分
for string in result:
    content=content+string+"\n"
    linesnum=linesnum+1 #统计行数


content=re.sub('{"name":".*?","configitems":\[','',content)
content=re.sub('{"name":".*?","paramitems":\[','',content)
content=content.replace('{"name":','')
content=content.replace(',"valueitems"','')
content=content.replace('"','')

f=codecs.open('D:/category.txt','w','utf-8')
f.write(content)
f.close()

print(linesnum)
