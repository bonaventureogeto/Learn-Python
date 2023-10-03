import re

text = "My phone number is 123-456-7890. \n The other one is 423-466-5670"
pattern = r"\d{3}-\d{3}-\d{4}"

match = re.search(pattern, text)
if match:
    phone_number = match.group()
    print("Phone number found:", phone_number)
else:
    print("Phone number not found.")
