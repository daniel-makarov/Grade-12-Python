# Daniel Makarov
# What is your speed
# Date: October 25 2021

while True:
    try:
        distanceInKm = float(input("How far did you run in kilometers? "))
        #print("Distance Input:", distanceInKm)
        break
    except:
        print("Your distance input seems off, please try again.")

while True:
    try:
        minutes = int(input("How long was your race in minutes? "))
        #print("Minutes Input:", minutes)
        break
    except:
        print("Your race length seems off, please try again.")

while True:
    try:
        userSeconds = int(input("Seconds? "))
        #print("Seconds Input:", userSeconds)
        break
    except:
        print("Your input seems off, please try again.")


seconds = userSeconds/60
#print("Seconds:", seconds)

time_in_minutes = minutes + seconds
#print("Time in minutes:", time_in_minutes)

hours = time_in_minutes/60
#print("Hours:", hours)

kilometers_in_a_mile = distanceInKm/1.61
#print("Kilometers in a mile:", kilometers_in_a_mile)


# Average time per mile in minutes

#print("Average time per mile in minutes:", time_in_minutes/kilometers_in_a_mile)

avg_time_rounded = time_in_minutes/kilometers_in_a_mile
avg_time_rounded = "{:.2f}".format(avg_time_rounded)
print("Average time per mile in minutes:", avg_time_rounded)

# Average speed in miles per hour

#print("Average speed in miles per hour: ", kilometers_in_a_mile/hours)

avg_speed_rounded = kilometers_in_a_mile/hours
avg_speed_rounded = "{:.2f}".format(avg_speed_rounded)
print("Average speed in miles per hour:", avg_speed_rounded)