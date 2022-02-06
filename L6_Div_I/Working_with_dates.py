# Daniel Makarov
# Date: November 22, 2021
# Working With Dates

# Contains the date
Month = []
Day = []
Year = []

US_date = "09/30/2021"

Month.append(US_date[0])
Month.append(US_date[1])
Month = ''.join(Month)
#print(type(Month))
#print("Month:", Month)

Day.append(US_date[3])
Day.append(US_date[4])
Day = ''.join(Day)
#print(type(Day))
#print("Day:", Day)

Year.append(US_date[6])
Year.append(US_date[7])
Year.append(US_date[8])
Year.append(US_date[9])
Year = ''.join(Year)
#print(type(Year))
#print("Year:", Year)

Canadian_date = Year + "-" + Month + "-" + Day
print(Canadian_date)