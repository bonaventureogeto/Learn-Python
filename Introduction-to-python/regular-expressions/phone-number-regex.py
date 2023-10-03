import re

text = "My phone number is +254-724-324-678."
pattern = r"[+]\d{3}-\d{3}-\d{3}-\d{3}"

match = re.search(pattern, text)
if match:
    phone_number = match.group()
    print("Phone number found:", phone_number)
else:
    print("Phone number not found.")
