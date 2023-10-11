class Person:
    def __init__(self, name, age, occupation, country, race):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.country = country
        self.race = race
        
    def greet(self):
        print("Hello", self.name)
        
    def cry(self):
        print(f"{self.name} is a cry baby! And he's {self.age} years old.")
    
    def vote(self):
        pass
    
myPerson = Person("Jack", 20, "Lab Technician", 'Kenya', 'Indian')

print(myPerson.name)
print(myPerson.age)
myPerson.greet()
myPerson.cry()

class Child(Person):
    def __init__(self, name, age, occupation, country, race, age1, firstname):
        Person.__init__(self, name, age, occupation, country, race)
        self.age1 = age1
        self.firstname = firstname
        
    def hello(self):
        print(f'My name is {self.name}, I am from {self.country}')
        
myChild = Child("Jack", 20, "Lab Technician", 'Kenya', 'Indian', 20, 'John')

print(myChild)

print(myChild.hello())
