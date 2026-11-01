class Counter:
    def __init__(self):
        self.count = 0

    def add(self,n):
        self.count += n
        return self.count
    def get(self):
        return self.count
c = Counter()
c.add(3)
c.add(2)
print(c.get())
