import re

my_txt = 'freeCodeCamp'
my_regex_1 = '^freecodecamp$'

res = re.match(my_regex_1, my_txt)  # using the match() method
print(res)  # returns None
