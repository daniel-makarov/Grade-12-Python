# Daniel Makarov
# Date: January 24, 2022
# A2C2

class User:
    def __init__(self, first_name=None, last_name=None, student_id=None, gender=None, fav_sport=None, fav_class=None):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.gender = gender
        self.fav_sport = fav_sport
        self.fav_class = fav_class

    def describe_user(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Gender:", self.gender)
        print("Student ID:", self.student_id)
        print("Favorite Sport:", self.fav_sport)
        print("Favorite Class:", self.fav_class)
  
    def greet_user(self):
        print("Hello", self.first_name, self.last_name + "! Good to see you!")
        
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