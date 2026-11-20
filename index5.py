
# PART ONE: Store 50 original product prices

prices = [
    500, 1200, 1500, 1800, 1900,
    2000, 2200, 2500, 2700, 3000,
    3500, 4000, 4500, 5000, 5500,
    6000, 6500, 7000, 7500, 8000,
    8500, 9000, 9500, 10000, 10500,
    11000, 11500, 12000, 12500, 13000,
    13500, 14000, 14500, 15000, 15500,
    16000, 16500, 17000, 17500, 18000,
    18500, 19000, 19500, 20000, 20500,
    21000, 21500, 22000, 22500, 23000
]

# Create an empty list for updated prices
updated_prices = []

# PART TWO: Increase prices using a for loop

for price in prices:

    if price < 2000:
        new_price = price + (price * 0.05)

    else:
        new_price = price + (price * 0.10)

    updated_prices.append(new_price)


# PART THREE: Print old and updated prices

print("FIRST TEN PRODUCTS")
print("-------------------")

for i in range(10):
    print("Old Price: ₦", prices[i],
          "Updated Price: ₦", updated_prices[i])


print("\nLAST TEN PRODUCTS")
print("-------------------")

for i in range(40, 50):
    print("Old Price: ₦", prices[i],
          "Updated Price: ₦", updated_prices[i])
