# Daniel Makarov
# Date: December 10, 2021
# Login Program

def error():
  ### Displays error message if username or password is incorrect. ###
  print("Username or Password is incorrect, please try again.")

teachassist = {
  "Makarov":340828672,
  "Etwaroo":123456789,
  "Foti":987654321,
  "Papadatos":543219876,
  "Tremblay":9058899696
}

#print("List of students & teachers:", teachassist)

# Counts the amount of times the user fails to login.
num_of_incorrect_login = 0

verified_flag = False

while True:
  username = input("Please enter username: ")
  #print("Username:", username)

  try:
    password = int(input("Please enter password: "))
  except:
    num_of_incorrect_login += 1
    if num_of_incorrect_login == 3:
      print("Username or Password is incorrect. You tried to log in 3 times. You are barred from logging in again.")
      break
    error()
    continue  
  #print("Password:", password)

  try:
    correct_password = (teachassist[username])
  except:
    num_of_incorrect_login += 1
    if num_of_incorrect_login == 3:
      print("Username or Password is incorrect. You tried to log in 3 times. You are barred from logging in again.")
      break
    error()
    continue

  if password == correct_password:
    print("Welcome!")
    verified_flag = True
    break
  else:
    num_of_incorrect_login += 1
    if num_of_incorrect_login == 3:
      print("Username or Password is incorrect. You tried to log in 3 times. You are barred from logging in again.")
      break
    error()
    continue