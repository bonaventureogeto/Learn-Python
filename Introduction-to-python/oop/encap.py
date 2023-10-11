class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

my_car = Car("Toyota", "Camry", 2020)
print(my_car._Car__make) # "Toyota"

print(my_car.make)
