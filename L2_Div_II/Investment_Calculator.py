# Daniel Makarov
# Investment Calculator
# Date: October 25 2021

while True:
    try:
        principal = float(input("Enter initial amount: "))
        #print("Inital Amount:", principal)
        break
    except:
        print("Something seems wrong with your initial ammount. Please try again")

while True:
    try:
        interest_rate = float(input("Enter interest rate: "))
        #print("Interest rate:", interest_rate)
        break
    except:
        print("Something seems wrong with your input. Please try again")

while True:
    try:
        years = int(input("Please input the number of years: "))
        #print("Input number of years:", years)
        break
    except:
        print("Something seems wrong with your input of years. Please try again")

years += 1


# Outputs a table for the compound interest over a set of years
for number_of_years in range(1, years):
    principal = principal * (1 + interest_rate)
    #print("Number:", number_of_years, "Total:", principal)

    # Rounds amount to 2 decimals
    principal_number = "{:.2f}".format(principal)
    print(number_of_years, principal_number)