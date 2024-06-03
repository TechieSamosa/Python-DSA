#Leap year checker
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return "Year is a Leap Year"
    elif  year % 400 == 0:
        return "Year is a Leap Year"
    else:
        return "Year is NOT a Leap Year"

year = int(input("Enter year: "))
print(is_leap_year(year))
