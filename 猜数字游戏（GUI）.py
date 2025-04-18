from tkinter import *
import random

number = random.randint(1,100)   #生成大呪等呪1小呪等呪100的呯机呮数

count = 0

def check ():

    global count

    guess=text_guess.get()

    guess=int(guess)

    count +=1

    if guess>number:

        label_result[ "text" ]="大了"

    elif guess < number:

        label_result["text" ]="小了"

    else:

        label_result["text" ]="正确，共猜了"+str(count)+"次"

root = Tk(className='猜数字游戏')

root.minsize(350, 260)

Label(root,text= "猜一个 1——100 之间的数字" ).place(x=90, y=20)

label_guess= Label(root, text= "这个数字是：" )

label_guess.place(x=20, y=80)

text_guess= Entry(root, width=10)

text_guess.place(x=100,y=80)

btnCheck= Button(root, text= '猜', command=check)

btnCheck.place(x=200, y=80, width=45, height=28)

label_result=Label(root, text="")

label_result.place(x=120, y=120)

root.mainloop()
