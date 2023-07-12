# regular expressions in python
import re

# pattern = re.compile('^Hello')
# result = pattern.finditer('Hello, World. Hello, John. Hello, Jane')
# for match in result:
#     print(match.start(), match.end(), match.group())

# result = pattern.sub('Hi', 'Hello, World! Hello')
# print(result)

# pattern = re.compile('\d+')
# result = pattern.findall('Here are some numbers: 42, 123, 5, 345, 546')
# print(result)

# pattern = re.compile('(Hello) (\w+)')
# result = pattern.search('Hello world!')
# print(result.group(1))
# print(result.group(2))


# simple pattern matching
# pattern = r"apple"
# text = "I have an apple and a banana."

# match = re.search(pattern, text)
# if match:
#     print("Pattern found!")
# else:
#     print("Pattern not found.")

# finding phone numbers

text = "My phone number is 254-797-321-907."
pattern = r"\d{3}-\d{3}-\d{3}-\d{3}"

match = re.search(pattern, text)
if match:
    phone_number = match.group()
    print("Phone number found:", phone_number)
else:
    print("Phone number not found.")

# finding email addresses

email = "example@example.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")
