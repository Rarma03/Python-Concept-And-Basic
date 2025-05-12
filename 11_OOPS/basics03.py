# Inheritance

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f'{self.brand} : {self.model}'
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        # super used to call the function in parent
        super().__init__(brand, model)
        self.battery = battery

    def fullnamechild(self):
        return f'{self.brand} : {self.model} : {self.battery}'


myElecCar = ElectricCar('Ola', 'ZZigy', '50000W')
# as we inherited whole Car, we can use all of its functions as well
print(myElecCar.fullname())
print(myElecCar.fullnamechild())