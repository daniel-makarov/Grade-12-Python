# Daniel Makarov
# Date: October 30, 2021
# Going to the movies, Extention 1

name = input("Hello, welcome to Cinaplex! What's your name? ")

while True:
  try:
    age = int(input("Hello " + str(name) + "! How old are you? "))
    #print("Age:", age)
    if age < 0:
      print("You can't be younger than zero years old. Try inputting your age again.")
      continue
    break
  except:
    print("Sorry, something seems wrong with your age.")
    continue

if age < 3:
  ticket_price = 0
  print("Your ticket is free!")
elif age >= 3 and age <= 12:
  ticket_price = 10
  print("The price of your tickets is $10.00")
elif age > 12 and age < 65:
  ticket_price = 25
  print("The price of your tickets is $25.00")
elif age >= 65:
  ticket_price = 15
  print("The price of your tickets is $15.00")

while True:
  try:
    num_of_tickets = int(input("How many tickets do you want? "))
    if num_of_tickets <= 0:
      print("Please choose one ticket or more.")
      continue
    break
  except:
    print("Sorry, something seems wrong with your input.")
    continue

#print("Ticket price:", ticket_price)

#print("Number of tickets:", num_of_tickets)

total_cost = (ticket_price*num_of_tickets)

total_cost = "{:.2f}".format(total_cost)

#print("Total cost:", total_cost)

if str(total_cost) == "0.00":
  print("You do not have to pay anything!")
else:
  print("Please pay $" + str(total_cost))