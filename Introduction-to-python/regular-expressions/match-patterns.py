import re

def matchPattern(pattern, text):
    match = re.search(pattern, text)
    if match:
        print("Pattern is", pattern)
    else:
        print("Pattern not found.")
        
matchPattern("have", "I have an apple and a banana.")

"""
 write a function that takes in two parameters
 pattern and text. if the text matches the pattern
 print out the keyword that matched the pattern
"""