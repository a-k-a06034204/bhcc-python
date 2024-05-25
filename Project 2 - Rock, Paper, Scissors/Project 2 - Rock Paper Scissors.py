#By terra-ko
#Project 2 Rock Paper Scissors

import random

wepons = ("R,r,P,p,S,s")
running = True
#count wins, losses, ties, and how many each user selected each weapon

while running: 
    player = None
    cpu = random.choice(weapons)

while player not in weapons:
    player = input("Rock, Paper, Scissors? ")
    print(f"Player:{player}")
    print(f"cpu:{cpu}")

if player == cpu:
    print("We've tied!")

elif player == "Rock" and cpu == "Scissors":
    print("Looks like you won this time!")

elif player == "Paper" and cpu == "Rock":
    print("Looks like you won this time!")

elif player == "Scissors" and cpu == "Paper":
    print("Looks like you won this time!")

else:
    print("Sorry, you lose!")

if not input("Would you like to play again? (y/n): ").lower() == "y":
    running = False
    #Qq to quit/"are you sure you want to quit?"
print("Thank you for playing, goodbye!") 

