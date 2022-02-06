# Daniel Makarov
# Date: October 30, 2021
# Going to the movies

name = input("Hello, welcome to Cinaplex! What's your name? ")

while True:
    try:
        age = int(input("Hello " + str(name) + "! How old are you? "))
        #print(age)
        if age < 0:
            print("You can't be younger than zero years old. Try inputting your age again.")
            continue
        break
    except:
        print("Sorry, there seems to be a problem with your input. Try again.")
        continue

if age < 3:
    print("Your ticket is free!")
elif age >= 3 and age <= 12:
    print("The price of your ticket is $10.00")
elif age > 12 and age < 65:
    print("The price of your ticket is $25.00")
elif age >= 65:
    print("The price of your ticket is $15.00")