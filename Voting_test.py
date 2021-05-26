# This is a Voting test Implement a voting test to prove if the user is 18 years old or older.

print("HI Citizens this is a age test to verify if you are allowed to vote!")
print('What would be your age on the election day?')
age = int(input())
if age <= 17:
    print("you cannot Vote yet, wait until you are 18 years old.")
if age >= 18:
    print("you can vote on this election")




