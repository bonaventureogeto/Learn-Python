# challenge: open the names.txt file in read mode. and append all the names to a list

# names = []

# with open("names.txt", "r") as file:
#     for name in file:
#         names.append(name.strip())

# print(names)

with open("example.txt", "w") as file:
    file.write(
        "To write to a file, you must open it in write mode or append mode.")
