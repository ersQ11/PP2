class Shape():
    def __init__(self):
        self.lenght = int(input())
        self.width = int(input())
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self):
        self.lenght = int(input())
        self.width = int(input())
    def area(self):
        return self.lenght * self.width

rectangle = Rectangle()
print (rectangle.area())