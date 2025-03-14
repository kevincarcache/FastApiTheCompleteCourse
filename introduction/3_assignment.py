"""
Write a Python program that can do the following:
- You have $50
- You buy an item that is $15, that has a 3% tax
- Using the print()  Print how much money you have left, after purchasing the item
"""

budget = 50
item_price = 15
tax = 0.03
calculated_price = item_price + ( item_price * tax )
money_left=budget - calculated_price
print(f"Budged: ${budget:.2f}")
print(f"Product Price: ${item_price:.2f} Calculated Price: ${calculated_price:.2f}")
print(f"You have: ${money_left:.2f} left")