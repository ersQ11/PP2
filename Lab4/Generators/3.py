def divisible(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

N = int(input())
div = divisible(N)

for i in div:
    print(i)