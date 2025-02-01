rows = 5 #number of rows, also used for max numbers of loop

#outer loop
for i in range(1, rows + 1):
    #spaces for aligning on right
    for space in range(rows - i):  #for calculating right spaces for the aligning on right
        print(" ", end="")
    
    #inner loop
    for j in range(1, i + 1):
        print(j, end="") 
    
    print()  
    
    
