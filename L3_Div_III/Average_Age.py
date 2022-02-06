# Daniel Makarov
# Date: November 2, 2021
# Average Age

group_member_ages = []

while True:
  try:
    num_of_people = int(input("How many people are in the group? "))

    if num_of_people <= 0:
      print("Please enter a number that is of value 1 or more")
      continue
    else:
      break
  except:
    print("Something is wrong with your input, please try again")
    continue

for person in range(0, num_of_people):
  while True:
    try:
      age = int(input("Please enter in the age of person #" + str(person+1) + ": "))
      if age < 0:
        print("Please enter a valid age")
        continue
      break
    except:
      print("Something is wrong with your input, please try again")
      continue

  #print("Persons age:", age)

  group_member_ages.append(age)

#print("All ages list:", group_member_ages)

average_age_of_group = sum(group_member_ages)/len(group_member_ages)

print("The average age of this group is", round(average_age_of_group, 2), "years old")