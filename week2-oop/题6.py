def safe_int(s):
    try :
        return int(s)
    except ValueError:
        return 0
print(safe_int("abc"))
print(safe_int("42"))