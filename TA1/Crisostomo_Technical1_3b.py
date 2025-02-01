row = 1
maxRows = 5

#outer loop
while row <= maxRows: #continues to loop until all rowa are processed
    if row == 1: 
        num = 1
    elif row == 2:
        num = 3
    elif row == 3:
        num = 5
    elif row == 4:
        num = 6
    elif row == 5:
        num = 7
    
    #inner loop
    col = 1
    while col <= row: #continues to loop until all columns are processed
        print(num, end="") 
        col += 1
    print() 
    row += 1 #to go to the next row