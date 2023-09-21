# while loops
# boolean - true, false

# while True:
#     print("Hello, World!")
#     break

number = 22

# print(number < 20)

while (number < 20):
    print("This number is less than 20")


# for loop
# for i in range(2, 50):
#     print(i)

# write a for loop that prints number between 0 and 100
# for num in range(0, 100):
#     if (num % 2 == 0):
#         print(num, "is even!")

# for num in range(0, 50, 2):
#     print(num, "is even")

# write a python program that prints odd numbers between 0 and 20
# for number in range(79, 234):
#     if (number % 2 == 1):
#         print(number, "is ODD!")


# write a python program that prints all the multiples of 7 between 0 and 1000
# for num in range(0, 1000, 7):
#     print(num, "is a multiple of 7!")

def evenNumbers(n):
    for i in range(n):
        if (i % 2 == 0):
            print(i, "is even!")


evenNumbers(200)
