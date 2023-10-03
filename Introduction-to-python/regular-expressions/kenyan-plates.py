# write a regular expression pattern for a Kenyan
# car number plate (KAZ 298 F)

# \w - matches any word character (a-z, A-Z, 0-9, _)
# \s - matches any whitespace character

import re

def matchPlate(text, pattern):
    result = re.match(pattern, text)
    print(result)

text = "KCD 376 Q"
pattern = r"^[A-Z]{3}\s\d{3}\s[A-Z]{1}$"

matchPlate(text, pattern)
