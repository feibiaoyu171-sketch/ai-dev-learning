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
                        self.depths.append(float(item["depth_m"]))
        except FileNotFoundError:
            print("文件不存在。")

    def max_depth(self):
        return max(self.depths)
    def min_depth(self):
        return min(self.depths)
    def avg_depth(self):
        return round(sum(self.depths)/len(self.depths),1)

d = DepthData("points.json")
d.load()
print(d.depths)
print(d.max_depth())
