# 隐藏pygame的import欢迎显示
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''
import sys  # 导入系统特定参数和函数
import random  # 导入随机数生成器
import pygame  # 导入pygame库用于游戏开发
from tkinter import Tk, messagebox  # 导入Tkinter库用于创建图形界面
import pyautogui  # 引入pyautogui库用于截屏
from datetime import datetime  # 引入datetime模块处理时间

# 窗口大小(width, height)
SCREENSIZE = (500, 260)

# 定义一些颜色
BLACK = (0, 0, 0)  # 黑色
DARKGRAY = (169, 169, 169)  # 深灰色
GAINSBORO = (230, 230, 230)  # 明亮的灰色
SKYBLUE = (135, 206, 235)  # 天空蓝

# 背景音乐路径
BGM_PATH = os.path.join(os.getcwd(), './music/bg.mp3')  # 设置背景音乐路径
# 字体路径
FONT_PATH = os.path.join(os.getcwd(), './font/STXINGKAI.ttf')  # 设置字体路径
# 背景图片路径
BACKGROUND_PATH = os.path.join(os.getcwd(), './img/bg.jpg')  # 设置背景图片路径
# ICON路径
ICON_IMAGE_PATH = os.path.join(os.getcwd(), './img/heart.jpg')  # 设置图标路径
# biu.jpg路径
BIU_IMAGE_PATH = os.path.join(os.getcwd(), './img/biu.jpg')  # 设置biu图片路径

# 按钮文本列表
button_no_texts = [  # 不同的文本用于“算了吧”按钮
    '你再想想',
    '我会写代码',
    '我会修电脑',
    '我养你',
    '好吃的都给你',
    '保大',
    '房产证给你',
    '我妈会游泳'
]


# 定义按钮类
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, fontpath, fontsize, fontcolor, bgcolors, edgecolor, edgesize=1,
                 is_want_to_be_selected=True, screensize=None):
        super().__init__()  # 调用父类构造函数
        self.rect = pygame.Rect(x, y, width, height)  # 创建按钮矩形
        self.text = text  # 设置按钮文本
        self.font = pygame.font.Font(fontpath, fontsize)  # 加载字体
        self.fontcolor = fontcolor  # 设置字体颜色
        self.bgcolors = bgcolors  # 设置背景颜色
        self.edgecolor = edgecolor  # 设置边框颜色
        self.edgesize = edgesize  # 设置边框大小
        self.is_want_to_be_selected = is_want_to_be_selected  # 是否想被选择
        self.screensize = screensize  # 屏幕大小

    def draw(self, screen):  # 绘制按钮
        pygame.draw.rect(screen, self.bgcolors[1], self.rect, 0)  # 绘制背景
        pygame.draw.rect(screen, self.edgecolor, self.rect, self.edgesize)  # 绘制边框

        text_render = self.font.render(self.text, True, self.fontcolor)  # 渲染文本
        fontsize = self.font.size(self.text)  # 获取字体大小
        screen.blit(text_render, (  # 将文本绘制到按钮中心
            self.rect.x + (self.rect.width - fontsize[0]) / 2, self.rect.y + (self.rect.height - fontsize[1]) / 2))
# 定义移动按钮类
class MovingButton(Button):
    def __init__(self, x, y, width, height, text, fontpath, fontsize, fontcolor, bgcolors, edgecolor, edgesize=1,
                 screensize=None):
        super().__init__(x, y, width, height, text, fontpath, fontsize, fontcolor, bgcolors, edgecolor, edgesize, True,
                         screensize)

    def update(self, mouse_pos):  # 更新按钮位置
        if self.rect.collidepoint(mouse_pos):  # 检查鼠标是否碰撞
            self.text = random.choice(button_no_texts)  # 随机选择文本
            # 随机设置按钮的新位置
            self.rect.left, self.rect.top = random.randint(0, SCREENSIZE[0] - self.rect.width), random.randint(0,
                                                                                                               SCREENSIZE[
                                                                                                                   1] - self.rect.height)


# 显示文本的函数
def showText(screen, text, position, fontpath, fontsize, fontcolor, is_bold=False):
    font = pygame.font.Font(fontpath, fontsize)  # 创建字体对象
    font.set_bold(is_bold)  # 设置字体加粗
    text_render = font.render(text, True, fontcolor)  # 渲染文本
    screen.blit(text_render, position)  # 绘制文本


