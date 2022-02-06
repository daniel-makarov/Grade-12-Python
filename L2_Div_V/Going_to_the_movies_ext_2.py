# Daniel Makarov
# Date: October 30
# Going to the movies, Extention 2

name = input("Hello, welcome to Cinaplex! What's your name? ")

while True:
    try:
        age = int(input("How old are you? "))
        #print("Age:", age)
        if age < 0:
            print("You can't be younger than zero years old. Try inputting your age again.")
            continue
        break
    except:
        print("Sorry, something seems wrong with your age.")
        continue

print("Hello", str(name) + "!")

while True:
    try:
        age_under_3 = int(input("How many tickets for kids under 3 years old? "))
        if age_under_3 < 0:
            print("Please choose zero tickets or more.")
            continue
        break
    except:
        print("Sorry, there seems to be a problem with your input. Try again.")
        continue

while True:
    try:
        age_under_12 = int(input("How many tickets for kids under 12 years old? "))
        if age_under_12 < 0:
            print("Please choose zero tickets or more.")
            continue
        break
    except:
        print("Sorry, there seems to be a problem with your input. Try again.")
        continue

while True:
    try:
        age_senior = int(input("How many tickets for Seniors? "))
        if age_senior < 0:
            print("Please choose zero tickets or more.")
            continue
        break
    except:
        print("Sorry, there seems to be a problem with your input. Try again.")
        continue

while True:
    try:
        age_adult = int(input("How many tickets for Adults? "))
        if age_adult < 0:
            print("Please choose zero tickets or more.")
            continue
        break
    except:
        print("Sorry, there seems to be a problem with your input. Try again.")
        continue

#print("Age 3:", age_under_3)
#print("Age 12:", age_under_12)
#print("Senior:", age_senior)
#print("Adult:", age_adult)

cost_age_under_3 = age_under_3*0
cost_age_under_12 = age_under_12*10
cost_age_senior = age_senior*15
cost_age_adult = age_adult*25

#print("Cost for those aged 3:", cost_age_under_3)
#print("Cost for those aged 12:", cost_age_under_12)
#print("Cost for Seniors:", cost_age_senior)
#print("Cost for Adults:", cost_age_adult)

final_cost = cost_age_under_3 + cost_age_under_12 + cost_age_senior + cost_age_adult
final_cost = "{:.2f}".format(final_cost)
print("Please pay $" + str(final_cost))