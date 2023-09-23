# currency = ["KSH", "USD", "EURO", "POUND"]

# # Write a python program that converts the specified currency
# # write a function that has two parameters(currency, amount, rates)


# def currencyConverter(amount, currency):
#     # conversion logic goes here
#     if (currency == "KSH"):
#         euroRate = float(input("Enter KSH to Euro Rate: "))
#         dollarRate = float(input("Enter KSH to USD Rate: "))
#         poundRate = float(input("Enter KSH to Pound Rate: "))
#         euros = amount * euroRate
#         dollars = amount * dollarRate
#         pounds = amount * poundRate
#         print(f"{amount} KSH to Euro is: {euros} Euros")
#         print(f"{amount} KSH to USD is: ${dollars}")
#         print(f"{amount} KSH to Pounds is: {pounds} Pounds")
#     elif (currency == "USD"):
#         euroRate = float(input("Enter USD to Euro Rate: "))
#         kshRate = float(input("Enter USD to KSH Rate: "))
#         poundRate = float(input("Enter USD to Pound Rate: "))
#         euros = amount * euroRate
#         ksh = amount * kshRate
#         pounds = amount * poundRate
#         print(f"{amount} USD to Euro is: {euros} Euros")
#         print(f"{amount} USD to KSH is: ${ksh}")
#         print(f"{amount} USD to Pounds is: {pounds} Pounds")
#     else:
#         print("We are yet to add this currency!")


# currencyConverter(200, "KSH")

currency = ["KSH", "USD", "EURO", "POUND"]


# define the function with parameters
def currency_converter(amount, from_currency, to_currency):

    # define the conversion rates
    conversion_rates = {
        'usd': 0.92,
        'euro': 1.09,
        'pound': 1.25,
    }

    # check if the currency is in the list
    converted_amount = amount * \
        conversion_rates[from_currency] / conversion_rates[to_currency]

    # return the converted amount
    return converted_amount


"""
 get the amount and currencies from the user as input 
 and store them in variables amount, from_currency and to_currency
"""

amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency you are converting from: ").lower()
to_currency = input("Enter the currency you are converting to: ").lower()

# call the function and pass the parameters
converted_amount = currency_converter(amount, from_currency, to_currency)
print(converted_amount)
