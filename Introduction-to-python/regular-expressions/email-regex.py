import re

email = "0x10x1-2067@0x10x1.0x1"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(pattern, email):
    print(email, "is a valid email address.")
else:
    print("Invalid email address.")
