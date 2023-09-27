def isPalindrome(fromFile, toFile):
    with open(fromFile, 'r') as file:
        for words in file:
            words = words.strip()
            if(words == words[::-1]):
                with open(toFile, 'w') as pal:
                    pal.writelines(words)
                    
isPalindrome('words.txt', 'palindromes.txt')
