#strings

print("Hello, World!")

print('Hello, Kenya!')

num = 490

# str()

number = (str(num))
print(number + number) 

# indexing 

greetings = " Good morning, Kenya! I  am your friend from Italy "

print(greetings[0])
print(greetings[-1])

# methods

print(greetings.replace("Kenya", "Chris"))

list_greet = greetings.split(" ")

print(list_greet)

# for i in list_greet:
#     print(i)

print("-".join(list_greet))

print(greetings.strip())

print(greetings.lower())

print(greetings.upper())

