# Daniel Makarov
# Date: January 24, 2022
# A2C7

from User import User
from PrivilegesAdmin import Privileges, Admin

person_1 = User("Daniel", "Makarov", "340828672", "Male", "Soccer", "Computer Science")
person_1.greet_user()
person_1.describe_user()

print()

person_2 = User("Elon", "Musk", "384938273", "Male", "Hockey", "Chemistry")
person_2.greet_user()
person_2.describe_user()

print()

person_3 = User("Tim", "Cook", "489383762", "Male", "Hockey", "Physics")
person_3.greet_user()
person_3.describe_user()

print()

person_4 = User("Veronica", "Billion", "394873763", "Female", "Hockey", "Math")
person_4.greet_user()
person_4.describe_user()

print()

person_5 = User("Richard", "Leert", "203948576", "Male", "Soccer", "English")
person_5.greet_user()
person_5.describe_user()

print()

person_6 = User("Emma", "Teller", "384758475", "Female", "Tennis", "Gym")
person_6.greet_user()
person_6.describe_user()

print()

person_7 = User("Billy", "Eroete", "485746374", "Male", "Tennis", "Spanish")
person_7.greet_user()
person_7.describe_user()

print()

person_8 = User("Alex", "Teeree", "384738475", "Male", "Soccer", "French")
person_8.greet_user()
person_8.describe_user()

print()

## A2C3 Section ##
person_9 = User("Ryan", "Baker", "283748576", "Male", "Soccer", "Computer Science")
#person_9.greet_user()
#person_9.describe_user()
for login_attempts in range(0, 7):
    #print("Login attempt number:", login_attempts)
    person_9.increment_login_attempts()

print("Incremented login attempts several times:")
print(person_9.login_attempts)

person_9.reset_login_attempts()
print()

print("Reset login attempts:")
print(person_9.login_attempts)

print()

## A2C4 Section ##
person_10 = Admin("Tim", "Brekk", "283948574", "Male", "Football", "Computer Science")
#person_10.greet_user()
#person_10.describe_user()
print("Administrative privileges for A2C4:")
person_10.show_privileges()

print()

## A2C5 Section ##
person_11 = Admin("Alexandra", "Bolarch", "485948374", "Female", "Volleyball", "Spanish")
#person_11.greet_user()
#person_11.describe_user()
print("Administrative privileges for A2C5:")
person_11_privileges = person_11.Privileges
person_11_privileges.show_privileges()

print()

## A2C6 Section ##
person_12 = Admin("Daniel", "Terrow", "384950384", "Male", "Hockey", "English")
#person_12.greet_user()
#person_12.describe_user()
print("Administrative privileges for A2C6:")
person_12.show_privileges()

print()

## A2C7 Section ##
person_13 = Admin("Mark", "Errey", "394857436", "Male", "Tennis", "French")
#person_13.greet_user()
#person_13.describe_user()
print("Administrative privileges for the A2C7:")
person_13.show_privileges()