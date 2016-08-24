#创建表格，字段名为参数，specid...
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


sql = "CREATE TABLE mycar(category VARCHAR(10),specid_25822 VARCHAR(20),specid_25823 VARCHAR(20),specid_25824 VARCHAR(20),specid_25825 VARCHAR(20),specid_25826 VARCHAR(20),specid_25827 VARCHAR(20),specid_25828 VARCHAR(20),specid_25829 VARCHAR(20),specid_25830 VARCHAR(20),specid_24325 VARCHAR(20))ENGINE=INNODB"
cursor.execute(sql)


conn.commit()
cursor.close()
conn.close()