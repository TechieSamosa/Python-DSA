# Define a class named 'Car'
class Car:
    # Constructor method to initialize the object with attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # Method to describe the car
    def describe_car(self):
        return f"{self.year} {self.make} {self.model}"

    # Method to read the odometer
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."

    # Method to update the odometer reading
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes and methods of the object
print(my_car.describe_car())
print(my_car.read_odometer())

# Update the odometer reading
my_car.update_odometer(15000)
print(my_car.read_odometer())