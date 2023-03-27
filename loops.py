# while loop
# booleans - True or false

while True:
    print("I love cars")
    break

# syntax:
"""
    while expression:
        statements
"""

num = 10

while num < 5:
    print("Less than 5")
else:
    print("Greater than 5")


num = 0

while (num < 10):
    num = num + 1
    print(num)
    print("I love cars")


# for loops

num = 20

for i in range(0, num):
    if (i % 2 == 0):
        print(i, " is even")
    else:
        print(i, " is odd")
