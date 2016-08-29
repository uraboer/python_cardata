# coding:utf-8
import codecs
import urllib.request
import linecache
import re
import pymysql
import time

#demo11###########################
conn_create=pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='qichezhijia',
    charset='gb2312'
)

cursor_create = conn_create.cursor()


sql_create = "CREATE TABLE cardata(specid VARCHAR(20),category VARCHAR(50), carvalue VARCHAR(50))ENGINE=INNODB"


cursor_create.execute(sql_create)


conn_create.commit()
cursor_create.close()
conn_create.close()
############################


#demo12###########################
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
    f_seriesid.flush()
    f_seriesid.close()

n=0
for n in range(1,21):

    linecache.updatecache('d:/specid_everycar.txt')
    linecache.updatecache('d:/category.txt')
    linecache.updatecache('d:/value.txt')
    linecache.updatecache('d:/linesnum.txt')
    linecache.updatecache('d:/specidnum.txt')
    linecache.updatecache('d:/specid.txt')


    seriesid=linecache.getline('d:/seriesid.txt',n)
    seriesid=seriesid.replace('\n','')
    #demo13###########################
    response = urllib.request.urlopen('http://car.autohome.com.cn/config/series/'+seriesid+'.html')
    html = str(response.read(), 'gb2312')

    f_specid = codecs.open('D:/specid.txt', 'w', 'utf-8')
    f_specid.write('')
    f_specid.flush()
    f_specid.close()
    f_specidnum = codecs.open('D:/specidnum.txt', 'w', 'utf-8')
    f_specidnum.write('')
    f_specidnum.flush()
    f_specidnum.close()

    regex_specid = re.compile('specsList.*?]')
    result_specid = regex_specid.findall(html)

    if (len(result_specid) > 0):
        list_specid = re.compile('"specid":\d*')

        list_specid = list_specid.findall(result_specid[0])  # 总共有3条匹配的，取出一条提取specid

        i = 0
        content_specid = ''
        for string in list_specid:
            content_specid = content_specid + string + "\n"
            i += 1  # 统计每款车specid个数

        content_specid = content_specid.replace('"specid":', '')
        f_specid = codecs.open('D:/specid.txt', 'w', 'utf-8')
        f_specid.write(content_specid)
        f_specid.flush()
        f_specid.close()
        f_specidnum = codecs.open('D:/specidnum.txt', 'w', 'utf-8')
        f_specidnum.write(str(i))
        f_specidnum.flush()
        f_specidnum.close()

        # demo7###########################
        specidnum = linecache.getline('d:/specidnum.txt', 1)
        specidnum=int(specidnum)

        x = 0
        for x in range(1, specidnum+1):
            regex_category = re.compile('{"name":".*?","valueitems"')
            result_category = regex_category.findall(html)

            content_category = ''
            linesnum = 1
            for string in result_category:
                content_category = content_category + string + "\n"
                linesnum = linesnum + 1

            content_category = re.sub('{"name":".*?","configitems":\[', '', content_category)
            content_category = re.sub('{"name":".*?","paramitems":\[', '', content_category)
            content_category = content_category.replace('{"name":', '')
            content_category = content_category.replace(',"valueitems"', '')
            content_category = content_category.replace('"', '')

            f_category = codecs.open('D:/category.txt', 'w', 'utf-8')
            f_category.write(content_category)
            f_category.flush()
            f_category.close()

            f_linesnum = codecs.open('D:/linesnum.txt', 'w', 'utf-8')
            f_linesnum.write(str(linesnum))
            f_linesnum.flush()
            f_linesnum.close()
        ############################


        # demo8###########################
            specid = linecache.getline('d:/specid.txt', x)
            specid = specid.replace('\n', '')

            regex_value = re.compile('{"specid":' + specid + ',"value":".*?"')
            result_value = regex_value.findall(html)

            content_value_all = ''
            for string in result_value:
                content_value_all = content_value_all + string + "\n"

            content_value = content_value_all.replace('{"specid":' + specid + ',"value":', '')

            content_value = content_value.replace('"', '')

            f_value = codecs.open('D:/value.txt', 'w', 'utf-8')
            f_value.write(content_value)
            f_value.flush()
            f_value.close()

            content_specid_everycar = content_value_all.replace('{"specid":', '')
            content_specid_everycar = re.sub(',"value":".*', '', content_specid_everycar)

            f_specid_everycar = codecs.open('D:/specid_everycar.txt', 'w', 'utf-8')
            f_specid_everycar.write(content_specid_everycar)
            f_specid_everycar.flush()
            f_specid_everycar.close()

            ############################


            # demo10###########################
            conn_insert = pymysql.Connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='123456',
                db='qichezhijia',
                charset='gb2312'
            )

            cursor_insert = conn_insert.cursor()

            n = 0
            content_insert = ''
            linusnum = linecache.getline('d:/linesnum.txt', 1)
            linesnum = int(linusnum)

            linecache.updatecache('d:/specid_everycar.txt')
            linecache.updatecache('d:/category.txt')
            linecache.updatecache('d:/value.txt')

            for n in range(1, linesnum):
                a1 = linecache.getline('d:/specid_everycar.txt', n)
                a2 = linecache.getline('d:/category.txt', n)
                a3 = linecache.getline('d:/value.txt', n)
                sql_insert = "insert into cardata(specid,category,carvalue) VALUES (\'%s\',\'%s\',\'%s\')" % (a1, a2, a3)
                cursor_insert.execute(sql_insert)
                n += 1
                conn_insert.commit()

            cursor_insert.close()
            conn_insert.close()

            x += 1
    else:
        content_specid_everycar=''
        f_specid_everycar = codecs.open('D:/specid_everycar.txt', 'w', 'utf-8')
        f_specid_everycar.write(content_specid_everycar)
        f_specid_everycar.flush()
        f_specid_everycar.close()
        content_specid=''
        f_specid = codecs.open('D:/specid.txt', 'w', 'utf-8')
        f_specid.write(content_specid)
        f_specid.flush()
        f_specid.close()
        content_category=''
        f_category = codecs.open('D:/category.txt', 'w', 'utf-8')
        f_category.write(content_category)
        f_category.flush()
        f_category.close()
        linesnum=''
        f_linesnum = codecs.open('D:/linesnum.txt', 'w', 'utf-8')
        f_linesnum.write(linesnum)
        f_linesnum.flush()
        f_linesnum.close()
        specidnum=''
        f_specidnum= codecs.open('D:/specidnum.txt', 'w', 'utf-8')
        f_specidnum.write(specidnum)
        f_specidnum.flush()
        f_specidnum.close()
        value=''
        f_value= codecs.open('D:/value.txt', 'w', 'utf-8')
        f_value.write(specidnum)
        f_value.flush()
        f_value.close()



    ###########################

    time.sleep(3)
    ############################

    n+=1
