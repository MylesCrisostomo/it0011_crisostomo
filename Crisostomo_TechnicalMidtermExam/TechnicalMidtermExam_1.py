with open("Crisostomo_TechnicalMidtermExam/numbers.txt", 'r') as data_file:
    all_lines = data_file.readlines()

current_line_number = 1

for data_line in all_lines:

    number_list = data_line.strip().split(',')

    if all(item.isdigit() for item in number_list):

        converted_numbers = [int(item) for item in number_list]

        calculated_sum = sum(converted_numbers)

        if str(calculated_sum) == str(calculated_sum)[::-1]:
            print(f"Line {current_line_number}: {data_line.strip()} (sum {calculated_sum}) - Palindrome")
        else:
            print(f"Line {current_line_number}: {data_line.strip()} (sum {calculated_sum}) - Not a palindrome")

    current_line_number += 1