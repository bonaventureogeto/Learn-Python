import re

phonePattern = r"\d{3}[-.\s]\d{3}[-.\s]\d{4}[-.\s]"

emailPattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

string = "Please contact info@example.com for assistance. Phone:123 456-7890 or 111 222-3333 "


# def extract_phone_numbers(string):
#     match = re.search(phonePattern, string)
#     if match:
#         phoneNumbers = match.group()
#         return phoneNumbers
#     else:
#         return 'No Phone Number Found'


def extract_email_addresses():
    match = re.findall(emailPattern, string)
    return match


def replace_email_addresses(string, replacement):
    replace = re.sub(emailPattern, replacement, string)
    return replace


# string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"
# print(extract_phone_numbers(string))
print(extract_email_addresses())
# print(replace_email_addresses(string, "REPLACED"))
