 def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Replace '2024' with the year you want to check
year_to_check = 2024
if is_leap_year(year_to_check):
    print(year_to_check, "is a leap year.")
else:
    print(year_to_check, "is not a 
