"""第 1 周小项目：读水深采样点 CSV，算最大 / 最小 / 平均水深。

你要完成的事：
1. 用 Python 读取同目录下的 points.csv
2. 提取「depth_m（水深）」这一列
3. 算出最大值、最小值、平均值
4. 打印结果，比如：最大水深 72.4m，最小水深 6.3m，平均水深 xx.xm

提示：
- 用 Python 自带的 csv 模块（import csv）就能读，不用装第三方库
- CSV 读出来默认是字符串，水深要先转成 float 才能做数学运算
- 第一行是表头，处理数据时要跳过它
"""

# TODO: 在这里写你的代码
import csv
depths = []
with open("points.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        depth = float(row[3])
        depths.append(depth)
max_dep = max(depths)
min_dep = min(depths)
aver_dep = round(sum(depths)/len(depths),1)
print("max=",max_dep,"m")
print("min=",min_dep,"m")
print("aver=",aver_dep,"m")
