import tkinter as tk
from tkinter import messagebox

from django.template.defaultfilters import title

Tk = tk.Tk()
login_window = title("北京科技大学天津学院学习管理平台")
fun = Tk.maxsize()
Tk.geometry('600x500')
#Tk.configure(bg="blue")
#Tk.attributes('-alpha',0.5)
def guan():
    print('你已退出学习')
#Tk.protocol('WM_DELETE_WINDOW',guan())
#Tk.destroy()
s1=tk.StringVar()
#s2=set('')
#textvariable=s1
b = tk.Label(Tk,text='学号',font=("黑体",16),fg='red')
tk.Entry(Tk,width=20,font=('黑体',26)).place(x=100,y=150)


Tk.mainloop()