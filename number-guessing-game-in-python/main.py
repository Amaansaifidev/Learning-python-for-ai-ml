import random
number = random.randint(1, 10)
userguess = int(input("enter your guess: "))
while number != userguess:
    print(f"it was {number}")
    break
number = int(input("enter again: "))
print("you got it")
print(f"it was {number}")
