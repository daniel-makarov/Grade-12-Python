# Daniel Makarov
# Date: December 3, 2021
# Pairing up people

while True:
  try:
    people = int(input("How many people are there? "))
    if people <= 1:
      print("Please enter 2 people or more.")
      continue
    break
  except:
    print("There is a problem with your input. Try again.")
    continue

people_list = []

for num_of_people in range (1, people+1):
  people_list.append(num_of_people)

#print("List of people:", people_list)

for first_person in people_list:
  for second_person in people_list[first_person:]:
    if first_person != second_person:
      print(first_person, second_person)