def tran(s):
    try:
        return int(s)
    except ValueError:
        return "这不是数字"
print(tran(False))