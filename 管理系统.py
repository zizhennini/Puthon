import tkinter as tk
from tkinter import messagebox


def show_custom_dialog(parent):
    dialog = tk.Toplevel(parent)
    dialog.title("自定义对话框")
    dialog.transient(parent)
    dialog.grab_set()

    label = tk.Label(dialog,text = "请输入你的名字：")
    label.pack(pady= 10)
    entry = tk.Entry(dialog)
    entry.pack(pady = 10)

    def on_ok():
        name = entry.get()
        if name:
            messagebox.showinfo('',f"你好，{name}！")
            dialog.destroy()
        else:
            messagebox.showwarning("警告","请输入名字！")

    def on_cancel():
        dialog.destroy()

    ok_button = tk.Button(dialog,text = "确定",command = on_ok)
    ok_button.pack(side = tk.LEFT,padx = 5,pady = 10)
    cancel_button = tk.Button(dialog,text = "取消",command = on_cancel)
    cancel_button.pack(side = tk.LEFT,padx = 5,pady = 10)

root = tk.Tk()
root.title("主窗口示例")
show_custom_dialog(root)
tk.mainloop()
