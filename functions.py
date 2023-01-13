# These are functions in python

# def greetings(name): # name is a parameter
#     if name == "Bonaventure":
#         print("Your name is Bonaventure")
#     else:
#         print("You are not Bonaventure")
    
# greetings("Bonaventure") # Bonaventure is an argument


# currency converter
def converter(amount, original_currency):
    if original_currency == "USD":
        print(amount*112.5)
    elif original_currency == "EUR":
        print(amount*132.45)
    else:
        print("The currency is not USD or EURO")
        
converter(10, "EUR")
