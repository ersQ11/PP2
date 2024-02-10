import random

def convert(x):
    return 28.3495231 * x

def solve(headsnum, legsnum):
    chickens = int(legsnum / 2)
    rabbits = 0
    while chickens + rabbits > headsnum:
        chickens -= 2
        rabbits += 1
    print (f"There are {rabbits} rabbits and {chickens} chickens")

def py_game():
    name = input("Hello! What is your name?\n")
    x = random.randint(1, 21)
    y = int(input("Well, KBTU, I am thinking of a number between 1 and 20. Take a guess.\n"))
    guesses = 1
    while x != y:
        if y < x:
            y = int(input("Your guess is too low. Take a guess.\n"))
            guesses += 1
        elif y > x:
            y = int(input("Your guess is too much. Take a guess.\n"))
            guesses += 1
    print(f"Good job, {name}! You guessed my number in {guesses} guesses!")

def volume():
    R = float(input())
    return float(3/4 * 3.14 * R ** 3)

def has_33(nums):
    for i in range(1, len(nums)-1):
        if number_list[i] == 3:
            if number_list[i+1] == number_list[i] or number_list[i-1] == number_list[i]:
                return False
            else:
                return True

con = int(input())
print (convert(con))

py_game()

print(volume())

heads = int(input("Number of heads: "))
legs = int(input("Number of legs: "))

solve(heads, legs)

numbers = input()
number_list = list(int(x) for x in numbers.split())
print(has_33(number_list))
