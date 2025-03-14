budget = 50
item_price = 15
tax = 0.03
calculated_price = item_price + ( item_price * tax )

formated_price = "Product Price: ${:.2f} Calculated Price: ${:.2f}"
print(formated_price.format(item_price, calculated_price))