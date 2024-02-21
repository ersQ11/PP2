def decr():
    n = int(input())
    for i in range(n, -1, -1):
        yield i

nums = decr()

for i in nums:
    print(i)