# Daniel Makarov
# Date: January 24, 2022
# A2C7, Privileges and Admin Module

from User import User

class Privileges:
    privileges = ["can add post", "can delete post", "can ban user", "can add user"]
    
    def show_privileges(self):
        print(*(self.privileges), sep="\n")

class Admin(User):
    privileges = ["can add post", "can delete post", "can ban user", "can add user"]

    def show_privileges(self):
        print(*(self.privileges), sep="\n")

    Privileges = Privileges()