import tkinter as tk
import random
import threading
import time


def create_window():
    window = tk.Tk()
    window.title('你是憨憨')
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width,height = 200, 50
    x = random.randrange(0,screen_width - width)
    y = random.randrange(0,screen_height - height)
    window.geometry(f"{width}x{height}+{x}+{y}")
    tk.Label(window,
        text='你真是个铁憨憨！',
        bg = random.choice(['Red','blue','yellow','green']),
        font=('楷体',17),
        width=20,height=2
        ).pack()
    return window

def countdown(window,time_remaining):
    if time_remaining == -1:
        window.destroy()
    else:
        window.after(1000,countdown,window,time_remaining - 1)

def display_window():
    window = create_window()
    countdown(window,50)    #设置10秒后窗口自动关闭
    window.mainloop()

threads = []
for i in range(1000):
    thread = threading.Thread(target=display_window)
    threads.append(thread)
    thread.start()
    time.sleep(0.01)     #  稍微延迟启动每个线程，确保窗口不会完全重叠
