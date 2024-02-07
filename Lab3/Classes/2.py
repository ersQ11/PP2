class Shape():
    def __init__(self):
        self.lenght = int(input())
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self):
        self.lenght = int(input())
    def area(self):
        return self.lenght ** 2

square = Square()
print (square.area())