# Daniel Makarov
# Date: November 22, 2021
# Desiderata

# Read file
with open('ICS4UDesiderata.txt') as file_object:
    text_file = file_object.read()
    
#print("Text File:")
#print(text_file)

text_file = text_file.replace("<p>","\n\n")
text_file = text_file.replace("<l>","\n")

print(text_file)

# Creates and saves text in a .txt file
with open('DanielMakarovDesiderata.txt', 'w') as f:
    f.write(text_file)
