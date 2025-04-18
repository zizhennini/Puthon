import tkinter as tk
import random
import threading
import time


def create_window(message):
    window = tk.Tk()
    window.title('消息窗口')  # 可以保持不变，或者根据需要动态设置
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width, height = 200, 50
    x = random.randrange(0, screen_width - width)
    y = random.randrange(0, screen_height - height)
    window.geometry(f"{width}x{height}+{x}+{y}")

    # 根据传入的消息创建标签
    tk.Label(window,
             text=message,
             bg=random.choice(['Red', 'blue', 'yellow', 'green']),
             font=('楷体', 17),
             width=20, height=2).pack()

    return window


def countdown(window, time_remaining):
    if time_remaining == -1:
        window.destroy()
    else:
        window.after(1000, countdown, window, time_remaining - 1)


def display_windows(messages):
    for message in messages:
        window = create_window(message)
        countdown(window, 50)  # 设置10秒后窗口自动关闭
        window.mainloop()
        time.sleep(1)  # 等待一段时间再显示下一条消息，避免窗口重叠


# 指定的11条消息
specified_messages = [
    '第一条消息',
    '第二条消息',
    '第三条消息',
    '第四条消息',
    '第五条消息',
    '第六条消息',
    '第七条消息',
    '第八条消息',
    '第九条消息',
    '第十条消息',
    '第十一条消息'
]

# 使用单独的线程显示每条消息，这里为了简化，我们不使用1000个线程，而是仅使用一个循环展示消息
display_thread = threading.Thread(target=display_windows, args=(specified_messages,))
display_thread.start()
