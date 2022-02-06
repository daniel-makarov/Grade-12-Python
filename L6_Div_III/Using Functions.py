# Daniel Makarov
# Date: December 17, 2021
# Using Functions

import random

def check_number(user_num, computer_num):
  ### Checks if the user's number is higher, lower, or equal to the computer's chosen number. ###
  response = 0

  if user_num > computer_num:
    response = 1
  elif user_num < computer_num:
    response = 2
  elif user_num == computer_num:
    response = 3
  
  return response

def tries(user_tries):
  ### Displays number of tries. ###
  print("Number of tries:", user_tries)

num_of_tries = 0

# Computer chooses random number from 1 to 100
random_num = (random.randint(1, 100))
#print("Number that the computer chose:", random_num)

stop_program = True

while stop_program:
  try:
    user_number = int(input("Enter a number: "))
  except:
    num_of_tries += 1
    print("Your input seems weird, please retry")
    tries(num_of_tries)
    continue
  #print("User's chosen number:", user_number)

  same_number_or_not = check_number(user_number, random_num)

  if same_number_or_not == 1:
    print("Your number is too high")
    num_of_tries += 1
    tries(num_of_tries)

  elif same_number_or_not == 2:
    print("Your number is too low")
    num_of_tries += 1
    tries(num_of_tries)

  elif same_number_or_not == 3:
    print("You guessed the number!")
    num_of_tries += 1
    tries(num_of_tries)
    stop_program = False
