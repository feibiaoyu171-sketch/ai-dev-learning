def safe_divide(a, b):
    try :
        return a/b

    except ZeroDivisionError:
        return "不能除以0"
print(safe_divide(1,0))