try:
    with open("point.csv") as f:
        next(f)
        print(f.read())
except FileNotFoundError:
    print("当前文件不存在")