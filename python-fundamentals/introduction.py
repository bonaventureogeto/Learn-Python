# age = 20

# if age >= 18 and age < 21:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# elif age >= 16:
#     print("You are old enough to drive!")
#     print("Have you registered to vote yet?")
# else :
#     print("Sorry, you are too young to vote.")
    
# # grade = int(input("Enter your grade: "))

# # loops

# for i in range(10):
#     print(i)
    
# # while loop

# while True:
#     print("Hello")
#     break

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
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
for i in range(200):
    print(fibonacci(i))