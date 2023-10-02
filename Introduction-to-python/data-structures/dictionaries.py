# a dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

person = {
    "name": "John Doe",
    "age": 40,
    "nationality": "Kenyan",
    "occupation": "Student",
    "height": "1.69cm"
}

# print(person["height"])
# print(person.get("occupation"))

person["hobbies"] = "Hiking" # adding key-value pairs to a dictionary

del person["name"]

person["age"] = 28 #reassingment in dictionaries

# print(person.keys())
# print(person.values())

xtra_features = {"Sex": "man", "race": "Latino"}

person.update(xtra_features)
# print(person)

for property in person:
    if person[property] == "Hiking":
        print("You can hike!")
    
def personValue(value):
    for property in person:
        if person[property] == value:
            print("The value is", value)
        else:
            print("The value doesn't exist!")

personValue("kenya")

