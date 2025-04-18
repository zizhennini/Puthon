import tkinter as tk
import random
import threading
import time

def create_window(text):
    window = tk.Tk()
    window.title('你是憨憨')
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width, height = 200, 50
    x = random.randrange(0, screen_width - width)
    y = random.randrange(0, screen_height - height)
    window.geometry(f"{width}x{height}+{x}+{y}")
    tk.Label(window,
             text=text,
             bg=random.choice(['Red', 'blue', 'yellow', 'green']),
             font=('楷体', 17),
             width=20, height=2
             ).pack()
    return window

def countdown(window, time_remaining):
    if time_remaining == -1:
        window.destroy()
    else:
        window.after(1000, countdown, window, time_remaining - 1)

def display_window(text):
    window = create_window(text)
    countdown(window, 50)
    window.mainloop()

texts = ["新年好", "这是第一句额外的话", "这是第二句额外的话", "这是第三句额外的话", "这是第四句额外的话",
         "这是第五句额外的话", "这是第六句额外的话", "这是第七句额外的话", "这是第八句额外的话", "这是第九句额外的话",
         "这是第十句额外的话", "这是第十一句额外的话"]

# 初始延迟时间，单位为秒
initial_delay = 0.1
# 衰减因子，控制指数衰减的速度，可根据需要调整
decay_factor = 0.9
# 最小延迟时间，单位为秒，避免延迟过小导致问题
min_delay = 0.001
# 用于记录已经创建的窗口数量
window_count = 0
while True:
    for text in texts:
        thread = threading.Thread(target=display_window, args=(text,))
        thread.start()
        # 根据指数函数计算当前延迟时间，使其按指数形式递减
        current_delay = max(initial_delay * (decay_factor ** window_count), min_delay)
        time.sleep(current_delay)
    window_count += len(texts)