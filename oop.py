# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def start(self):
#         print(
#             f"Starting the {self.make} {self.model} engine! About to go 0-100MPH in 3.2 seconds!")

#     def stop(self):
#         print(f"Stopping the {self.make} {self.model} engine!")

#     def drive(self):
#         print(f"Driving the {self.make} {self.model} at 180MPH!")


# myCar = Car("Mazda", "CX5", 2018)

# myCar.start()
# myCar.stop()
# myCar.drive()


# class Person:
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height

#     def who(self):
#         print(
#             f"My name is {self.name} and I'm {self.age} years old and {self.height}cm tall.")

#     def sleep(self):
#         print("John is sleeping soundly...")


# myPerson = Person("John", 25, 180)

# myPerson.sleep()


# class MiniPerson(Person):
#     def __init__(self, name, age, height):
#         super().__init__(name, age, height)

#     def sleep(self):
#         print(f"{self.name} is sleeping soundly...")


# myMiniPerson = MiniPerson("Grace", 55, 120)

# myMiniPerson.sleep()


# bank

class BankAccount:
    def __init__(self, name, balance):
        self.name = name  # this(self)
        self.balance = balance

    def check_balance(self):
        print(f"Hey {self.name}, Your current balance is ${self.balance}.")

    def deposit(self, amount):
        self.balance += amount
        print(f"Hey {self.name}, Your current balance is ${self.balance}.")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Hey {self.name}, Your current balance is ${self.balance}.")

    def appreciation(self):
        print(
            f"Thank you for banking with The Bank of Scotland! You are a valued customer!")


myBank = BankAccount("Ogah", 89500)

myBank.check_balance()
myBank.deposit(5000)
myBank.withdraw(10000)
myBank.appreciation()
