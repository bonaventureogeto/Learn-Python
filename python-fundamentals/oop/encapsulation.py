# encapsulation is the concept of information hiding
class Car:
    def __init__(self, make, model, year):
        self._make = make
        self.__model = model
        self.__year = year
        
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

myCar = Car("Tesla", "Model S", 2021)

print(myCar._make)