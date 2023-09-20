def greet():
    print("Hello, Stranger!")


# greet()

# write a function called full name that prints out the full name of an individual


def fullname(firstname, lastname):
    print(firstname + " " + lastname)


fullname("Ken", "Doe")


def greetings(name):
    print("Hello", name)


greetings("Chris")

# write a function that takes in age of a person as a parameter and prints a statement about their age


def person(age):
    if (age >= 18):
        print("You can VOTE!")
    else:
        print("You cannot VOTE!")


person(14)


def sum(num1, num2):
    print(num1 + num2)


sum(34, 8)

# write a function called product that prints the product of two numbers
