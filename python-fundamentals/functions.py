def square(x):
    return x * x


square(20)


def greeting():
    print("Hello, World!")


greeting()


def numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)


numbers(10000)

# challenge 1: grading program
# write a function that takes in the score of a student and returns/prints the grade of the student

# challenge 2: prime numbers
# write a function that prints all prime numbers between 1 and n


def prime(n):
    for i in range(1, n + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
                else:
                    print(i)


prime(50)
