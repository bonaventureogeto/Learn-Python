# list

listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

listCars = ["Ford", "BMW", "Volvo"]

print(listNum[0])

print(listNum[0])

for i in listNum:
    if i % 2 == 0:
        print(i)

for i in listNum:
    print(i**2)

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

# print(car["make"])

car["color"] = "red"

# print(car)

cars = {
    "car1": {
        "make": "Ford",
        "model": "Mustang",
        "year": 1964
    },
    "car2": {
        "make": "Ford",
        "model": "Mustang",
        "year": 1963
    },
}

print(cars["car1"]["year"])

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
