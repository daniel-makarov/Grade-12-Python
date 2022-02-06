# Daniel Makarov
# October 30, 2021
# Measuring Cholesterol

while True:
  try:
    LDL = int(input("What is your LDL: "))
    break
  except:
    print("Something is wrong with your input. Please try again.")
    continue

#print("LDL:", LDL)

while True:
  try:
    HDL = int(input("What is your HDL: "))
    break
  except:
    print("Something is wrong with your input. Please try again.")
    continue

#print("HDL level:", HDL)

while True:
  try:
    TRI = int(input("What is your TRI: "))
    break
  except:
    print("Something is wrong with your input. Please try again.")
    continue

#print("TRI:", TRI)

Total = LDL + HDL + TRI*0.2
#print("Total:", Total)

if LDL<100 and HDL>60 and TRI<150 and Total<200:
  print("Cholesterol looks great!")
elif LDL>130 or HDL<50 or TRI>200 or Total>240:
  print("Cholesterol looks bad!")
else:
  print("Borderline cholesterol problems.")