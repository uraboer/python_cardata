#抓取年款
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


sql_create = "CREATE TABLE YearId(yearid VARCHAR(50) ,series VARCHAR(50))ENGINE=INNODB"


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
while(n!=2060):
    try:
        for n in range(n, 2060,1):

            seriesid = linecache.getline('d:/seriesid.txt', n)
            seriesid = seriesid.replace('\n', '')

            response = urllib.request.urlopen('http://car.autohome.com.cn/config/series/'+seriesid+'.html')
            html = str(response.read(), 'gb2312')

            regex_yearid = re.compile('<a target="_self" href="/config/series/.*-.*')
            result_yearid = regex_yearid.findall(html)

            if (len(result_yearid) > 0):

                i = 0
                content_yearid = ''
                for string in result_yearid:
                    content_yearid = content_yearid + string + "\n"
                    i += 1

                content_yearid = content_yearid.replace('<a target="_self" href="/config/series/','')
                content_yearid=content_yearid.replace('.html">','')

                f_specid = codecs.open('D:/yearid.txt', 'w', 'utf-8')
                f_specid.write(content_yearid)
                f_specid.close()

                regex_specid = re.compile('<span class="year-text">.*?款')
                result_series = regex_specid.findall(html)


                content_series = ''
                for string in result_series:
                    content_series = content_series + string + "\n"

                content_series = content_series.replace('<span class="year-text">', '')
                content_series = content_series.replace('款', '')

                f_specid = codecs.open('D:/series.txt', 'w', 'utf-8')
                f_specid.write(content_series)
                f_specid.close()


                linecache.updatecache('d:/yearid.txt')
                linecache.updatecache('d:/series.txt')

                conn_insert = pymysql.Connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='123456',
                    db='qichezhijia',
                    charset='gb2312'
                )

                cursor_insert = conn_insert.cursor()

                j=0
                for j in range (1,i+1,1):
                    a1 = linecache.getline('d:/yearid.txt', j)
                    a1 = a1.replace('\n','')
                    a2 = linecache.getline('d:/series.txt', j)
                    a2 = a2.replace('\n', '')
                    sql_insert = "insert into YearId(yearid,series) VALUES (\'%s\',\'%s\')" % (a1,a2)
                    cursor_insert.execute(sql_insert)

                conn_insert.commit()
                cursor_insert.close()
                conn_insert.close()
            else:
                continue
    except:
        print(seriesid)
        f_seriesid_error = codecs.open('D:/seriesid_error.txt', 'a', 'utf-8')
        f_seriesid_error.write(seriesid+'\n')
        f_seriesid_error.close()

    n+=1
    time.sleep(1)
