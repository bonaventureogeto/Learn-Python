import os

file = open('words.txt', "r")

print(file)

content = file.read()

print(content)

with open("words.txt", "r") as file:
    print(file.read())

with open("something.txt", 'r') as thing:
    for i in thing:
        print(i)


lines = ["Hello", "World", "This", "Is", "A", "List"]

with open("xyz.txt", 'w') as file:
    file.writelines(lines)
    file.write(
        "Heyy, I'm an Arsenal Fan. I'm not happy with the way things are going at the club.")
    file.close()
