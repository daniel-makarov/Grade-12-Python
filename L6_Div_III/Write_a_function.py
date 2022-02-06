# Daniel Makarov
# Date: December 17, 2021
# Write a function

def word_num_of_char(word, letter):
  ### Counts the number of occurences of a chosen character in a word. ###
  num_of_char = 0

  word = list(word)

  #print("Word in list form:", word)

  for characters in word:
    #print(characters)
    if letter == characters:
      num_of_char += 1
      
  return num_of_char

user_word = input("Enter a word: ").lower()

while True:
  user_letter = input("Enter a letter: ")
  try:
    user_letter = int(user_letter)
    print("Please enter a letter")
    continue
  except:
    user_letter = user_letter.lower()
    break

num_of_found_char = (word_num_of_char(user_word, user_letter))
print(num_of_found_char)
