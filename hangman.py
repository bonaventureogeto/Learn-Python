import random

# Set up the words for the game
hangman_words = ['python', 'java', 'ruby', 'javascript',
                 'php', 'csharp', 'swift', 'sql', 'html', 'css']

# Pick a random word
word = random.choice(hangman_words)

# Set up the game
letters_guessed = []
tries = 6
word_completion = '_' * len(word)
guessed = False

# Define the function to print the hangman


def hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


# Start the game
print('Welcome to Hangman!')
print(hangman(tries))
print(word_completion)

while not guessed and tries > 0:
    guess = input('Please guess a letter: ').lower()

    # Check if the guess is a single letter
    if len(guess) == 1 and guess.isalpha():
        # Check if the letter has already been guessed
        if guess in letters_guessed:
            print('You already guessed that letter. Try again.')
        elif guess not in word:
            # Decrement the tries if the letter is not in the word
            print(guess, 'is not in the word.')
            tries -= 1
            letters_guessed.append(guess)
        else:
            # Replace the underscores with the letter if the letter is in the word
            print('Good job,', guess, 'is in the word!')
            letters_guessed.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = ''.join(word_as_list)
            if '_' not in word_completion:
                guessed = True
    else:
        print('Invalid guess. Please enter a single letter.')

    # Print the hangman and the word so far
    print(hangman(tries))
    print(word_completion)

# Print the results
if guessed:
    print('Congratulations, you guessed the word! You win!')
else:
    print('Sorry, you ran out of tries. The word was ' + word + '. You lost.')
