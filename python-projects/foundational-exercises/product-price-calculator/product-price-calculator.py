# Product Price Calculator
# Asks the user for three product names and prices, then calculates the total and average.

# Ask the user to enter the names of three products
product1 = input("Enter the name of the first product: ")
product2 = input("Enter the name of the second product: ")
product3 = input("Enter the name of the third product: ")

# Ask for the price of each product (two decimal values expected)
price1 = float(input(f"Enter the price of {product1}: "))
price2 = float(input(f"Enter the price of {product2}: "))
price3 = float(input(f"Enter the price of {product3}: "))

# Calculate the total sum of all three products
total_price = round(price1 + price2 + price3, 2)

# Calculate the average price of the three products
average_price = round(total_price / 3, 2)

# Print the final formatted output
print(
    f"The Total of {product1}, {product2}, {product3} is R{total_price} "
    f"and the average price of the items is R{average_price}."
)
