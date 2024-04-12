def fib_num(c):
    a = 0
    b = 1
    for i in range(0, c+1):
        num = a
        a = b
        b = b + num
        yield num

n = int(input())
for i in fib_num(n):
    print(i)

     
