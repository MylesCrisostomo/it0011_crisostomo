month_names = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

date_string = input("Provide the date in the format mm/dd/yyyy (e.g., 02/07/2025): ")

month_part, day_part, year_part = date_string.split('/')

month_full_name = month_names.get(month_part, "Invalid Month")

formatted_date = f"{month_full_name} {int(day_part)}, {year_part}"

print("Formatted Date: ", formatted_date)