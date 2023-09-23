# introduction to function
def greet():
    print("Hello, Stranger!")


# greet()

# write a function called full name that prints out the full name of an individual


def fullname(firstname, lastname):
    print(firstname + " " + lastname)


# fullname("Ken", "Doe")

# square of a number
def multiply(a, b):
    return a * b


# print(multiply(134, 3))

def greetings(name):
    print("Hello", name)


# greetings("John Doe")

"""
 write a grade anaylzer function that takes the average score from a user
 and assigns a grade accordingly e.g 45 gets a C
"""

# write a function that takes in age of a person as a parameter and prints a statement about their age


def person(age):
    if (age >= 18):
        print("You can VOTE!")
    else:
        print("You cannot VOTE!")


# person(14)


def sum(num1, num2):  # a function that takes in two parameters
    print(num1 + num2)


# sum(34, 8)

# write a function called product that prints the product of two numbers


def product(num1, num2):
    print(num1 * num2)


# product(129, 80)

# write a function that calculates the area and perimemter of a rectangle
