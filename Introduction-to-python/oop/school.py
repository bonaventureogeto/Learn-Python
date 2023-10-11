"""
    Create a School class with atleast 3 properties, 
    then create a child class that inherits the properties of the School class
"""

class School:
    def __init__(self, name, population, location):
        self.name = name
        self.population = population
        self.location = location
        
class University(School):
    def __init__(self, name, population, location):
        super().__init__(name, population, location)

myUniversity = University('UoN', 30000, 'Nairobi')

print(myUniversity.name)
