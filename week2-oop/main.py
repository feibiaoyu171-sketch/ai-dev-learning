"""第 2 周小项目：用面向对象重构水深数据工具。

小练习：
1. 定义一个 Point 类，__init__ 接收 lon（经度）和 lat（纬度）

提示：
- 用 class 定义类，类名大写开头
- __init__ 是初始化方法，第一个参数是 self
- 用 self.lon = lon 存属性
"""
import csv
import json
class DepthData:
    def __init__(self,filename):
        self.filename = filename
        self.depths = []

    def load(self):
        try:
            with open(self.filename) as f:
                if self.filename.endswith(".csv"):
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        self.depths.append(float(row[3]))
                elif self.filename.endswith(".json"):
                    data = json.load(f)
                    for item in data:
                        self.depths.append(item["depth_m"])
        except FileNotFoundError:
            print("文件未找到。")

    def max_depth(self):
        return max(self.depths)

    def min_depth(self):
        return min(self.depths)

    def avg_depth(self):
        return round(sum(self.depths) / len(self.depths), 1)
d = DepthData("points.json")
d.load()
print(d.avg_depth())