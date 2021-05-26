# This program will check if the 2 numbers that the user entered is greater than 100 and return a response that the number is too big
# If the number is equal or lower than 100 the program will add the numbers and return the result.

print("Please enter a number: ")
num1 = int(input())
if num1 > 99:
    print("That number is greater than 100. Please try again.")
elif num1 < 1:
    print("That number is less than 1. Please try again.")

print("Again, please type any number:")
num2 = int(input())
if num2 > 99:
    print("That number is greater than 100. Please try again.")
elif num2 < 1:
    print("That number is less than 1. Please try again.")

sum = num1 + num2
if sum >= 101:
    print("They add up to a big number")
elif sum <= 100:
    print("Your two numbers are equal to:", sum)
