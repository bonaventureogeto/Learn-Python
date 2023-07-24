# user defined polymorphic functions
# A simple Python function to demonstrate
# Polymorphism

# def add(x, y, z = 0):
# 	return x + y+z

# # Driver code
# print(add(2, 3))
# print(add(2, 3, 30))

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        
    def start(self):
        return(f"Vroom!!! The {self.year} {self.make} {self.model} has started.")
    
    def energize(self):
        return(f"Your {self.year} {self.make} {self.model} has been fueled/charged.")
        
    def stop(self):
        return(f"Screech!!! You have used up all {self.mileage} miles on your {self.year} {self.make} {self.model}.")
        
# myCar = Car("Tesla", "Model S", 2021, 100000)
# print(myCar.start())


# inheritance

class ElectricCar(Car):
    def __init__(self, make, model, year, mileage, batterySize):
        super().__init__(make, model, year, mileage)
        self.batterySize = batterySize
        
    def charge(self):
        return(f"Your {self.year} {self.make} {self.model} has been charged.")
    
    # polymorphism
    def energize(self):
        return(f"Your {self.year} {self.make} {self.model} has been charged.")
    
myElectricCar = ElectricCar("Tesla", "Model S", 2021, 100000, 100)

print(myElectricCar.energize())

