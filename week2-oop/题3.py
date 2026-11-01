class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_pass(self):
        return self.score >= 60

print(Student("小明", 85).is_pass())
