# regular expressions in python
import re

pattern = re.compile('^Hello')
result = pattern.match('Hello World')
print(result)
