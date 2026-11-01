import csv
with open("book.txt","w") as f:
    f.write("我爱你！\n")
    f.write("我不爱你了！\n")
with open("book.txt") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)