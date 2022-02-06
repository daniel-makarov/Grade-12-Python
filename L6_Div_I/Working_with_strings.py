# Daniel Makarov
# Date: November 22, 2021
# Working with strings

#### First Program ####
print("---First Program---")
TSSPhoneNum = "905-889-9696"

FirstChar = TSSPhoneNum[0]
#print("First character:", FirstChar)
SecondChar = TSSPhoneNum[1]
#print("Second character:", SecondChar)
ThirdChar = TSSPhoneNum[2]
#print("Third character:", ThirdChar)

AreaCode = (FirstChar + SecondChar + ThirdChar)

print("Area Code:", AreaCode)
print()

#### Second Program ####
print("---Second Program---")
TSSAddress = "8075 Bayview Ave. Thornhill, ON L3T 4N4"

# Length of characters for the city
CityCharLength = 9

City = TSSAddress[18:18+CityCharLength]

print("City:", City)