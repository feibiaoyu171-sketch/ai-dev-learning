name = "文昌站"
depth = 23.7
print(f"{name}的深度为{depth:.2f}m",f"{name}")
name2 = "  文昌站  "
print(len(name2))
name2.strip()
print(len(name2))
s = "1,2,3,4,5"
print(s)
s2 = s.split(",")
print(s2)
print(len(s2))
print(",".join(s2))
str1 = "hello"
print(str1)
print(str1.upper())
print(str1.replace("e","a"))

s = "  hello,python,world  "
s = s.strip()
print(s)
s1 = s.split(",")
print(s1)
print("/".join(s1))
print(f"一共有{len(s1)}个单词")

