def solve(headsnum, legsnum):
    chickens = int(legsnum / 2)
    rabbits = 0
    while chickens + rabbits > headsnum:
        chickens -= 2
        rabbits += 1
    print (f"There are {rabbits} rabbits and {chickens} chickens")

heads = int(input("Number of heads: "))
legs = int(input("Number of legs: "))

solve(heads, legs)


