'''Here's a Python code snippet that uses various operators in Python, including arithmetic, assignment,
 comparison, logical, membership, and identity operators'''

# Arithmetic operators
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)
print("Modulus:", a % b)

# Assignment operators
x = 5
x += 3
print("Assignment:", x)

# Comparison operators
print("Comparison:", a > b)
print("Comparison:", a == b)
print("Comparison:", a != b)

# Logical operators
print("Logical AND:", a > b and a < b)
print("Logical OR:", a > b or a < b)
print("Logical NOT:", not(a > b))

# Membership operators
list_example = [1, 2, 3, 4, 5]
print("Membership (in):", 2 in list_example)
print("Membership (not in):", 6 not in list_example)

# Identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("Identity (is):", x is z)
print("Identity (is not):", x is not y)
