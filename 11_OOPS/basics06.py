# Multi-Inheritance
class Car:
    def cardetail(self):
       return f"this is car"
    
class Battery:
    def batterydetail(self):
       return f"5000kewh"
    
class Tyre:
    @property
    def tyredetail(self):
       return f"Black"
    
class Combine(Car, Battery, Tyre):
    def detail():
        print("this is combine")

obj = Combine()
print(obj.cardetail())
print(obj.batterydetail())
print(obj.tyredetail)

def emp():
    return

print(emp())        # prints 'None'
print()             # prints blank line