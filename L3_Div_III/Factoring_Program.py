# Daniel Makarov
# Date: November 2, 2021
# Factoring Program

initial_divisor = 1

# Factors of a number
factors = []

while True:

  print('Please enter a number to factor (or "QUIT" to quit):')
  number = input().upper()
  #print(number)
  
  if number == "QUIT":
    break
  
  try:
    number = int(number)
  except:
    print("Something is wrong with your input, please try again")
    continue

  if number > 0:
    while initial_divisor <= number:
      if number%initial_divisor == 0:
        factors.append(initial_divisor)
        #print("List of numbers:", factors)
        
      initial_divisor += 1

    #print("List of numbers:", factors)

    final_statement = [str(number) for number in factors]

    #print(final_statement)

    final_statement = ", ".join(final_statement)

    print(final_statement)
    
    initial_divisor = 1
    factors = []
    continue

  elif number < 0:
    number = str(number)

    number = number.replace("-", "")

    number = int(number)

    while initial_divisor <= number:
      if number%initial_divisor == 0:
        factors.append(initial_divisor)
        #print("List of numbers:", factors)
          
      initial_divisor += 1

    #print("List of numbers:", factors)

    plus_minus_factors = factors[:((len(factors))//2)]
    minus_plus_factors = factors[((len(factors))//2):]
    #print(plus_minus_factors)
    #print(minus_plus_factors)

    plus_minus_factors = [str("±") + str(number) for number in plus_minus_factors]
    minus_plus_factors = [str("∓") + str(number) for number in minus_plus_factors]
    #print(plus_minus_factors)
    #print(minus_plus_factors)

    final_statement = plus_minus_factors + minus_plus_factors

    #print(final_statement)
    
    final_statement = ", ".join(final_statement)

    print(final_statement)
    
    initial_divisor = 1
    factors = []
    continue

  elif number == 0:
    print("Infinite number of factors")