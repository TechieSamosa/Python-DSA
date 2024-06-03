def type_of_triangle(a, b, c):
    if a == b == c:
        return "The triangle is an 'Equilatral Triangle'."
    elif a == b or a == c or b == c:
        return "The triangle is an 'Isosceles Triangle'."
    else:
        return "The triangle is Scaline"
    
#Driver Code
side1 = int(input("Enter the 1st side:"))
side2 = int(input("Enter the 2st side:"))
side3 = int(input("Enter the 3st side:"))
print(type_of_triangle(side1, side2, side3))
