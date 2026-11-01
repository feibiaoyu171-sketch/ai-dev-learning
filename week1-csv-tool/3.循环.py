from main import depths

for i in range(1,5):
    print(i)
count = 1
while count <5:
    print(count)
    count = count+1
depths = [8.5, 15.2, 23.7, 55.1, 72.4]
for depth in depths:
    if depth < 20 :
        print(depth,"浅水")
    elif depth < 60 :
        print(depth,"中等")
    else :
        print(depth,"中等")