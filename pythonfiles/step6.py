#抓取seriesid和对应的specid
# coding:utf-8
import codecs
import urllib.request
import linecache
import re
import pymysql
import time


#创建连接，创建表
conn_create=pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='qichezhijia',
    charset='gb2312'
)

cursor_create = conn_create.cursor()


sql_create = "CREATE TABLE iddata(seriesid VARCHAR(20),specid VARCHAR(20))ENGINE=INNODB"


cursor_create.execute(sql_create)


conn_create.commit()
cursor_create.close()
conn_create.close()
#关闭数据库连接


#抓取所有seriesid
f_seriesid = codecs.open('D:/seriesid.txt', 'w', 'utf-8')
f_seriesid.write('')
f_seriesid.close()

Char=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

for seriesid in Char:
    response = urllib.request.urlopen('http://www.autohome.com.cn/grade/carhtml/' + seriesid + '.html')
    html = str(response.read(), 'gb2312')

    regex_seriesid = re.compile('"s\d*?"')
    result_seriesid = regex_seriesid.findall(html)

    content_seriesid = ''
    for string in result_seriesid:
        content_seriesid = content_seriesid + string + "\n"

    content_seriesid = content_seriesid.replace('"', '')
    content_seriesid = content_seriesid.replace('s', '')

    f_seriesid = codecs.open('D:/seriesid.txt', 'a', 'utf-8')
    f_seriesid.write(content_seriesid)
    f_seriesid.close()
#抓取完毕，写入文本seriesid中


#个别页面错误跳过，进入下一个页面抓取
n=0
while(n!=20):
    try:
        for n in range(n, 20,1):

            seriesid = linecache.getline('d:/seriesid.txt', n)
            seriesid = seriesid.replace('\n', '')

            response = urllib.request.urlopen('http://car.autohome.com.cn/config/series/' + seriesid + '.html')
            html = str(response.read(), 'gb2312')

            regex_specid = re.compile('specsList.*?]')
            result_specid = regex_specid.findall(html)

            if (len(result_specid) > 0):
                list_specid = re.compile('"specid":\d*')

                list_specid = list_specid.findall(result_specid[0])

                i = 0
                content_specid = ''
                for string in list_specid:
                    content_specid = content_specid + string + "\n"
                    i += 1

                content_specid = content_specid.replace('"specid":', '')
                f_specid = codecs.open('D:/specid.txt', 'w', 'utf-8')
                f_specid.write(content_specid)
                f_specid.close()

                f_everyseriesid=codecs.open('D:/everyseriesid.txt', 'w', 'utf-8')
                f_everyseriesid.write('')
                f_everyseriesid.close()
                linecache.updatecache('d:/everyseriesid.txt')

                num=0
                for num in range(0,i,1):
                    f_everyseriesid = codecs.open('D:/everyseriesid.txt', 'a', 'utf-8')
                    f_everyseriesid.write(seriesid+'\n')
                    f_everyseriesid.close()


                linecache.updatecache('d:/everyseriesid.txt')
                linecache.updatecache('d:/specid.txt')

                conn_insert = pymysql.Connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='123456',
                    db='qichezhijia',
                    charset='gb2312'
                )

                cursor_insert = conn_insert.cursor()

                j = 0
                content_insert = ''
                for j in range(1, i+1, 1):
                    a1 = linecache.getline('d:/everyseriesid.txt', j)
                    a1 = a1.replace('\n','')
                    a2 = linecache.getline('d:/specid.txt', j)
                    a2 = a2.replace('\n', '')
                    sql_insert = "insert into iddata(seriesid,specid) VALUES (\'%s\',\'%s\')" % (a1, a2)
                    cursor_insert.execute(sql_insert)

                conn_insert.commit()
                cursor_insert.close()
                conn_insert.close()
            else:
                continue
    except:
        print(seriesid)
        f_seriesid_error = codecs.open('D:/seriesid_error.txt', 'a', 'utf-8')
        f_seriesid_error.write(seriesid)
        f_seriesid_error.close()

    n+=1
    time.sleep(1)

# seriesid     specid
# 2097         24355
# 923          26247
# 923          26255
# 923          25153
# 385          25156
# 385          27315
# 385          25157