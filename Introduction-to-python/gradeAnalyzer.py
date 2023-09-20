score = int(input("Enter your score: "))

if (score > 80 and score < 100):
    print("Grade: A")
elif (score > 70 and score <= 80):
    print("Grade: B")
elif (score > 60 and score <= 70):
    print("Grade: C")
elif (score > 50 and score <= 60):
    print("Grade: D")
elif (score > 40 and score <= 50):
    print("Grade: E")
elif (score > 0 and score <= 40):
    print("Grade: F")
else:
    print("Invalid SCORE")
