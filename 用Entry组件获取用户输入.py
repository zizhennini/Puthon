import tkinter as tk


def print_entry():
    print(entry.get())


root = tk.Tk()

entry = tk.Entry(root)

entry.pack()

button = tk.Button(root, text="打印输入",command = print_entry)

button.pack()

root.mainloop()

