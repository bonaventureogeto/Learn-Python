# name = input("Enter your name: ")

# if (name == "John"):
#     print("Hello, John!")
# elif (name == "Jade"):
#     print("Hello, Jade!")
# elif (name == "Barrack"):
#     print("You're Barrack!")
# elif (name == "Mary"):
#     print("You're Mary!")
# else:
#     print("Your name is", name)

"""
 write a simple python program that checks whether someone
 is eligible to vote or not.
"""
# age = int(input("Please, enter your age: "))

# if (age >= 18):
#     print("You're eligible to VOTE")
# else:
#     print("You can't vote!")

# height = float(input("Write you height, please: "))

# age = int(input("Write your age: "))

# print(height+age)  # 234

""" 
 write a simple program that determines whether the number input by a user
 is even or odd
"""
# number = int(input("Enter a number: "))

# if (number % 2 == 0):
#     print(number, "is even")
# else:
#     print(number, "is odd.")

"""
 write a grade anaylzer program that takes the average score from  a user
 and assigns a grade accordingly e.g 45 gets a C
"""
score = int(input("Input your average score: "))

if (score > 80 and score < 100):
    print("A")
elif (score > 70 and score <= 80):
    print("B")
elif (score > 60 and score <= 70):
    print("B")
elif (score > 50 and score <= 60):
    print("B")
elif (score > 40 and score <= 50):
    print("B")
else:
    print("Invalid score")
