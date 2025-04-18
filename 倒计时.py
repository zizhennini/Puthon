import datetime
import sys
import time
import math
spring = datetime.datetime(2024, 12, 14, 14, 16, 0)  # 新的一年的日期
while True:
    today = datetime.datetime.now()  # 获取当前的日期
    day = (spring - today).days  # 新年日期减去当前日期
    second = (spring - today).seconds  #得到秒数
    sec = second % 60
    minute = second / 60 % 60
    hour = second / 60 / 60
    if hour > 24:
        hour = hour - 24

    hour = math.floor(hour)  # 去掉小数点，向下取整
    minute = math.floor(minute)  # 去掉小数点，向下取整

    sys.stdout.write("离今年春节还有" + str(day) + "天" + str(hour) + "小时" + str(minute) + "分钟" + str(sec) + "秒" + '\r')
    sys.stdout.flush()
    time.sleep(1)
    print("离今年春节还有" + str(day) + "天" + str(hour) + "小时" + str(minute) + "分钟" + str(sec) + "秒" + '\r')