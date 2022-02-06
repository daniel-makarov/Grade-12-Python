# Daniel Makarov
# Date: October 25, 2021
# What is my time?

# Left home at 6:52 a.m.
time_left_home = 6 + 52/60

# 1 km at an easy pace (8:15 per km)
easy_pace_time = 8.25

# Run 3 km at tempo (7:12 per km)
tempo_time = 3*(7.2)

# Running time in minutes
run_time = 2*(easy_pace_time) + tempo_time
#print("Total Time Spent Running:", run_time, "minutes.")

# Running time in hours
run_time = run_time/60
#print("Total Time Spent Running:", run_time, "hours.")

time_came_home = run_time + time_left_home

#print("Time came home (decimals):", time_came_home)

time_came_home_hours = time_came_home
time_came_home_minutes = (time_came_home*60) % 60
print("Time came home: %d:%02d a.m." % (time_came_home_hours, time_came_home_minutes))