class Rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height*self.width

    def perimeter(self):
        return (self.width+self.height)*2

print(Rectangle(3, 4).area())