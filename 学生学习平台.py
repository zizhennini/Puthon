import tkinter as tk
from tkinter import messagebox

# 创建登录界面的函数
def create_login_window():
    # 创建主窗口
    login_window = tk.Tk()
    login_window.title("学生学习平台登录")
    login_window.geometry("400x200")

    # 创建并放置标签和文本框
    tk.Label(login_window, text="学号:").grid(row=0, column=0, padx=10, pady=10)
    student_id_var = tk.StringVar()
    tk.Entry(login_window, textvariable=student_id_var).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="姓名:").grid(row=1, column=0, padx=10, pady=10)
    name_var = tk.StringVar()
    tk.Entry(login_window, textvariable=name_var).grid(row=1, column=1, padx=10, pady=10)

    tk.Label(login_window, text="学习科目:").grid(row=2, column=0, padx=10, pady=10)
    subject_var = tk.StringVar()
    tk.Entry(login_window, textvariable=subject_var).grid(row=2, column=1, padx=10, pady=10)

    # 定义登录按钮的点击事件处理函数
    def login():
        student_id = student_id_var.get()
        name = name_var.get()
        subject = subject_var.get()
        # 在这里可以添加验证逻辑，但为了示例简单，直接显示成功登录界面
        if student_id and name and subject:
            create_success_window(name)
            login_window.destroy()  # 关闭登录窗口
        else:
            messagebox.showwarning("输入警告", "请填写所有字段")

    # 定义注册按钮（本例中未实现具体注册逻辑，仅作为示例）
    def register():
        messagebox.showinfo("注册提示", "注册功能尚未实现")

    # 创建并放置登录和注册按钮
    tk.Button(login_window, text="登录", command=login).grid(row=3, column=0, padx=20, pady=20)
    tk.Button(login_window, text="注册", command=register).grid(row=3, column=1, padx=20, pady=20)

    # 运行主循环
    login_window.mainloop()

# 创建成功登录后的界面的函数
def create_success_window(name):
    # 创建新窗口
    success_window = tk.Tk()
    success_window.title("学生学习平台")
    success_window.geometry("300x100")

    # 创建并放置欢迎标签
    tk.Label(success_window, text=f"你已成功登录学生学习平台，{name}，请你开始学习").pack(pady=20)

    # 运行主循环（这里其实可以不需要，因为一旦显示信息后用户可能会关闭窗口）
    success_window.mainloop()

# 运行登录界面函数
create_login_window()