# Defining classes and their method

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f'{self.brand} : {self.model}'

myCar = Car('Lamborgini', 'NitroX V2.01')
print(myCar.fullname())