import random
import turtle

# List of hangman words
hangman_words = ['python', 'programming', 'code', 'algorithm', 'development']

# Choose a random word from the list
word = random.choice(hangman_words)

# Create a list of dashes to represent the hidden word
hidden_word = ['_'] * len(word)

# Keep track of the number of failed attempts
failed_attempts = 0

# Keep track of the letters that have been guessed
guessed_letters = []

# Start the game
while '_' in hidden_word and failed_attempts < 6:
    print(' '.join(hidden_word))
    print('Guessed letters: ', guessed_letters)
    letter = input('Guess a letter: ')

    try:
        # Check if the input is a single letter
        if len(letter) != 1:
            raise ValueError
        # Check if the letter has already been guessed
        elif letter in guessed_letters:
            raise ValueError
    except ValueError:
        print(
            'Invalid input. Please enter a single letter that has not been guessed before.')
        continue

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
    else:
        failed_attempts += 1
        print(
            f'Letter not in word. You have {6 - failed_attempts} attempts remaining.')

# Check if the player won or lost
if '_' not in hidden_word:
    print(' '.join(hidden_word))
    print('You won!')
else:
    print('You lost.')
    print('The word was:', word)


def draw_hangman(failed_attempts):
    # Create a turtle object
    t = turtle.Turtle()
    t.speed(10)

    # Draw the gallows
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.forward(400)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)

    # Draw the head
    if failed_attempts > 0:
        t.right(180)
        t.circle(25)

    # Draw the body
    if failed_attempts > 1:
        t.left(90)
        t.forward(100)

    # Draw the arms
    if failed_attempts > 2:
        t.right(90)
        t.forward(50)
        t.backward(100)
        t.forward(50)

    # Draw the legs
    if failed_attempts > 3:
        t.right(90)
        t.forward(50)
        t.backward(100)
        t.forward(50)

    # Draw the left
    if failed_attempts > 4:
        t.penup()
        t.goto(-20, 50)
        t.pendown()
        t.dot(10)

    # Draw the right eye
    if failed_attempts > 5:
        t.penup()
        t.goto(20, 50)
        t.pendown()
        t.dot(10)

    turtle.done()

    # Call the draw_hangman function inside the while loop
    while '_' in hidden_word and failed_attempts < 6:
        # Code for guessing letters and updating hidden_word
        draw_hangman(failed_attempts)
