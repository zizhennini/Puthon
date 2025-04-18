from tkinter import *

def reg():              #完成注册按钮事件处理

    global flag

    flag = False        #不存在重复用户名

    username = txt_user.get().strip()

    userpwd = txt_pwd.get().strip()

    with open("userinfo.txt","r") as file:

        all_content_list = file.read().split("\n")  #得到每个用户一个元素的列表

        for  user  in  all_content_list:

            if user !="":

                if user.split("\t")[0] == username:

                    flag = True

                    lbl_message["text"] = "用户名已存在！"

                    return # 将焦点设置回用户名输入框


    if flag == False :  #没找到重复的用户名

        with open("userinfo.txt","a") as file:

            file.write(username+"\t"+userpwd+"\n")

            lbl_message["text"] = "注册成功！"

root = Tk(className="用户注册")

root.geometry("260x150+250+100")

Label(root, text="用户名：").place(x=20,y=30)

txt_user = Entry(root, width="20")

txt_user.place(x=80,y=30)

Label(root, text="密 码：").place(x=20,y=60)

txt_pwd = Entry(root, width="20",show="*")

txt_pwd.place(x=80,y=60)

lbl_message = Label(root, text="", fg="red")

lbl_message.place(x=100,y=90)

btn_reg = Button(root, text="注 册", command=reg).place(x=120,y=120)

root.mainloop()