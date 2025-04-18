import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import json

# 加载城市列表
with open('city_code.json', 'r', encoding='utf-8') as file:
    city_data = json.load(file)
    if city_data:
        cities = [key for key in city_data]

def get_city_code(city_name):
# 读取城市天气代码
    try:
        code = city_data[city_name]
        return code
    except:
        messagebox.showerror('提示', '输入城市不存在')

def get_weather(city_name):
    city_code = get_city_code(city_name)
    # 目标城市的URL
    CITY_URL = f'http://www.weather.com.cn/weather/{city_code}.shtml'
    # 模拟浏览器头部信息
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',}
    # 发送请求并获取响应内容
    response = requests.get(CITY_URL, headers=headers)
    response.raise_for_status()
    # 如果请求失败，则抛出异常
    content = response.content.decode('utf-8')
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(content, 'html.parser')
    # 根据实际页面结构，找到包含天气信息的元素 这里假设天气信息存储在某些具有特定类名或ID的元素中，你需要根据实际情况调整
    weather_elements = soup.select('ul[class="t clearfix"] li')
    # 天气信息在一个ul标签中类名为t clearfix的li标签中
    # 遍历天气信息元素，提取所需数据
    weather_data = []

    for element in weather_elements:
        # 这里需要根据实际的HTML结构来提取日期、温度和天气状况等信息
        # 日期存储在一个为h1的标签中
        date_element = element.select_one('h1')
        # 天气状态存储在一个为wea的类中
        sta_element = element.select_one('.wea')
        # 温度存储在一个为tem的类中
        temp_element = element.select_one('.tem')
        # 风力等级存储在一个为win的类中
        weather_element = element.select_one('.win')

        if date_element and sta_element and temp_element and weather_element:
            date = date_element.get_text().strip()
            sta = sta_element.get_text().strip()
            temp_data = temp_element.get_text().strip()
            wind = weather_element.get_text().strip()

            if '/' in temp_data:
                temp_max, temp_min = temp_element.get_text().strip().split('/')[:2]
                weather_data.append(f"{date},{sta}, 温度: {temp_min}~{temp_max}, 风力: {wind}" + "\n")
            else:
                weather_data.append(f"{date},{sta}, 温度: {temp_data}, 风力: {wind}" + "\n")
        else:
            messagebox.showinfo('提示', "无法提取完整的天气信息")
            return

        return weather_data

# 更新天气显示
def update_weather():
    city = city_var.get()
    if city:
        weather_data = get_weather(city)
        weather_text.delete(1.0, tk.END)
        for data in weather_data:
            weather_text.insert(tk.END, data + "\n")

# 动态更新城市列表
def filter_cities(*args):
    search_text = city_var.get().strip().lower()
    filtered_cities = [city for city in cities if search_text in city.lower()]
    city_combobox['values'] = filtered_cities

root = tk.Tk()
root.title("天气查询APP")
root.geometry("400x300+700+300")
root.resizable(False, False)

# 创建城市选择框
label_name = tk.Label(root, text='查询城市', font=('仿宋', 12))
label_name.place(x=40, y=30)
city_var = tk.StringVar()

city_combobox = ttk.Combobox(root, textvariable=city_var, values=cities, font=('仿宋', 12), state="normal")
city_combobox.place(x=110, y=30)
city_combobox.bind('', lambda e: filter_cities())

# 创建查询按钮
query_button = tk.Button(root, text="查询", font=('仿宋', 12), width=5, command=update_weather)
query_button.place(x=300, y=27)

# 创建天气显示区
weather_text = tk.Text(root, font=('仿宋', 10), height=16, width=50)
weather_text.place(x=20, y=70)
root.mainloop()