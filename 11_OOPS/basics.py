# Defining classes and their constructor usecases

class Car:
    brand = None
    model = None

    def __init__(userbrand, usermodel):
        brand = userbrand
        model = usermodel

    # self in python = this in java
    # self is help to set the connection between class and its objects
    # best practice to use below
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# __init__ is the constructor of class

my_car = Car('Ferrari', 'GTx10')
print(my_car.brand, my_car.model)