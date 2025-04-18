from tkinter import * # 导入tkinter库的所有组件
import random # 导入random库用于生成随机数

count =0# 初始化全局计数器

def race():# 定义开始游戏的函数
    global count  # 使用全局变量count
    count +=1# 每次调用函数时计数器加1
    txt.insert(END,f'第{count}局\n') # 在文本框中插入当前局数

    # 创建一个字典，将数字映射到石头、剪刀、布
    choices = {0:'石头',1:'剪刀',2:'布'}
    people = choices[num.get()] # 获取玩家的选择
    robot = random.choice(list(choices.values())) # 计算机随机选择

    # 在文本框中插入玩家和计算机的选择
    txt.insert(END,f'玩家出:{people}\n')
    txt.insert(END,f'机器人出:{robot}\n')

    # 判断胜负并输出结果
    if people == robot:
        txt.insert(END,'结果:平局\n\n')
    elif(people =='石头'and robot =='布') or \
        (people =='剪刀' and robot =='石头') or\
        (people =='布'and robot =='剪刀'):
        txt.insert(END,'结果:机器人获胜\n\n')
    else:
        txt.insert(END,'结果:玩家获胜\n\n')

    txt.see(END) # 确保文本框滚动到最新内容
    txt.update() # 更新文本框显示

def clean():# 定义清除文本框内容的函数
    txt.delete(1.0, END) # 清除文本框从开始到结束的内容

root = Tk() # 创建Tkinter窗口
root.title('猜丁壳') # 设置窗口标题
root.geometry('400x360+200+300') # 设置窗口大小和位置
root.resizable(False,False) # 禁止调整窗口大小
root.config(bg='#d7d7d5') # 设置窗口背景颜色

# 创建欢迎标签
Label(root, text='欢迎来到猜丁壳小游戏', font=('微软雅黑',15), bg='#d7d7d5').pack()

# 创建选择区域
frame1 = Frame(root, bg='#d7d7d5')
frame1.pack()
num = IntVar()
num.set(0) # 初始化选择变量
Label(frame1, text='请选择:', font=('微软雅黑',15), bg='#d7d7d5').pack(side=LEFT)
Radiobutton(frame1, text='石头', font=('微软雅黑',15), bg='#d7d7d5', value=0, variable=num).pack(side=LEFT)
Radiobutton(frame1, text='剪刀', font=('微软雅黑',15), bg='#d7d7d5', value=1, variable=num).pack(side=RIGHT)
Radiobutton(frame1, text='布', font=('微软雅黑',15), bg='#d7d7d5', value=2, variable=num).pack(side=RIGHT)

# 创建控制按钮区域
frame2 = Frame(root, bg='#d7d7d5')
frame2.pack(pady=5)
begin = Button(frame2, text='开始', font=('微软雅黑',9), command=race)
begin.pack(side=LEFT, padx=5)
Button(frame2, text='清除', font=('微软雅黑',9), command=clean).pack(side=LEFT, padx=5)
Button(frame2, text='退出', font=('微软雅黑',9), command=quit).pack(side=RIGHT, padx=5)

# 创建显示比赛结果的标签
Label(root, text='比赛结果', font=('微软雅黑',15), bg='#cefdfc').pack()

txt = Text(root, width=50, height=10, font=('微软雅黑',12)) # 创建文本框用于显示结果
txt.pack() # 将文本框添加到窗口

root.mainloop() # 进入Tkinter事件循环

