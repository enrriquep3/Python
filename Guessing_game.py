# This program create a random name and ask the user to guess the number.

import random
num = random.randint(0, 101)
run = True
print('Welcome to the Guess Number Game.')
while run:
    guess = int(input("Enter your number between 0-100: "))

    if guess == num:
        print("You Are Correct!")
        run = False

    if guess > num:
        print("Your number is to high, keep trying")

    if guess < num:
        print("Your number is too low, keep trying")
