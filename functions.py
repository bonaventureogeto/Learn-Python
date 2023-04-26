def hello(name):
    print(f"Hello {name}")


hello("Kenya")


# These are functions in python

def greetings(name):  # name is a parameter
    if name == "Bonaventure":
        print("Your name is Bonaventure")
    else:
        print("You are not Bonaventure")


greetings("Bonaventure")  # Bonaventure is an argument


# currency converter
def converter(amount, original_currency):
    if original_currency == "USD":
        print(amount*112.5)
    elif original_currency == "EUR":
        print(amount*132.45)
    else:
        print("The currency is not USD or EURO")


converter(10, "EUR")

# def greet(name):
#     print("Hello ", name)


# greet("Bonaventure")

# longest word
def find_longest_word(sentence):
    """
    A function that takes a sentence as input and returns the longest word in that sentence.
    """
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


longest_word = find_longest_word(
    "A function that takes a sentence as input and returns the longest word in that sentence")
print(longest_word)

# fibonacci series


def calculate_fibonacci_sequence(n):
    """
    A function that takes an integer as input and returns a list of the first n numbers in the Fibonacci sequence.
    """
    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence[:n]
