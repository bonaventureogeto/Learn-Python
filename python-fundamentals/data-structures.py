# list

listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(len(listNum))

carsTuple = ("Ford", "BMW", "Volvo")

print(len(carsTuple))

listNum[10] = 3264

print(listNum[10])


# carsTuple[0] = "Toyota"

print(carsTuple[0])

for i in listNum:
    if i % 2 == 0:
        print(i)

for i in listNum:
    print(i**2)


listNum.append("COOL")
print(listNum)

# listMty = []

tupleMty = ()

myTuples = (1, 2, 3, 4, 5)


# listName[0] = 1000

print(len(listNum))
print(len(myTuples))

# sets

kar = {"make", "Ford", "model", "Mustang", "year"}


# # dictionary

car = {
    "make": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car["make"])

car["color"] = "red"

# print(car)

# dictionary of dictionaries

cars = {
    "car1": {
        "make": "Tesla",
        "model": "Plaid",
        "year": {
            "year1": 2021,
            "year2": 2022
        }
    },
    "car2": {
        "make": "Ford",
        "model": "Mustang",
        "year": 1963
    },
}

print(cars["car1"]["make"])

m = []
for car in cars:
    print(cars[car]["make"])
    for k in cars[car]:
        yr = cars[car]["year"]
        m.append(yr)

print(m)

# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "married": True
# }

# print(person)

# print(person["name"])
# print(person["age"])
# print(person["city"])

# print(person.get("city"))

# person["job"] = "Developer"
# print(person.keys())
# print(person.values())

# person.update(car)

# print(person)
