import re

# my_txt = 'freeCodeCamp'
# my_regex_1 = '^freecodecamp$'

# res = re.match(my_regex_1, my_txt)  # using the match() method
# print(res)  # returns None

pattern = re.compile('^Hello')

results = pattern.sub('Kenya', 'Hello World, Hello Python, Hello Regex')

print(results)

# for result in results:
#     print(result.start(), result.end(), result.group())
