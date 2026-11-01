while True:
    try :
        a = int(input("请输入数字:"))
        print(a)
        break
    except ValueError:
        print("请输入数字")
        continue