# Project 2 - Rock, Paper, Scissors
# By: Ashley Kochapski

import random

# Count wins, losses, ties, and how many each user selected each weapon

weapons = ["R","r","P","p","S","s"]
player_chose_rock = 0
player_chose_paper = 0
player_chose_scissors = 0
player_wins = 0
cpu_wins = 0
ties = 0

print("Hello user! :)")
running = True
while running: 
    player = ''
    cpu = random.choice(weapons)

    # Make the player choose a weapon:
    while player not in weapons:
        player = input("Rock (R), Paper (P), Scissors (S)? ")
    print(f"Player: {player}")
    print(f"CPU: {cpu}")

    # Count the weapon choices
    if player.lower() == 'r':
        player_chose_rock += 1
    if player.lower() == 'p':
        player_chose_paper += 1
    if player.lower() == 's':
        player_chose_scissors += 1

    # Count the wins:
    if player == cpu:
        print("We've tied!")
        ties += 1
    elif player == "r" and cpu == "s":
        print("Looks like you won this time!")
        player_wins += 1
    elif player == "p" and cpu == "r":
        print("Looks like you won this time!")
        player_wins += 1
    elif player == "s" and cpu == "p":
        print("Looks like you won this time!")
        player_wins += 1
    else:
        print("Sorry, you lose!")
        cpu_wins += 1

    # Ask if they want to play another round:
    if not input("Would you like to play again? (y/n): ").lower() == "y":
        running = False

# Show the results:
print(f"CPU wins: {cpu_wins}")
print(f"Player wins: {player_wins}")
print(f"Rounds that ended in a tie: {ties}")
print(f"The number of times the user selected each weapon (Rock, Paper, Scissors):")
print(f"- Rock: {player_chose_rock}")
print(f"- Paper: {player_chose_paper}")
print(f"- Scissors: {player_chose_scissors}")
print("Thank you for playing, goodbye!") 