student_record = []
filename = "student_record.txt"

while True:
    print("\nMenu:")
    print("[1] Open File")
    print("[2] Save File")
    print("[3] Save As File")
    print("[4] Show All Students Record")
    print("[5] Order by Last Name")
    print("[6] Order by Grade")
    print("[7] Show Student Record")
    print("[8] Add Record")
    print("[9] Edit Record")
    print("[10] Delete Record")
    print("[11] Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            try:
                with open(filename, 'r') as file:
                    student_record = [eval(line.strip()) for line in file]
            except FileNotFoundError:
                print("File not found. Starting with an empty record.")
        case "2":
            with open(filename, 'w') as file:
                for record in student_record:
                    file.write(str(record) + "\n")
            print("\n[Records saved successfully]")
        case "3":
            filename = input("Enter new filename: ")
            with open(filename, 'w') as file:
                for record in student_record:
                    file.write(str(record) + "\n")
            print("\n[Records saved successfully]")
        case "4":
            for record in student_record:
                student_id, name, class_standing, major_exam = record
                final_grade = round((class_standing * 0.6) + (major_exam * 0.4), 2)
                print(f"\nID: {student_id}, \nName: {name[0]} {name[1]}, \nClass Standing: {class_standing}, \nMajor Exam: {major_exam}, \nFinal Grade: {final_grade}")
        case "5":
            student_record.sort(key=lambda x: x[1][1])
            print("Records sorted by last name:")
            for record in student_record:
                print(record)
        case "6":
            student_record.sort(key=lambda x: (x[2] * 0.6) + (x[3] * 0.4), reverse=True)
            print("Records sorted by final grade:")
            for record in student_record:
                print(record)
        case "7":
            student_id = input("Enter Student ID: ")
            for record in student_record:
                if record[0] == student_id:
                    print(record)
                    break
            else:
                print("\n[Student ID not found]")
        case "8":
            student_id = input("Enter Student ID (6 digits): ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            student_record.append((student_id, (first_name, last_name), class_standing, major_exam))
            print("\n[Record added successfully]")
        case "9":
            student_id = input("Enter Student ID to edit: ")
            for i, record in enumerate(student_record):
                if record[0] == student_id:
                    first_name = input("Enter New First Name: ")
                    last_name = input("Enter New Last Name: ")
                    class_standing = float(input("Enter New Class Standing Grade: "))
                    major_exam = float(input("Enter New Major Exam Grade: "))
                    student_record[i] = (student_id, (first_name, last_name), class_standing, major_exam)
                    print("\n[Record edit successful]")
                    break
            else:
                print("Student ID not found.")
        case "10":
            student_id = input("Enter Student ID to delete: ")
            student_record = [record for record in student_record if record[0] != student_id]
            print("\n[Record delete successful]")
        case "11":
            break
        case _:
            print("Invalid choice. Try again.")
            
            

