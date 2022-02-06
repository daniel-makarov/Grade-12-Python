# Daniel Makarov
# Date: November 2, 2021
# Multiplication table

# Inital multiplier
multiplier = 1

stop_program = True

while stop_program:
  for multiplicand in range(1,13):
    print(multiplier, "X", str(multiplicand), "=", str(multiplier*multiplicand))
  multiplier += 1
  print()

  if multiplier == 13:
    break