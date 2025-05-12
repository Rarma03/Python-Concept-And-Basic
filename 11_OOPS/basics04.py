# Defining classes and their method

# using '__' ahead of parameter in class make that attribute private
# i.e. that variable now can't be accesed outside of class
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def getter(self):
        return self.__brand
    
    def setter(self, new_brand):
        self.__brand = new_brand

# Example usage
myCar = Car('Lamborgini', 'NitroX V2.01')

# Using the getter
print(myCar.getter())

# Using the setter
myCar.setter('Ferrari')
print(myCar.getter())