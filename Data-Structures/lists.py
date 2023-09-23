number = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list
names = ["John", "Doe", "Jack", "Jude", "Jake", "June"]

mixed = [1, 2, "Three", "Four", 5, 6, "Seven", True, False]

arr = [[1, 2, 3, 5], ["Ken", "Food", "Car"]]

print(number[7])  # O(1)

for i in arr:  # O(n^3)
    for j in i:
        print(j)
