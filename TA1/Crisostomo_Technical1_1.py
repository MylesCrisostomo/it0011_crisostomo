vowel = 0
consonant = 0
space = 0
digit = 0
specChar = 0

stringInput = input("Enter a string: ")
vowelIs = set("aeiouAEIOU")

for char in stringInput:
    if char in vowelIs:
        vowel += 1
    elif char.isalpha(): #check if it is an alphabet
        consonant +=1
    elif char.isspace(): #checks if it is a space
        space += 1
    elif char.isnumeric(): #checks if it is a number
        digit += 1
    else: #checks if it is a special character
        specChar += 1

print("====================================================")
print("Vowels: \t" , vowel , "\nConsonants: \t" , consonant ,
      "\nSpaces: \t" , space , "\nDigit: \t\t", digit , "\nOthers: \t" , specChar)


