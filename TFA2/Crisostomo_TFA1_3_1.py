f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
age = input("Enter your age: ")

full_name = f_name + " " + l_name
print("Full name: " , full_name)

sliced_name = f_name[0:3]
print("Sliced Name: ",sliced_name)

greeting_message = "Hello, {}! Welcome. You are {} years old."
print("Greeting Message:", greeting_message.format(sliced_name,age))