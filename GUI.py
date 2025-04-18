import tkinter as tk
from tkinter import messagebox

# 学号设置为"24515099"
CORRECT_STUDENT_ID = "245115099"

# 创建登录界面的函数
def create_login_window():
    # 初始化登录窗口
    login_window = tk.Tk()
    login_window.title("学生学习平台登录")
    login_window.geometry("400x250")

    # 创建并放置文本框和标签
    tk.Label(login_window, text="学号:").grid(row=0, column=0, padx=10, pady=10)
    student_id_var = tk.StringVar()
    tk.Entry(login_window, textvariable=student_id_var).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="姓名:").grid(row=1, column=0, padx=10, pady=10)
    name_var = tk.StringVar()
    tk.Entry(login_window, textvariable=name_var).grid(row=1, column=1, padx=10, pady=10)

    tk.Label(login_window, text="学习科目:").grid(row=2, column=0, padx=10, pady=10)
    subject_var = tk.StringVar()
    tk.Entry(login_window, textvariable=subject_var).grid(row=2, column=1, padx=10, pady=10)

    # 定义注册按钮的点击
    def register():
        student_id = student_id_var.get()
        if not student_id.isdigit() or len(student_id) != 4:
            messagebox.showwarning("注册警告", "学号不对请重新输入")
        else:

            messagebox.showinfo("注册提示", "注册成功！请登录。")

    # 定义登录按钮的点击
    def login():
        student_id = student_id_var.get()
        if student_id == CORRECT_STUDENT_ID:
            create_success_window(name_var.get(), subject_var.get())
            login_window.destroy()  # 关闭登录窗口
        else:
            messagebox.showwarning("登录警告", "学号错误，请重新输入")

    # 创建并放置注册和登录按钮
    tk.Button(login_window, text="注册", command=register).grid(row=3, column=0, padx=20, pady=20)
    tk.Button(login_window, text="登录", command=login).grid(row=3, column=1, padx=20, pady=20)

    # 运行登录窗口的主循环
    login_window.mainloop()

# 创建成功登录后的学习界面
def create_success_window(name, subject):
    # 初始化学习窗口
    success_window = tk.Tk()
    success_window.title("学生学习平台")
    success_window.geometry("350x150")

    # 创建并放置欢迎标签
    tk.Label(success_window, text=f"你已成功登录学生学习平台，{name}，{subject}科目，请你开始学习").pack(pady=10)

    # 定义开始学习按钮的点击
    def start_learning():
        messagebox.showinfo("学习提示", "开始学习功能尚未实现")

    # 定义退出学习按钮的点击
    def exit_learning():
        success_window.destroy()  # 关闭学习窗口

    # 创建并放置开始学习和退出学习按钮
    tk.Button(success_window, text="开始学习", command=start_learning).pack(side=tk.LEFT, padx=20, pady=20)
    tk.Button(success_window, text="退出学习", command=exit_learning).pack(side=tk.RIGHT, padx=20, pady=20)

    # 运行学习窗口的主循环
    success_window.mainloop()

# 运行登录界面函数以启动程序
create_login_window()