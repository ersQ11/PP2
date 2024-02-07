class Points():
    def __init__(self):
        self.x1 = int(input())
        self.y1 = int(input())
        self.x2 = int(input())
        self.y2 = int(input())
    def show(self):
        print (f"({self.x1};{self.y1})")
        print (f"({self.x2};{self.y2})")
    def move(self):
        self.choose = int(input("Choose point, that you want to move 1 or 2: "))
        if self.choose == 1:
            self.var = str(input("Choose variable, that you want to move x or y: "))
            if self.var == "x":
                self.ax = int(input())
                self.x1 = self.x1 + self.ax
            elif self.var == "y":
                self.ay = int(input())
                self.y1 = self.y1 + self.ay
        if self.choose == 2:
            self.var = str(input("Choose variable, that you want to move x or y: "))
            if self.var == "x":
                self.ax = int(input())
                self.x2 = self.x2 + self.ax
            elif self.var == "y":
                self.ay = int(input())
                self.y2 = self.y2 + self.ay
    def dist(self):
        self.distx = self.x1 - self.x2
        self.disty = self.y1 - self.y2
        print (f"({self.distx};{self.disty})")


point = Points()

point.show()
point.move()
point.show()
point.dist()
