# Daniel Makarov
# Date: December 10, 2021
# Number Guessing Game

import random

num_of_tries = 0

def check_number(user_num, computer_num):
  ### Checks if the user's number is higher, lower, or equal to the computer's chosen number. ###
  
  global stop_program
  global num_of_tries

  if user_num > computer_num:
    print("The number is too high.")
    print("Number of Tries:", num_of_tries)

  elif user_num < computer_num:
    print("The number is too low.")
    print("Number of Tries:", num_of_tries)

  elif user_num == computer_num:
    print("You guessed the number!")
    print("Number of Tries:", num_of_tries)
    stop_program = False

# Computer chooses random number from 1 to 100
random_num = (random.randint(1, 100))
#print("Number that the computer chose:", random_num)

stop_program = True

while stop_program:
  try:
    user_number = int(input("Enter a number: "))
    num_of_tries += 1
  except:
    num_of_tries += 1
    print("Your input seems weird, please retry.")
    print("Number of Tries:", num_of_tries)
    continue
  #print("User's chosen number:", user_number)

  check_number(user_number, random_num)