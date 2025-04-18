# 导入tkinter
import tkinter as tk
# 创建主窗口
root = tk.Tk()
root.title("简单问好")
root.geometry("600x500")

# 创建标签
label = tk.Label(root,text="请输入您的姓名：")
label.pack(pady=30)

# 创建文本框
entry = tk.Entry(root)
entry.pack()

# 创建按钮和事件处理结果程序
def button_clicked():
    user_name = entry.get()  # 获取文本框中的内容
    label.config(text="您好，" + user_name + "!")

button = tk.Button(root,text="点击我",command=button_clicked)
button.pack()

# 停滞界面
root.mainloop()
