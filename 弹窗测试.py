# import tkinter as tk
# import random
# import threading
# import time
#
# # 生成渐变颜色的函数，这里实现从红色到蓝色的简单线性渐变，你可以调整起始和结束颜色以及计算逻辑来实现不同效果
# def generate_gradient_color():
#     r_start, g_start, b_start = 255, 0, 0  # 起始颜色红色（RGB值）
#     r_end, g_end, b_end = 0, 0, 255  # 结束颜色蓝色（RGB值）
#     # 随机生成一个比例，用于混合起始颜色和结束颜色，实现渐变效果
#     ratio = random.random()
#     r = int(r_start * (1 - ratio) + r_end * ratio)
#     g = int(g_start * (1 - ratio) + g_end * ratio)
#     b = int(b_start * (1 - ratio) + b_end * ratio)
#     return f"#{r:02X}{g:02X}{b:02X}"
#
# def create_window(text):
#     window = tk.Tk()
#     window.title('你是憨憨')
#     screen_width = window.winfo_screenwidth()
#     screen_height = window.winfo_screenheight()
#     width, height = 200, 50
#     x = random.randrange(0, screen_width - width)
#     y = random.randrange(0, screen_height - height)
#     window.geometry(f"{width}x{height}+{x}+{y}")
#     # 调用生成渐变颜色的函数来设置标签背景色
#     tk.Label(window,
#              text=text,
#              bg=generate_gradient_color(),
#              font=('楷体', 17),
#              width=20, height=2
#              ).pack()
#     return window
#
# def countdown(window, time_remaining):
#     if time_remaining == -1:
#         window.destroy()
#     else:
#         window.after(1000, countdown, window, time_remaining - 1)
#
# def display_window(text):
#     window = create_window(text)
#     countdown(window, 50)
#     window.mainloop()
#
# texts = ["新年好", "这是第一句额外的话", "这是第二句额外的话", "这是第三句额外的话", "这是第四句额外的话",
#          "这是第五句额外的话", "这是第六句额外的话", "这是第七句额外的话", "这是第八句额外的话", "这是第九句额外的话",
#          "这是第十句额外的话", "这是第十一句额外的话"]
#
# # 初始延迟时间，单位为秒
# initial_delay = 0.1
# # 衰减因子，控制指数衰减的速度，可根据需要调整
# decay_factor = 0.9
# # 最小延迟时间，单位为秒，避免延迟过小导致问题
# min_delay = 0.001
# # 用于记录已经创建的窗口数量
# window_count = 0
# while True:
#     for text in texts:
#         thread = threading.Thread(target=display_window, args=(text,))
#         thread.start()
#         # 根据指数函数计算当前延迟时间，使其按指数形式递减
#         current_delay = max(initial_delay * (decay_factor ** window_count), min_delay)
#         time.sleep(current_delay)
#     window_count += len(texts)


import tkinter as tk
import random
import threading
import time

# 假设这是从图片中提取的颜色编码列表
color_codes = [
    "#ff99ff", "#cc99ff", "#66cccc", "#ffff00", "#ff00ff", "#00ffff",
    "#99ff00", "#008000", "#000080", "#808000", "#800080", "#008080",
    "#c0c0c0", "#808080", "#ffffff", "#99ffcc"
]

def create_window(text):
    window = tk.Tk()
    window.title('你是憨憨')
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width, height = 200, 50
    x = random.randrange(0, screen_width - width)
    y = random.randrange(0, screen_height - height)
    window.geometry(f"{width}x{height}+{x}+{y}")
    # 从颜色编码列表中随机选择一个颜色
    bg_color = random.choice(color_codes)
    tk.Label(window,
             text=text,
             bg=bg_color,
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

texts = ["新年好", "新年好", "新年好", "陈燕桢新年好", "祝意深深情谊绵绵",
        "朋心共进学海扬鞭", "友伴同行勇攀峰巅", "学途璀璨梦想高悬", "习练真知不畏辛艰", "考绩斐然名榜留传",
        "试剑考场笑傲无前", "顺意逐光岁岁欢颜"]

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