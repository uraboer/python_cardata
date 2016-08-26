#python 3.5
#取出A-Z分类下所有seriesid号(拼接url使用,共2059个)
import codecs
import urllib.request

f = codecs.open('D:/seriesid.txt', 'w', 'utf-8')
f.write('')
f.close()

Char=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
###########################
#seriesid='A'             #
###########################

for seriesid in Char:
    response = urllib.request.urlopen('http://www.autohome.com.cn/grade/carhtml/' + seriesid + '.html')
    html = str(response.read(), 'gb2312')

    import re

    regex = re.compile('"s\d*?"')
    result = regex.findall(html)

    content = ''
    for string in result:
        content = content + string + "\n"

    content = content.replace('"', '')
    content = content.replace('s', '')

    f = codecs.open('D:/seriesid.txt', 'a', 'utf-8') #'a'追加
    f.write(content)
    f.close()



# 2097
# 2148
# 2098
# 4034
# 4106
# 715
# 1021
# 3825
# 2288
# 2715