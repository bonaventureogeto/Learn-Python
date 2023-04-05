class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(
            f"Starting the {self.make} {self.model} engine! About to go 0-100MPH in 3.2 seconds!")

    def stop(self):
        print(f"Stopping the {self.make} {self.model} engine!")

    def drive(self):
        print(f"Driving the {self.make} {self.model} at 180MPH!")


myCar = Car("Mazda", "CX5", 2018)

myCar.start()
myCar.stop()
myCar.drive()
