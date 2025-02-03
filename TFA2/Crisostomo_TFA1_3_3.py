l_name = input("Enter your last name: ")
f_name = input("Enter your first name: ")
age = input("Enter your age: ")
contact_number = input("Enter your contact number: ")
course = input("Enter your course: ")

output = "Last Name: {} \nFirst Name: {} \nAge: {}   \nContact Number: {} \nCourse: {} "
f=open("TFA2/students.txt","a+")
f.write(
    output.format(l_name,f_name,age,contact_number,course)
)
line = f.readline()
f.close()

print("\n\nStudent information has been saved to 'students.txt'")