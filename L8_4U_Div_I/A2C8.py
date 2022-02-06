# Daniel Makarov
# Date: January 24, 2022
# A2C8

import random

class Die:
    owner = "Daniel Makarov"
    sides = 6

    def greet_owner(self):
        print("Hello", self.owner + "! Good to see you!")
    
    def roll_die(self):
        print(random.randint(1,(self.sides)))

class six_sided_die(Die):
    pass

class ten_sided_die(Die):
    sides = 10

class twenty_sided_die(Die):
    sides = 20

die = Die()
die.greet_owner()
print("Die rolled:")
die.roll_die()

print()

# Six sided die rolled
six_s_die = six_sided_die()
#six_s_die.greet_owner()
print("Six sided die rolled 10 times:")
for rolls in range(0,10):
    #print("Roll number:", rolls)
    six_s_die.roll_die()

print()

# Ten sided die rolled
ten_s_die = ten_sided_die()
#ten_s_die.greet_owner()
print("Ten sided die rolled 10 times:")
for rolls in range(0,10):
    #print("Roll number:", rolls)
    ten_s_die.roll_die()

print()

# Twenty sided die rolled
twenty_s_die = twenty_sided_die()
#twenty_s_die.greet_owner()
print("Twenty sided die rolled 10 times:")
for rolls in range(0,10):
    #print("Roll number:", rolls)
    twenty_s_die.roll_die()