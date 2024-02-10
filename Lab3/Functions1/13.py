import random

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
    
py_game()