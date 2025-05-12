# polymorphism

# Base class (interface-like)
class Vehicle:
    total = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Vehicle.total+=1

    def fullname(self):
        raise NotImplementedError("Subclass must implement fullname method")

# Derived class: Car
class Car(Vehicle):
    total = 0
    def __init__(self,brand,model):
        super().__init__(brand,model)
        Car.total += 1
    def fullname(self):
        return f'Car: {self.brand} {self.model}'

# Derived class: Bike
class Bike(Vehicle):
    total = 0
    def __init__(self,brand,model):
        super().__init__(brand,model)
        Bike.total += 1
    def fullname(self):
        return f'Bike: {self.brand} {self.model}'

# Polymorphic behavior
vehicles = [
    Car('Toyota', 'Corolla'),
    Bike('Yamaha', 'R15'),
    Car('Honda', 'Civic'),
    Bike('Royal Enfield', 'Classic 350')
]

# Unified interface call
for vehicle in vehicles:
    print(vehicle.fullname())

print(f'total vehicle : {Vehicle.total}')
print(f'Car count : {Car.total} \nBike count : {Bike.total}')