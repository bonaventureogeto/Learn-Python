"""
    Using oop concepts we've learned in class
    Write a python class that represents a country.
        1. Add atleast 3 attributes
        2. Have atleast 2 methods that perform various
            tasks in a country
        3. Happy Coding!
"""

class Country:
    def __init__(self, name, continent, population):
        self.name = name
        self.continent = continent
        self.population = population
        
    def welcome(self):
        print(f'Welcome to {self.name}. We have a population of a little over {self.population} people')
    
    def region(self):
        print(f"{self.name} is located in {self.continent}")

name = input("Enter the country: ")
myCountry = Country(name, "Africa", "55 Million")

myCountry.welcome()
myCountry.region()