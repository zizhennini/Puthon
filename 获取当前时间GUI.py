import tkinter as tk
import time

def gettime():
    var.set(time.strftime("%H:%M:%S"))  # 获取当前时间
    root.after(1000,gettime)            # 每隔1秒调用 gettime 自身获取时间

root = tk.Tk()
root.title('时钟')
var = tk.StringVar()

lb = tk.Label(root,textvariable=var,fg="blue",font=("黑体",80))
lb.pack()
gettime()
root.mainloop()