# list

listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# print(len(listNum))

carsTuple = ("Ford", "BMW", "Volvo")

# print(len(carsTuple))

first = listNum[0]
# print(first)

element = listNum[len(listNum) - 1]
# print(element)

listNum[0] = 32

# print(listNum)

# carsTuple[0] = "Toyota"

# print(carsTuple[0])


# lists challenge:
# declare and initialize a list of people's names. the list should have at least 10 names in it.
# print the 5th person's name in the list.
# print the length of the list.
# print the last name in the list.

# for i in listNum:
#     if i % 2 == 0:
#         print(i)

# for i in range(len(listNum)):
#     print("Index " + str(i) + ":", listNum[i])

# for i in listNum:
#     print(i**2)


listNum.append("COOL")
# print(listNum)

# # listMty = []

# tupleMty = ()

# myTuples = (1, 2, 3, 4, 5)


# # listName[0] = 1000

# print(len(listNum))
# print(len(myTuples))


# sets

# kar = {"make", "Ford", "model", "Mustang", "year"}


# dictionary

car = {
    "make": "Ford",
    "model": "Model S",
    "year": 2021
}

# print(car["year"])

# car["make"] = "Tesla"

# print(car)

# # dictionary of dictionaries

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

# print(cars["car1"]["year"]["year2"])

# m_list = []
# for car in cars:
#     for k in cars[car]:
#         yr = cars[car]["year"]
#         m_list.append(yr)

# print(m_list)

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "married": True
}

# print(person)

# print(person["name"])
# print(person["age"])
# print(person["city"])

# print(person.get("age"))

# person["job"] = "Developer"
# print(person.keys())
# print(person.values())

cars.update(car)

print(cars)
