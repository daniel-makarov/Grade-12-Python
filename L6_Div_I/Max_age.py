# Daniel Makarov
# Date: November 22, 2021
# Max Age

import sys

name = input("Please input a name: ") 

if name == "stop":
  print("Okay!")
  sys.exit()

while True:
  try:
    age = int(input("Please input their age: "))
    if age < 0:
      print("Please enter a valid age.")
      continue
  except:
    print("Please enter in a valid number.")
    continue
  break

people_list = {name:age}

run = True
while run:
  name = input("Please input a name: ") 

  if name == "stop":
    break
    run = False

  while True:
    try:
      age = int(input("Please input their age: "))
      if age < 0:
        print("Please enter a valid age.")
        continue
    except:
      print("Please enter in a valid number.")
      continue
    break

  people_list[name] = age

#print(people_list)

# Finds the oldest person in the list
oldest_person = str(max(people_list, key = people_list.get))

print("The oldest person is", oldest_person + ".")