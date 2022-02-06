# Daniel Makarov
# Date: December 3, 2021
# Collatz Conjecture

while True:
  try:
    number = float(input("Enter a number: "))
    if number <= 0:
      print("Please enter a number greater than 0.")
      continue
  except:
    print("There is something wrong with your input, please try again.")
    continue
  break

#print("Number chosen:", number)
print(number)

num_of_steps = 0 

while number > 0:

  if number == 1:
    #print("You reached 1!")
    print("Number of steps it took to reach 1:", num_of_steps)
    break

  elif number%2 == 0:
    num_of_steps += 1
    number = number/2
    #print("Step Number:", num_of_steps)
    print(number)
    continue

  elif number%2 != 0:
    num_of_steps += 1
    number = (number*3) + 1
    #print("Step Number:", num_of_steps)
    print(number)
    continue