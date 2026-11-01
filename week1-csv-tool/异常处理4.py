def read_file(filename):
    try:
        with open(filename) as f:
            next(f)
            return f.read()
    except FileNotFoundError:
        return f"文件 {filename} 不存在"

print(read_file("point.csv"))