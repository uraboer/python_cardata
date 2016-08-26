# coding:utf-8
import codecs
import urllib.request
import linecache
import re
import pymysql
import time

#demo11###########################
conn = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='qichezhijia',
    charset='gb2312'
)

cursor = conn.cursor()

sql = "CREATE TABLE cardata(specid VARCHAR(10),category VARCHAR(50), carvalue VARCHAR(50))ENGINE=INNODB"

cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()
############################


#demo12###########################
f = codecs.open('D:/seriesid.txt', 'w', 'utf-8')
f.write('')
f.close()
Char=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

for grade in Char:
    response = urllib.request.urlopen('http://www.autohome.com.cn/grade/carhtml/' + grade + '.html')
    html_1 = str(response.read(), 'gb2312')

    regex = re.compile('"s\d*?"')
    result1 = regex.findall(html_1)

    content = ''
    for string in result1:
        content = content + string + "\n"

    content = content.replace('"', '')
    content = content.replace('s', '')

    f = codecs.open('D:/seriesid.txt', 'a', 'utf-8')
    f.write(content)
    f.close()


n=0
for n in range(1,20):
    seriesid=linecache.getline('d:/seriesid.txt',n)
    seriesid=seriesid.replace('\n','')
    #demo13###########################
    response = urllib.request.urlopen('http://car.autohome.com.cn/config/series/'+seriesid+'.html')
    html = str(response.read(), 'gb2312')

    f = codecs.open('D:/specid.txt', 'w', 'utf-8')
    f.write('')
    f.close()
    f = codecs.open('D:/specidnum.txt', 'w', 'utf-8')
    f.write('')
    f.close()

    regex = re.compile('specsList.*?]')
    result_specid = regex.findall(html)

    if(len(result_specid)>0):
        specidlist = re.compile('"specid":\d*')
        specidresult = specidlist.findall(result_specid[0])
        i=0
        content2 = ''
        for string in specidresult:
            content2 = content2 + string + "\n"
            i+=1
        content3 = content2.replace('"specid":', '')
        f = codecs.open('D:/specid.txt', 'w', 'utf-8')
        f.write(content3)
        f.close()
        f = codecs.open('D:/specidnum.txt', 'w', 'utf-8')
        f.write(str(i))
        f.close()
    else:
        content4=''
    ###########################


    # demo7###########################

    z=linecache.getline('D:/specidnum.txt',1)


    response = urllib.request.urlopen('http://car.autohome.com.cn/config/series/' + seriesid + '.html')
    html = str(response.read(), 'gb2312')

    regex = re.compile('{"name":".*?","valueitems"')
    result = regex.findall(html)

    content_category = ''
    linesnum = 1
    for string in result:
        content_category = content_category + string + "\n"
        linesnum = linesnum + 1

    content_category = re.sub('{"name":".*?","configitems":\[', '', content_category)
    content_category = re.sub('{"name":".*?","paramitems":\[', '', content_category)
    content_category = content_category.replace('{"name":', '')
    content_category = content_category.replace(',"valueitems"', '')
    content_category = content_category.replace('"', '')

    f = codecs.open('D:/category.txt', 'w', 'utf-8')
    f.write(content_category)
    f.close()

    f = codecs.open('D:/linesnum.txt', 'w', 'utf-8')
    f.write(str(linesnum))
    f.close()
    ############################


    # demo8###########################
    specid=linecache.getline('d:/specid.txt',n)
    specid=specid.replace('\n','')

    response = urllib.request.urlopen('http://car.autohome.com.cn/config/series/'+seriesid+'.html')
    html_4 = str(response.read(), 'gb2312')

    regex = re.compile('{"specid":' + specid + ',"value":".*?"')
    result = regex.findall(html_4)

    content_specidevery = ''
    for string in result:
        content_specidevery = content_specidevery + string + "\n"

    content_value = content_specidevery.replace('{"specid":' + specid + ',"value":', '')

    content_value = content_value.replace('"', '')

    f = codecs.open('D:/value.txt', 'w', 'utf-8')
    f.write(content_value)
    f.close()

    content_specid = content_specidevery.replace('{"specid":', '')
    content_specid = re.sub(',"value":".*', '', content_specid)

    f = codecs.open('D:/specid_everycar.txt', 'w', 'utf-8')
    f.write(content_specid)
    f.close()
    ############################


    # demo10###########################
    conn = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='qichezhijia',
        charset='gb2312'
    )

    cursor = conn.cursor()

    n1 = 0
    content = ''
    a4 = linecache.getline('d:/linesnum.txt', 1)
    a4 = int(a4)
    for n1 in range(1, a4):
        a1 = linecache.getline('d:/specid_everycar.txt', n1)
        a2 = linecache.getline('d:/category.txt', n1)
        a3 = linecache.getline('d:/value.txt', n1)
        sql = "insert into cardata(specid,category,carvalue) VALUES (\'%s\',\'%s\',\'%s\')" % (a1, a2, a3)
        cursor.execute(sql)
        n1 += 1

    conn.commit()
    cursor.close()
    conn.close()
    ############################

    time.sleep(5)

    n+=1
