stringInput = input("Enter a String: ")

sum = 0

for char in stringInput:
    if char.isnumeric():
        sum += int(char)
        
print("====================================================")
print("Sum of all digits is: " , sum)