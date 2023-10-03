import re

def matchPattern(pattern, text):
    match = re.search(pattern, text)
    if match:
        print("Pattern found!")
    else:
        print("Pattern not found.")
        
matchPattern("apple", "I have an apple and a banana.")
