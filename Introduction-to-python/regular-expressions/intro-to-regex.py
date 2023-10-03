import re

pattern = re.compile("^Hello")

# result = pattern.search("world Hello, world!");

# result = pattern.findall("Hello, world! Hello");
result = pattern.finditer("Hello, world! Hello");

for match in result:
    print(match.start(), match.end(), match.group())

# print(result);
