# challenge: prime numbers
# write a program that prints all prime numbers between 1 and 100

# prime numbers are numbers that are only divisible by 1 and itself
for i in range(1, 101):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
