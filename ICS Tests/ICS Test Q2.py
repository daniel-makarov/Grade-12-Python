# Daniel Makarov
# ICS Test Q2
# Date: October 18 2021

# Prices of goods
bread_price = float(input("Hello, how much does one loaf of bread cost? "))
cheese_price = float(input("How much does one block of cheese cost? "))

# Calculates the price with the amount of goods
total_bread_cost = bread_price*2
total_cheese_cost = cheese_price*3

# Calculates total cost
total_cost = total_bread_cost + total_cheese_cost

# Rounds amount to 2 decimals
total_cost = "{:.2f}".format(total_cost)

# Gives final statement
print("The cost for 2 loaves of bread and 3 blocks of cheese is $" + str(total_cost))
