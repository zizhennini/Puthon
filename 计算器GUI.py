from tkinter import *

root = Tk()
# 165 x 110 代表初始化窗口大小，280，280代表初始化窗口所在位置
root.geometry("165x110+280+280")
root.title("计算器")

entry=Entry(root)
entry.grid(row = 0,column = 0,columnspan = 4,sticky = E + W)
btn1 = Button(root,text="1",width=5,bg="yellow")
btn2 = Button(root,text="2",width=5)
btn3 = Button(root,text="3",width=5)
btn4 = Button(root,text="4",width=5)
btn5 = Button(root,text="5",width=5,bg="green")
btn6 = Button(root,text="6",width=5)
btn7 = Button(root,text="7",width=5)
btn8 = Button(root,text="8",width=5)
btn9 = Button(root,text="9",width=5,bg="red")
btn0 = Button(root,text="0",width=5)
btnp = Button(root,text=".",width=5)
btna = Button(root,text="+",width=5)
btnb = Button(root,text="-",width=5)
btnc = Button(root,text="*",width=5)
btnd = Button(root,text="/",width=5)
btne = Button(root,text="=",width=5)

# grid布局
btn1.grid(row = 1,column= 0)
btn2.grid(row = 1,column= 1)
btn3.grid(row = 1,column= 2)
btna.grid(row = 1,column= 3)
btn4.grid(row = 2,column= 0)
btn5.grid(row = 2,column= 1)
btn6.grid(row = 2,column= 2)
btnb.grid(row = 2,column= 3)
btn7.grid(row = 3,column= 0)
btn8.grid(row = 3,column= 1)
btn9.grid(row = 3,column= 2)
btnc.grid(row = 3,column= 3)
btn0.grid(row = 4,column= 0)
btnp.grid(row = 4,column= 1)
btnd.grid(row = 4,column= 2)
btne.grid(row = 4,column= 3)
root.mainloop()


