import random
from math import sin,cos,pi,log
from tkinter import *

# 画布的宽度和高度常量
CANVAS_WIDTH = 1500
CANVAS_HEIGHT = 1000
CANVAS_CENTER_X = CANVAS_WIDTH / 2
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2
# https://tools.jb51.net/static/colorpicker/  颜色标准表
# 爱心形状的放大比例
IMAGE_ENLARGE = 12
HEART_COLOR = "#FFB5C5"

def heart_function(t,shrink_ratio:float = IMAGE_ENLARGE):
    """
    根据参数 t 生成爱心形状的坐标。

    :param t: 角度参数（以弧度为单位）
    :param shrink_ratio: 爱心形状的缩放因子
    :return: 坐标元组（x，y）
    """
    x = 16 * (sin(t) ** 3)
    y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))

    x = int(x * shrink_ratio + CANVAS_CENTER_X)
    y = int(y * shrink_ratio + CANVAS_CENTER_Y)
    return x,y

def scatter_inside(x,y,beta = 0.15):
    """
    生成一个新坐标，模拟在点(x, y)周围的散布。
    :param x:原始 x 坐标
    :param y:原始 y 坐标
    :param beta: 散布强度
    :return: 新的 (x, y) 坐标元组
    """
    # 计算散布比例
    dx = -beta * log(random.random()) * (x - CANVAS_CENTER_X)
    dy = -beta * log(random.random()) * (y - CANVAS_CENTER_Y)

    return x - dx, y - dy


def shrink(x, y, ratio):
    """
    将坐标向画布中心缩小。

    :param x: 原始 x 坐标
    :param y: 原始 y 坐标
    :param ratio: 缩小因子
    :return: 新的 (x, y) 坐标元组
    """
    distance_squared = (x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2
    force = -1 / (distance_squared ** 0.6)
    dx = ratio * force * (x - CANVAS_CENTER_X)
    dy = ratio * force * (y - CANVAS_CENTER_Y)

    return x - dx, y - dy


def curve(p):
    """
    根据输入参数计算类似正弦的曲线值。

    :param p: 曲线的参数
    :return: 曲线的值
    """
    return 2 * (2 * sin(4 * p)) / (2 * pi)


class Heart:
    """
    表示爱心形状的类，包含用于渲染的各种点。
    """

    def __init__(self, generate_frame=20):
        self._points = set()  # 爱心的点集合
        self._edge_diffusion_points = set()  # 边缘扩散点集合
        self._center_diffusion_points = set()  # 中心扩散点集合
        self.all_points = {}  # 所有帧的点集合
        self.build(2000)  # 生成初始爱心点

        self.random_halo = 1000  # 随机光环
        self.generate_frame = generate_frame  # 帧数

        # 生成动画的每一帧
        for frame in range(generate_frame):
            self.calc(frame)

    def build(self, number):
        """
    生成初始爱心形状及其扩散点。

    :param number: 要生成的爱心形状点的数量
    """
        # 生成爱心形状的点
        for _ in range(number):
            t = random.uniform(0, 2 * pi)
            self._points.add(heart_function(t))

        # 生成边缘扩散点
        for _x, _y in self._points:
            for _ in range(3):
                self._edge_diffusion_points.add(scatter_inside(_x, _y, 0.05))

            # 生成中心扩散点
        point_list = list(self._points)
        for _ in range(4000):
            x, y = random.choice(point_list)
            self._center_diffusion_points.add(scatter_inside(x, y, 0.17))

    @staticmethod
    def calc_position(x, y, ratio):
        """
        根据比例计算点的新位置。

        :param x: 原始 x 坐标
        :param y: 原始 y 坐标
        :param ratio: 缩放比例
        :return: 新的 (x, y) 坐标元组
        """
        distance_squared = (x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2
        force = 1 / (distance_squared ** 0.520)

        dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)
        dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)

        return x - dx, y - dy

    def calc(self, generate_frame):
        """
        计算特定帧的点以用于动画。

        :param generate_frame: 当前帧数
        """
        ratio = 10 * curve(generate_frame / 10 * pi)

        halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))

        all_points = []  # 存储当前帧的所有点
        heart_halo_point = set()  # 存储光环点

        # 生成光环点
        for _ in range(halo_number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_function(t, shrink_ratio=11.6)
            x, y = shrink(x, y, halo_radius)
            if (x, y) not in heart_halo_point:
                heart_halo_point.add((x, y))
                x += random.randint(-14, 14)
                y += random.randint(-14, 14)
                size = random.choice((1, 2, 2))
                all_points.append((x, y, size))

    # 生成轮廓点
        for x, y in self._points:
            x, y = self.calc_position(x, y, ratio)
            all_points.append((x, y, random.randint(1, 3)))

        # 生成边缘扩散点
        for x, y in self._edge_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            all_points.append((x, y, random.randint(1, 2)))

        # 生成中心扩散点
        for x, y in self._center_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            all_points.append((x, y, random.randint(1, 2)))

        self.all_points[generate_frame] = all_points

    def render(self, render_canvas, render_frame):
        """
        在指定帧上将点渲染到画布上。

        :param render_canvas: 要绘制的画布
        :param render_frame: 当前帧数
        """
        for x, y, size in self.all_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=HEART_COLOR)


def draw(main: Tk, render_canvas: Canvas, render_heart: Heart, render_frame=0):
    """
    在画布上绘制爱心动画。
    :param main: 主窗口
    :param render_canvas: 要渲染的画布
    :param render_heart: 要渲染的 Heart 对象
    :param render_frame: 当前帧数
    """
    render_canvas.delete('all')  # 清空画布
    render_heart.render(render_canvas, render_frame)  # 渲染爱心点
    main.after(160, draw, main, render_canvas, render_heart, render_frame + 1)  # 调度下一帧


if __name__ == '__main__':
    root = Tk()  # 创建主窗口
    root.title('爱心')  # 设置窗口标题
    canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    canvas.pack()  # 将画布添加到主窗口
    heart = Heart()  # 创建 Heart 对象
    draw(root, canvas, heart)  # 开始绘制
    root.mainloop()  # 启动 Tkinter 事件循环