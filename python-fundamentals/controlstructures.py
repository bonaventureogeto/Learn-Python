# if, elif, else statements

age = 122
if age >= 18 and age <= 120:
    print("You are an adult, you can drink, and vote")
elif age <= 0:
    print("Invalid age, TRY AGAIN!!")
elif age > 120:
    print("FOSSIL ALERT!!!")
else:
    print("You are a child, you can't drink, and vote")


# for loops
for i in range(1, 101):
    if i % 2 == 1:
        print(i)

# challenge: use a for loop and if statements
# write a program that autogrades student scores between 1 and 100
