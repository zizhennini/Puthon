import time

def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    while total_seconds > 0:
    # 将总秒数转换为时间格式（小时:分钟:秒）
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)
        time_format = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

        # 清除上一行的输出，并打印新的时间
        print(time_format, end='\r')
        time.sleep(1)
        total_seconds -= 1

    print("时间到！")

# 用户输入时间
hours = int(input("输入小时："))
minutes = int(input("输入分钟："))
seconds = int(input("输入秒数："))

countdown(hours, minutes, seconds)