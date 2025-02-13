f=open("TFA2/students.txt","r")
while True:
    try:
        line = next(f)
        print(line)
    except StopIteration:
        break
f.close()