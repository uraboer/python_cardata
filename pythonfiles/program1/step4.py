# 两个文件逐行读取,插入数据库中
#coding:utf-8
import codecs
import linecache

f = codecs.open('D:/demo.txt', 'a', 'utf-8')
f.write('')
f.close()

f1 = codecs.open("d:/category.txt","r","utf-8")
f2 = codecs.open("d:/value.txt","r","utf-8")


import pymysql

conn=pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='qichezhijia',
    charset='gb2312'
)

cursor = conn.cursor()

n=0
content=''
for n in range(1,186):
    a1=linecache.getline('d:/category.txt',n)
    a2 = linecache.getline('d:/value.txt', n)
    ######################################################################
    sql = "insert into mycar1(id,name) VALUES (\'%s\',\'%s\')" %(a1,a2)  #不加\会报语法错误1064，原因不明
    ######################################################################
    cursor.execute(sql)
    n+=1

conn.commit()
cursor.close()
conn.close()
