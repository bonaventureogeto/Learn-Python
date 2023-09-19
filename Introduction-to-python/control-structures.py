name = input("Enter your name: ")

if (name == "John"):
    print("Hello, John!")
elif (name == "Jade"):
    print("Hello, Jade!")
elif (name == "Barrack"):
    print("You're Barrack!")
elif (name == "Mary"):
    print("You're Mary!")
else:
    print("Your name is", name)

"""
 write a simple python program that checks whether someone
 is eligible to vote or not.
"""
age = int(input("Please, enter your age: "))

if (age >= 18):
    print("You're eligible to VOTE")
else:
    print("You can't vote!")
