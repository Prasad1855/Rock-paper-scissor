import random

def gamewin(computer,you):
    if computer == you:
        return None
    elif computer == "rock":
        if you == "scissor":
            return False
        elif you == "paper":
            return True
    elif computer == "paper":
        if you == "rock":
            return False
        elif you == "scissor":
            return True
    elif computer == "scissor":
        if you == "paper":
            return False
        elif you == "rock":
            return True

print("computer turn  rock or paper or scissor:  ")
random_no = random.randint(1,3)
if random_no == 1:
    computer = "rock"
elif random_no == 2:
    computer = "paper"
elif random_no == 3:
    computer = "scissor"

you=input("your turn  rock or paper or scissor:  ") 
a = gamewin(computer,you)

print(f"computer choose {computer}")
print(f"you choose {you}")

if a == None:
    print("The game is tie/nTry one more time")
elif a == True:
    print("You win ")
else:
    print("You loose/nBetter luck next time")        

       


            