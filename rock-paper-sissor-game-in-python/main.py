import random
user_input = input("enter your move: ")
random = random.choice(("rock", "paper", "scissors"))
while True:
    if user_input != random:
            print("you are wrong")
            print(f"it was {random}")
            user_input = input("try again: ")
    else: 
        print(f"you got it right {random}")
        break
