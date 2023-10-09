class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
        
    def greet(self):
        print("Hello", self.name)
        
    def cry(self):
        print(f"{self.name} is a cry baby! And he's {self.age} years old.")
    
    def vote(self):
        pass
    
myPerson = Person("Jack", 20, "Lab Technician")

print(myPerson.name)
print(myPerson.age)
myPerson.greet()
myPerson.cry()
