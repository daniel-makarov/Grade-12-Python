# Daniel Makarov
# Date: November 22, 2021
# Savings Program

import math

goal_name = input("What do you want to save money for? (i.e. house, car, computer...) ")
#print("You will save money for a", goal_name + ".")

while True:
  try:
    goal_cost = float(input("How much will it cost? $"))
    if goal_cost <= 0:
      print("Please input a number greater than $0.")
      continue
    break
  except:
    print("Please input a valid number.")
    continue

#print("Your", goal_name, "will cost $" + str(goal_cost))

goal_cost = round(goal_cost, 2)

#print("Your", goal_name, "will cost $" + str(goal_cost))

while True:
  try:
    money_set_aside = float(input("How much will you set aside every month? $"))
    if money_set_aside <= 0:
      print("Please input a number greater than $0.")
      continue
    break
  except:
    print("Please input a valid number.")
    continue

#print("You will set aside $" + str(money_set_aside), "each month.")

# Number of months to meet the savings goal
months = goal_cost/money_set_aside
#print("Number of months to meet goal:", months)

# Rounds up number of months
months = math.ceil(months)
#print("Number of months to meet goal:", months)

print("You will need to set aside $" + str(format(money_set_aside, '.2f')), "for", months, "month(s) until you fully pay off your", goal_name + ".")