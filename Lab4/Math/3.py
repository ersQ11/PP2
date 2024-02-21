import math

def area():
    n = int(input("Input number of sides: "))
    a = int(input("Input the length of a side: "))
    S = (n * a ** 2) / (4 * math.tan(math.pi/n))
    print(f"The area of the polygon is: {math.floor(S)}")

area()
