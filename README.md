# python_cardata

要求：
  从汽车之家网站上抓取汽车配置信息，存入结构化数据库中
  使用mysql-essential-6.0.11-alpha-winx64.msi
  
  SQLyog-12.2.5-0.x86Trial.exe 查看表
  
  Project Interpreter: python 3.5.2
  Package: PyMySQL\pypyodbc\setuptools\pip
  
Note：
1.http://car.autohome.com.cn/config/series/4034.html
  "抱歉，暂无相关数据。"
  seriesid有值，而specid没值,也可以正常运行（specid=''）

2.个别seriesid的页面报解码错误，无法解决，也只有6个而已，故让其打印错误seriesid并跳过错误，继续抓取下一个页面

error seriesid	

3170

2951

3103

3457

86

3736
