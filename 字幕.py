import turtle as tle
import random as rnd
import math

def Romantic():
    #初始化画布
    tle.setup(1.0, 1.0)
    tle.screensize(1.0,1.0)  # 设置画布大小
    tle.bgcolor('black')  # 设置画布颜色
    tle.title("嘻嘻")  # 设置标题
    t = tle.Pen()
    t.ht()  # 隐藏画笔


    # 文案列表
    messages = ["我爱你",
                "我心中只有你",
                "I Love You!",
                "永远爱你",
                "你是我年少的欢喜",
                "你是我的一切！",
                "一生一世一双人",
                "余生我陪你走",
                "陪你到来生",
                "春风十里不如你",
                "我的心与你紧紧相连",
                "三生有幸来日方长",
                "夜很长幸有你",
                "爱你的全部",
                "踏过八荒四海只为你",
                "愿得一人心",
                "众里寻他千百度",
                "顶峰相见",
                "等你下课",
                "往后余生",
                "Missing You!",
                "做我女朋友好么",
                "你已经在我的未来里了",
                "陪你到世界之巅",
                "白头偕老",
                "我喜欢你",
                "好想好想你",
                "想你想你想你",
                "今夜月色真美",
                "你是我的唯一",
                "你是我心灵的归宿"
                ]
    class Love():  # 文案类
        def __init__(self):
            self.x = rnd.randint(-1000, 1000)  # 文案的横坐标
            self.y = rnd.randint(-500, 500)  # 文案的纵坐标
            self.f = rnd.uniform(-3, 3)  # 文案左右移动
            self.speed = rnd.uniform(2, 5)  # 文案移动速度
            self.message = rnd.choice(messages)  # 文案
            self.color = "#%02x%02x%02x" % (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))  # 文案的颜色

        def draw(self):  # 写每个文案
            t.penup()  # 提笔
            t.goto(self.x, self.y)  # 随机位置
            t.pendown()  # 落笔
            t.color(self.color)  # 文案颜色
            t.write(self.message, align="center", font=("Comic Sans MS", 24, "bold"))

        def move(self):  # 文案移动函数
            if self.y <= 500:  # 当文案还在画布中时
                self.y += self.speed  # 设置上下移动速度
                self.x -= self.speed * math.sin(self.f)  # 设置左右移动速度
            else:  # 当文案漂出了画布时，重新生成一个文案
                self.x = rnd.randint(-1000, 1000)
                self.y = -500
                self.f = rnd.uniform(-3.14, 3.14)  # 文案左右移动呈正弦函数
                self.speed = rnd.uniform(2, 5)  # 文案移动速度
                self.message = rnd.choice(messages)  # 文案
                self.color = "#%02x%02x%02x" % (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))  # 文案的颜色

    class Ball():  # 彩球类
        def __init__(self):
            self.r = rnd.uniform(2, 5)  # 彩球的半径
            self.x = rnd.randint(-1000, 1000)  # 彩球的横坐标
            self.y = rnd.randint(-500, 500)  # 彩球的纵坐标
            self.speed = rnd.uniform(2, 10)  # 彩球移动速度
            self.color = "#%02x%02x%02x" % (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))  # 彩球的颜色
            self.outline = 10  # 彩球的大小

        def draw(self):  # 画每个彩球
            x = self.r  # 彩球的半径
            t.pensize(self.outline)  # 彩球的大小
            t.penup()  # 提笔
            t.goto(self.x, self.y)  # 随机位置
            t.pendown()  # 落笔
            t.color(self.color)  # 彩球颜色
            t.begin_fill()
            t.fillcolor(self.color)
            t.circle(x)

        def move(self):  # 彩球移动函数
            if self.y >= -500:  # 当彩球还在画布中时
                self.y -= self.speed  # 设置上下移动速度
            else:  # 当彩球漂出了画布时，重新生成一个彩球
                self.r = rnd.uniform(2, 3)
                self.x = rnd.randint(-1000, 1000)
                self.y = 500
                self.speed = rnd.uniform(2, 10)
                self.color = "#%02x%02x%02x" % (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
                self.outline = 10

    Loves = []  # 用列表保存所有文案
    for i in range(595):
        Loves.append(Love())
        Loves.append(Ball())
        Loves.append(Ball())

    while True:  # 开始绘制
        tle.tracer(0)
        t.clear()
        for i in range(199):  # 66个漂浮的文案
            Loves[i].move()
            Loves[i].draw()
        tle.update()
    tle.mainloop()

if __name__ == '__main__':
    Romantic()  # 显示满屏飘字表白代码