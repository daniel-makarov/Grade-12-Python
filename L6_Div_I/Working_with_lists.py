# Daniel Makarov
# Date: November 22, 2021
# Working with lists

from calendar import monthrange

while True:
  try:
    year = int(input("Please enter a year: "))
  except:
    print("Please retype a valid year.")
    continue
  break

# Number of days for each month of a year
number_of_days = []

for month in range(1,13):

  # Get the weekday for the first day of the month, and the number of days in each month
  month_number = str(monthrange(year, month))
  #print(month_number)

  first_char = month_number[4]
  second_char = month_number[5]
  number_of_days.append(first_char + second_char)

#print("Months in the year:")
#print(number_of_days)

for number in range(0, len(number_of_days)):
  number_of_days[number] = int(number_of_days[number])

print()
print(number_of_days)

# Number of days for the month that I was born in
print("\nThe number of days in November (my birthday month):", str(number_of_days[10]))

# Total number of days in the year
print("\nNumber of days in the year:", sum(number_of_days))

# Number of days in each month from June to August (Summer months)
print("\nNumber of days of the month for the summer months only - June to August:")
print(number_of_days[5:8])

# Number of days for each month in the first 3 months of the year
print("\nNumber of days of the month for the first 3 months of the year:")
print(number_of_days[:3])

# Number of days for each month in the last 3 months of the year
print("\nNumber of days of the month for the last 3 months of the year:")
print(number_of_days[-3:])

# Number of days for each month in the first & last 3 months of the year
print("\nFirst & last 3 months of the year:")
print(number_of_days[:3] + number_of_days[-3:])