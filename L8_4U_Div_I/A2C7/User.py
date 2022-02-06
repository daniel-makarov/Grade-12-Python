# Daniel Makarov
# Date: January 24, 2022
# A2C7, User Module

class User:
    def __init__(self, first_name=None, last_name=None, student_id=None, gender=None, fav_sport=None, fav_class=None):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.gender = gender
        self.fav_sport = fav_sport
        self.fav_class = fav_class
        self.login_attempts = 0

    def describe_user(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Gender:", self.gender)
        print("Student ID:", self.student_id)
        print("Favorite Sport:", self.fav_sport)
        print("Favorite Class:", self.fav_class)
  
    def greet_user(self):
        print("Hello", self.first_name, self.last_name + "! Good to see you!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0 