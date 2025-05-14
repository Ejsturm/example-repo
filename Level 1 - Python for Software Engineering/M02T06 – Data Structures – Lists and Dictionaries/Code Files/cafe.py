'''This program enumerates a cafe's items, how much each one costs, and the 
stock amount of each. The total worth will be computed from these data.
2025-05-13 EJS'''

menu = ["bagel", "muffin", "tea", "coffee", "pastry"]

# How many of each item are in stock.
stock = {"bagel": 13,
         "muffin": 6,
         "tea": 25,
         "coffee": 36,
         "pastry": 18
         }

# Prices for each item.
price = {"bagel": 2.99,
         "muffin": 1.50,
         "tea": 1.00,
         "coffee": 1.50,
         "pastry": 2.49
         }

total_stock = 0.0
for item in menu:
    total_stock += stock[item] * price[item]

print(f"The total value of current stock is: {total_stock}.")