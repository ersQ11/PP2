def ev():
    current = 0
    stop = int(input())
    while current <= stop-2:
        current += 2
        yield current
    
    
mynums = ev()

for i in mynums:
    print(i)