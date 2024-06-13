"""
CP1404/CP5632 - Practical
Shop calculator program to calculate the total price of items with a discount for totals over $100.
"""

# Get the number of items
number_of_items = int(input("Number of items: "))

# Input validation for number of items
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Initialize total price
total_price = 0

# Get the price of each item and add to the total price
for i in range(number_of_items):
    price = float(input(f"Price of item {i + 1}: "))
    total_price += price

# Apply a 10% discount if the total price is over $100
if total_price > 100:
    total_price *= 0.9

# Display the total price formatted to 2 decimal places
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
