"""
Variables
"""

message = "Hello World"
print(message)

price = 25.99
tax = 0.07
calculated_tax = price * tax
total_price = price + calculated_tax

"""
Si concatenamos con + debemos convertir a str
"""
print("The original price is: " + str(price) + " and the total price is: " + str(total_price))

"""
Con , no es necesario
"""
print("The original price is:", price ,"and the total price is:", total_price)

"""
Si deseamos tener mayor control sobre la salida podemos formatearla con f"cadena {variable1} .... {variable2}"
"""
print(f"The original price is: {price:.2f} and the total price is: {total_price:.2f}")