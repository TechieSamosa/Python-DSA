#this is a Python program that takes a person's age as input and categorizes them as an infant (0-1 years), child (2-12 years), teenager (13-19 years), adult (20-64 years), or senior (65+ years). Print the appropriate category based on the age.
def age_calculator(age):

    if age>=65:
        return "Senior"
    elif age>=20 and age < 65:
        return "Adult"
    elif age>= 13 and age < 20:
        return "Teenager"
    elif age>=2 and age < 13:
        return "Child"
    elif age<2:
        return "Infant"
    else:
        return "There is some kind of error"
    
#DriverCode
num = int(input("Enter the age:"))
print(age_calculator(num))