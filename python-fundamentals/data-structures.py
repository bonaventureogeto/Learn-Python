# list

listName = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

listMty = []

tupleMty = ()

myTuples = (1, 2, 3, 4, 5)


listName[0] = 1000

print(len(listName))
print(len(myTuples))


# dictionary

car = {
    "make": "Ford",
    "model": "Mustang",
    "year": 1964
}

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "married": True
}

print(person)

print(person["name"])
print(person["age"])
print(person["city"])

print(person.get("city"))

person["job"] = "Developer"
print(person.keys())
print(person.values())

person.update(car)

print(person)
