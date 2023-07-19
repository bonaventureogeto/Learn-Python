class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        
    def start(self):
        return(f"Vroom!!! The {self.year} {self.make} {self.model} has started.")
        
    def stop(self):
        return(f"Screech!!! You have used up all {self.mileage} miles on your {self.year} {self.make} {self.model}.")
        
myCar = Car("Tesla", "Model S", 2021, 100000)

print(myCar.stop())
