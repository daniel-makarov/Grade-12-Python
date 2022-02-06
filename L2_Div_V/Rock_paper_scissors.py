# Daniel Makarov
# Date: October 30
# Rock Paper Scissors Game

import random

wins = 0
losses = 0
ties = 0
stop = 0

computer_actions = ["r", "p", "s"]
#print("Computer's available actions:", computer_actions)

print("ROCK, PAPER, SCISSORS")

run_game = True
while run_game:
  print(wins, "Wins,", losses, "Losses,", ties, "Ties")

  while True:
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    player_choice = input()
    #print("Player choice:", player_choice)

    if player_choice == "r":
      print("ROCK versus...")
      break
    elif player_choice == "p":
      print("PAPER versus...")
      break
    elif player_choice == "s":
      print("SCISSORS versus...")
      break
    elif player_choice == "q":
      stop += 1
      break
    else:
      print("Something seems wrong with your input, please try again!")

  if stop == 1:
    break
  computer_action = random.choice(computer_actions)
  #print("Computer Choice:", computer_action)
  
  if computer_action == "r":
    print("ROCK")
  elif computer_action == "p":
    print("PAPER")
  elif computer_action == "s":
    print("SCISSORS")

  if player_choice == computer_action:
    print("It's a tie!")
    ties += 1

  elif player_choice == "r":
    if computer_action == "s":
      print("You win!")
      wins += 1
    else:
      print("You lose!")
      losses += 1

  elif player_choice == "s":
    if computer_action == "p":
      print("You win!")
      wins += 1
    else:
      print("You lose!")
      losses += 1

  elif player_choice == "p":
    if computer_action == "r":
      print("You win!")
      wins += 1
    else:
      print("You lose!")
      losses += 1