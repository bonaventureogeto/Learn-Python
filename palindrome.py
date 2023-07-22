# check for palindromes in a file

# file = open('words.txt', 'r')
# for words in file:
#     words = words.strip()
#     if(words == words[::-1]):
#         print(words)

with open('words.txt', 'r') as file:
    for words in file:
        words = words.strip()
        if (words == words[::-1]):
            print(words)
