class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get(self):
        return self.count
c = Counter()
c.increment()
c.increment()
print(c.get())
c.reset()
print(c.get())