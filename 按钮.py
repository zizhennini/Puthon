import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("简单的GUI示例")
root.geometry("300x200")

# 创建一个标签
label = tk.Label(root, text="这是一个简单的GUI示例")
label.pack(pady=10)

# 创建一个文本输入框
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# 定义一个按钮点击事件的处理函数
def on_button_click():
    user_input = entry.get()
    messagebox.showinfo("用户输入", f"你输入了: {user_input}")

# 创建一个按钮
button = tk.Button(root, text="点击我", command=on_button_click)
button.pack(pady=10)

# 运行主循环
root.mainloop()