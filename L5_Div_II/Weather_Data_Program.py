# Daniel Makarov
# Date: December 15, 2021
# Weather Data

import calendar

def find_data(file, date):
    
    ### Find and return the line containing weather data for the chosen date. ###

    with open(file, "r") as file_text:
        for date_data_info in file_text:
            if date in date_data_info:
                return date_data_info


while True:
    data_file = input("Enter the name of the data file: ")
    data_file = (data_file + ".txt")
    
    if data_file != "DataFile1.txt":
        print("This file does not exist. Try again.")
        continue

    #print("File:", data_file)
    break

while True:
    while True:
        try:
            day = int(input("For the date you care about, enter the day: "))
        except:
            print("There seems to be a problem with your input. Try again.")
            continue
        
        if day>=32 or day<=0:
            print("It is not possible to have this day number in a month. Try again.")
            continue

        day = str(day)
        # Appends a 0 to a number that is one digit long
        day = day.zfill(2)
        
        #print("Day chosen:", day)
        break

    while True:
        try:
            month = int(input("For the date you care about, enter the month: "))
        except:
            print("There seems to be a problem with your input. Try again.")
            continue
        
        if month>12 or month<=0:
            print("It is not possible to have this month number in a year. Try again.")
            continue

        # Converts month's integer to the abbreviation of the month's name
        month = str(calendar.month_abbr[month])
        
        #print("Month chosen:", month)
        break

    while True:
        try:
            year = int(input("For the date you care about, enter the year: "))
        except:
            print("There seems to be a problem with your input. Try again.")
            continue

        year = str(year)
        year = year[-2:]
        
        #print("Year chosen:", year)
        break

    full_date = (day + "-" + month + "-" + year)
    #print(full_date)

    date_data = find_data(data_file, full_date)
    
    if (date_data is None):
        print("There is no data regarding your chosen date.")
        print()
        continue

    #print("Information Regarding Chosen Date:", date_data)

    date_data_info_list = date_data.split(",")
    
    #print(date_data_info_list)

    print("The low temperature was", date_data_info_list[1], "degrees Celsius")
    print("The high temperature was", date_data_info_list[2], "degrees Celsius")
    print("The average temperature was", date_data_info_list[3], "degrees Celsius")
    print()
    continue