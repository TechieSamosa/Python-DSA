# Creating a list of fruits
fruits = ["apple", "banana", "cherry"]

# Accessing elements of the list
print("First fruit:", fruits[0])  # Prints the first fruit in the list
print("All fruits:", fruits)      # Prints all fruits in the list

# Modifying elements of the list
fruits[1] = "orange"              # Changes the second fruit to "orange"
print("Modified fruits:", fruits) # Prints the modified list of fruits

# Adding elements to the list
fruits.append("kiwi")             # Adds "kiwi" to the end of the list
print("Fruits with kiwi:", fruits) # Prints the updated list of fruits

# Removing elements from the list
removed_fruit = fruits.pop(2)     # Removes and returns the third fruit ("cherry")
print("Removed fruit:", removed_fruit)
print("Remaining fruits:", fruits)

# Creating a dictionary of car details
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Accessing values in the dictionary
print("Car brand:", car["brand"]) # Prints the brand of the car
print("Car details:", car)        # Prints all details of the car

# Modifying values in the dictionary
car["year"] = 2020                # Changes the year of the car to 2020
print("Modified car details:", car)

# Adding new key-value pairs to the dictionary
car["color"] = "red"              # Adds the color of the car
print("Car details with color:", car)

# Removing key-value pairs from the dictionary
removed_model = car.pop("model")  # Removes and returns the model of the car
print("Removed model:", removed_model)
print("Remaining car details:", car)

'''Lists:
Lists are ordered collections of items in Python.
Accessing elements: Use square brackets [] with the index of the element to
access it (indexing starts at 0).
Modifying elements: Assign a new value to the desired index.
Adding elements: Use the append() method to add an element to the end of the list.
Removing elements: Use the pop() method with the index of the element to remove it
(removes and returns the element).


Dictionaries:
Dictionaries are unordered collections of key-value pairs in Python.
Accessing values: Use square brackets [] with the key to access the value.
Modifying values: Assign a new value to the desired key.
Adding key-value pairs: Simply assign a value to a new key.
Removing key-value pairs: Use the pop() method with the key to remove the key-value
pair (removes and returns the value).'''