#两个txt文件中逐行读取
import codecs
import linecache

f1 = codecs.open("d:/category.txt","r","utf-8")
f2 = codecs.open("d:/value.txt","r","utf-8")

i=0
content=''
for i in range(1,187):
    a1=linecache.getline('d:/category.txt',i)
    a2=linecache.getline('d:/value.txt',i)
    i=i+1
    content=a1+a2
    print(content)

# line1=f1.readline()
# line2=f2.readline()

# while line1:
#     while line2:
#         content=line1+line2
#         print(content)

# f=codecs.open('D:/demo.txt','w','utf-8')
# f.write(content)
# f.close()


# "车型名称"
# "博越 2016款 1.8TD 手动智享型"
# 
# "厂商指导价(元)"
# "10.68万"
# 
# "厂商"
# "吉利汽车"
# 
# "级别"
# "紧凑型SUV"
# 
# "发动机"
# "1.8T 163马力 L4"
# 
# "变速箱"
# "6挡手动"
# 
# "长*宽*高(mm)"
# "4519*1831*1694"
# 
# "车身结构"
# "5门5座SUV"
# 
# "最高车速(km/h)"
# "195"
# 
# "官方0-100km/h加速(s)"
# "-"
# 
# "实测0-100km/h加速(s)"
# "-"
# 
# "实测100-0km/h制动(m)"
# "-"
# 
# "实测油耗(L/100km)"
# "-"
# 
# "工信部综合油耗(L/100km)"
# "7"
# 
# "实测离地间隙(mm)"
# "-"
# 
# "整车质保"
# "四年或10万公里"
# 
# "长度(mm)"
# "4519"
# 
# "宽度(mm)"
# "1831"
# 
# "高度(mm)"
# "1694"
# 
# "轴距(mm)"
# "2670"
# 
# "前轮距(mm)"
# "-"
# 
# "后轮距(mm)"
# "-"
# 
# "最小离地间隙(mm)"
# "-"
# 
# "整备质量(kg)"
# "1610"
# 
# "车身结构"
# "SUV"
# 
# "车门数(个)"
# "5"
# 
# "座位数(个)"
# "5"
# 
# "油箱容积(L)"
# "60"
# 
# "行李厢容积(L)"
# "-"
# 
# "发动机型号"
# "JLE-4G18TD"
# 
# "排量(mL)"
# "1799"
# 
# "排量(L)"
# "1.8"
# 
# "进气形式"
# "涡轮增压"
# 
# "气缸排列形式"
# "L"
# 
# "气缸数(个)"
# "4"
# 
# "每缸气门数(个)"
# "4"
# 
# "压缩比"
# "-"
# 
# "配气机构"
# "DOHC"
# 
# "缸径(mm)"
# "-"
# 
# "行程(mm)"
# "-"
# 
# "最大马力(Ps)"
# "163"
# 
# "最大功率(kW)"
# "120"
# 
# "最大功率转速(rpm)"
# "5500"
# 
# "最大扭矩(N・m)"
# "250"
# 
# "最大扭矩转速(rpm)"
# "1500-4500"
# 
# "发动机特有技术"
# "-"
# 
# "燃料形式"
# "汽油"
# 
# "燃油标号"
# "93号(京92号)"
# 
# "供油方式"
# "直喷"
# 
# "缸盖材料"
# "铝"
# 
# "缸体材料"
# "铁"
# 
# "环保标准"
# "国V"
# 
# "简称"
# "6挡手动"
# 
# "挡位个数"
# "6"
# 
# "变速箱类型"
# "手动变速箱(MT)"
# 
# "驱动方式"
# "前置前驱"
# 
# "四驱形式"
# "-"
# 
# "中央差速器结构"
# "-"
# 
# "前悬架类型"
# "麦弗逊式独立悬架"
# 
# "后悬架类型"
# "多连杆独立悬架"
# 
# "助力类型"
# "电动助力"
# 
# "车体结构"
# "承载式"
# 
# "前制动器类型"
# "通风盘式"
# 
# "后制动器类型"
# "盘式"
# 
# "驻车制动类型"
# "电子驻车"
# 
# "前轮胎规格"
# "225/60 R18"
# 
# "后轮胎规格"
# "225/60 R18"
# 
# "备胎规格"
# "非全尺寸"
# 
# "主/副驾驶座安全气囊"
# "主●&nbsp;/&nbsp;副●"
# 
# "前/后排侧气囊"
# "-"
# 
# "前/后排头部气囊(气帘)"
# "-"
# 
# "膝部气囊"
# "-"
# 
# "胎压监测装置"
# "-"
# 
# "零胎压继续行驶"
# "-"
# 
# "安全带未系提示"
# "●"
# 
# "ISOFIX儿童座椅接口"
# "●"
# 
# "发动机电子防盗"
# "●"
# 
# "车内中控锁"
# "●"
# 
# "遥控钥匙"
# "●"
# 
# "无钥匙启动系统"
# "●"
# 
# "无钥匙进入系统"
# "-"
# 
# "ABS防抱死"
# "●"
# 
# "制动力分配(EBD/CBC等)"
# "●"
# 
# "刹车辅助(EBA/BAS/BA等)"
# "●"
# 
# "牵引力控制(ASR/TCS/TRC等)"
# "●"
# 
# "车身稳定控制(ESC/ESP/DSC等)"
# "●"
# 
# "上坡辅助"
# "●"
# 
# "自动驻车"
# "●"
# 
# "陡坡缓降"
# "●"
# 
# "可变悬架"
# "-"
# 
# "空气悬架"
# "-"
# 
# "可变转向比"
# "-"
# 
# "前桥限滑差速器/差速锁"
# "-"
# 
# "中央差速器锁止功能"
# "-"
# 
# "后桥限滑差速器/差速锁"
# "-"
# 
# "电动天窗"
# "-"
# 
# "全景天窗"
# "-"
# 
# "运动外观套件"
# "-"
# 
# "铝合金轮圈"
# "●"
# 
# "电动吸合门"
# "-"
# 
# "侧滑门"
# "-"
# 
# "电动后备厢"
# "-"
# 
# "感应后备厢"
# "-"
# 
# "车顶行李架"
# "●"
# 
# "真皮方向盘"
# "○"
# 
# "方向盘调节"
# "上下+前后调节"
# 
# "方向盘电动调节"
# "-"
# 
# "多功能方向盘"
# "○"
# 
# "方向盘换挡"
# "-"
# 
# "方向盘加热"
# "-"
# 
# "方向盘记忆"
# "-"
# 
# "定速巡航"
# "-"
# 
# "前/后驻车雷达"
# "前-&nbsp;/&nbsp;后●"
# 
# "倒车视频影像"
# "○"
# 
# "行车电脑显示屏"
# "●"
# 
# "全液晶仪表盘"
# "-"
# 
# "HUD抬头数字显示"
# "-"
# 
# "座椅材质"
# "织物"
# 
# "运动风格座椅"
# "-"
# 
# "座椅高低调节"
# "●"
# 
# "腰部支撑调节"
# "-"
# 
# "肩部支撑调节"
# "-"
# 
# "主/副驾驶座电动调节"
# "-"
# 
# "第二排靠背角度调节"
# "-"
# 
# "第二排座椅移动"
# "-"
# 
# "后排座椅电动调节"
# "-"
# 
# "电动座椅记忆"
# "-"
# 
# "前/后排座椅加热"
# "-"
# 
# "前/后排座椅通风"
# "-"
# 
# "前/后排座椅按摩"
# "-"
# 
# "第三排座椅"
# "-"
# 
# "后排座椅放倒方式"
# "比例放倒"
# 
# "前/后中央扶手"
# "前●&nbsp;/&nbsp;后●"
# 
# "后排杯架"
# "●"
# 
# "GPS导航系统"
# "-"
# 
# "定位互动服务"
# "-"
# 
# "中控台彩色大屏"
# "○"
# 
# "蓝牙/车载电话"
# "○"
# 
# "车载电视"
# "-"
# 
# "后排液晶屏"
# "-"
# 
# "220V/230V电源"
# "-"
# 
# "外接音源接口"
# "USB+AUX"
# 
# "CD支持MP3/WMA"
# "-"
# 
# "多媒体系统"
# "-"
# 
# "扬声器品牌"
# "-"
# 
# "扬声器数量"
# "6-7喇叭"
# 
# "近光灯"
# "卤素"
# 
# "远光灯"
# "卤素"
# 
# "日间行车灯"
# "●"
# 
# "自适应远近光"
# "-"
# 
# "自动头灯"
# "●"
# 
# "转向辅助灯"
# "-"
# 
# "转向头灯"
# "-"
# 
# "前雾灯"
# "●"
# 
# "大灯高度可调"
# "●"
# 
# "大灯清洗装置"
# "-"
# 
# "车内氛围灯"
# "-"
# 
# "前/后电动车窗"
# "前●&nbsp;/&nbsp;后●"
# 
# "车窗防夹手功能"
# "-"
# 
# "防紫外线/隔热玻璃"
# "-"
# 
# "后视镜电动调节"
# "●"
# 
# "后视镜加热"
# "●"
# 
# "内/外后视镜自动防眩目"
# "-"
# 
# "后视镜电动折叠"
# "-"
# 
# "后视镜记忆"
# "-"
# 
# "后风挡遮阳帘"
# "-"
# 
# "后排侧遮阳帘"
# "-"
# 
# "后排侧隐私玻璃"
# "-"
# 
# "遮阳板化妆镜"
# "●"
# 
# "后雨刷"
# "●"
# 
# "感应雨刷"
# "-"
# 
# "空调控制方式"
# "自动●"
# 
# "后排独立空调"
# "-"
# 
# "后座出风口"
# "-"
# 
# "温度分区控制"
# "●"
# 
# "车内空气调节/花粉过滤"
# "-"
# 
# "车载冰箱"
# "-"
# 
# "自动泊车入位"
# "-"
# 
# "发动机启停技术"
# "-"
# 
# "并线辅助"
# "-"
# 
# "车道偏离预警系统"
# "-"
# 
# "主动刹车/主动安全系统"
# "-"
# 
# "整体主动转向系统"
# "-"
# 
# "夜视系统"
# "-"
# 
# "中控液晶屏分屏显示"
# "-"
# 
# "自适应巡航"
# "-"