def find_common(a, b):
    c = []
    for i in a:
        if i in b and i not in c:
            c.append(i)
    return  c

print(find_common([1,2,3],[1,1,2]))