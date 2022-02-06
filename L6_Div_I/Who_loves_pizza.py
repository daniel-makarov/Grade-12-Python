# Daniel Makarov
# Date: December 10, 2021
# Who Loves Pizza?

pizza_list = ["cheese pizza", "pepperoni pizza", "chicago pizza"]

for pizza in pizza_list:
  if pizza == "cheese pizza":
    print("I love", pizza_list[0] + ", its my favorite!")
  elif pizza == "pepperoni pizza":
    print("I also like", pizza_list[1] + ", its not bad.")
  elif pizza == "chicago pizza":
    print("Another good choice is", pizza_list[2] + ", it tastes nice.")

print("I really love pizza!")

friend_pizzas = ["cheese pizza", "pepperoni pizza", "chicago pizza"]

pizza_list.append("new york-style pizza")
#print("My pizza list:", pizza_list)

friend_pizzas.append("greek pizza")
#print("Friend pizza list:", friend_pizzas)

print()
print("My favorite pizzas are:")
for pizza_name in pizza_list:
  print("-", pizza_name)

print()
print("My friend's favorite pizzas are:")
for pizza_name in friend_pizzas:
  print("-", pizza_name)