# 截图函数
def save_screenshot():
    screenshot = pyautogui.screenshot()  # 使用pyautogui截取全屏
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # 获取当前时间并格式化
    screenshot_path = os.path.join(os.getcwd(), f"./img/{current_time}.png")  # 设置保存路径
    screenshot.save(screenshot_path)  # 保存截图


# 主函数
def main():
    # 初始化
    pygame.init()  # 初始化pygame
    screen = pygame.display.set_mode(SCREENSIZE, 0, 32)  # 创建窗口
    pygame.display.set_icon(pygame.image.load(ICON_IMAGE_PATH))  # 设置窗口图标
    pygame.display.set_caption('来自一位喜欢你的小哥哥')  # 设置窗口标题

    # 背景音乐
    pygame.mixer.music.load(BGM_PATH)  # 加载背景音乐
    pygame.mixer.music.play(-1, 30.0)  # 循环播放音乐

    # 加载背景图片
    background_image = pygame.image.load(BACKGROUND_PATH)  # 加载背景图片
    background_image = pygame.transform.scale(background_image, SCREENSIZE)  # 缩放到窗口大小

    # 加载biu.jpg图片
    biu_image = pygame.image.load(BIU_IMAGE_PATH)  # 加载biu图片
    biu_image = pygame.transform.scale(biu_image, (180, 180))  # 适当缩放

    # 实例化按钮
    button_yes = Button(x=35, y=SCREENSIZE[1] - 80, width=120, height=35,
                        text='好呀', fontpath=FONT_PATH, fontsize=15, fontcolor=BLACK, edgecolor=SKYBLUE,
                        edgesize=2, bgcolors=[DARKGRAY, GAINSBORO], screensize=SCREENSIZE)  # 创建“好呀”按钮

    button_no = MovingButton(x=SCREENSIZE[0] - 165, y=SCREENSIZE[1] - 80, width=120, height=35,
                             text='算了吧', fontpath=FONT_PATH, fontsize=15, fontcolor=BLACK,
                             edgecolor=DARKGRAY, edgesize=1, bgcolors=[DARKGRAY, GAINSBORO],
                             screensize=SCREENSIZE)  # 创建“算了吧”移动按钮

    # 是否点击了好呀按钮
    is_agree = False  # 初始化同意标志为False

    # 主循环
    clock = pygame.time.Clock()  # 创建时钟对象
    while True:
        # 背景图像
        screen.blit(background_image, (0, 0))  # 绘制背景图像
        screen.blit(biu_image, (0, 0))  # 在左边绘制biu图片

        # 鼠标事件捕获
        for event in pygame.event.get():  # 获取事件
            if event.type == pygame.QUIT:  # 如果是退出事件
                if is_agree:  # 如果已经点击“好呀”按钮
                    pygame.quit()  # 退出pygame
                    sys.exit()  # 退出系统
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button:  # 如果鼠标按下
                if button_yes.rect.collidepoint(pygame.mouse.get_pos()):  # 如果点击了“好呀”按钮
                    root = Tk()  # 创建Tkinter窗口
                    root.withdraw()  # 隐藏主窗口
                    messagebox.showinfo('', '❤❤❤么么哒❤❤❤')  # 弹出消息框
                    root.destroy()  # 销毁窗口

                    # 截图
                    save_screenshot()  # 调用截图函数
                    is_agree = True  # 设置同意标志为True

        # 更新移动按钮
        button_no.update(pygame.mouse.get_pos())  # 更新移动按钮位置

        # 显示文字
        showText(screen=screen, text='小姐姐, 我观察你很久了', position=(120, 70),
                 fontpath=FONT_PATH, fontsize=25, fontcolor=BLACK, is_bold=False)  # 显示第一行文字
        showText(screen=screen, text='做我女朋友好不好?', position=(140, 120),
                 fontpath=FONT_PATH, fontsize=25, fontcolor=BLACK, is_bold=True)  # 显示第二行文字

        # 显示按钮
        button_yes.draw(screen)  # 绘制“好呀”按钮
        button_no.draw(screen)  # 绘制“算了吧”按钮

        # 刷新
        pygame.display.update()  # 刷新屏幕
        clock.tick(60)  # 控制帧率为60帧每秒


# run
if __name__ == '__main__':
    main()  # 运行主函数

