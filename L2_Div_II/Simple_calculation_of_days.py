# Daniel Makarov
# Simple Calculation Number of Days
# Date: October 25 2021

days = 7

while True:
    try:
        weeks = int(input("Enter a number of weeks: "))
        #print("Number of weeks:", weeks)
        break
    except:
        print("Something seems wrong, please try again.")

print(weeks, "weeks equals", weeks*days, "days.")