print("This is my first python program!")
print(1000)

firstName = "John"
secondName = "Doe"

salary = "USD 2000"

age = "27"

name = firstName + " " + secondName + " is " + \
    age + " years old"  # concatanation


print(name)
print(salary)

form = 4

if (form < 3):
    print("You are not eligible for the captain position")

elif (form == 3):
    print("You are eligible for the deputy captain position")

else:
    print("You are eligible for the captain position")


age = 10

if age >= 18 and age < 21:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
elif age >= 16:
    print("You are old enough to drink!")
    print("Have you bought a fake ID yet?")
else:
    print("Sorry, you are too young to vote.")

# # grade = int(input("Enter your grade: "))

# # loops

for i in range(10):
    if i % 2 == 0:
        print(i, " is even")

# # while loop

k = 10

while k > 0:
    print(k)
    break

# # functions

# def sum(a, b):
#     return a + b

# print(sum(1, 2))

# # challenge
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# sum = 0
# for num in numbers:
#     if num % 2 == 0:
#        sum += num
#        print(sum)

# fubonacci sequence
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# for i in range(200):
#     print(fibonacci(i))
