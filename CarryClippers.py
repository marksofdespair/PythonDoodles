hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

# Loop through prices
for price in prices:
    total_price += price
print(total_price)

# Flexibility vs hardcoding 8
average_price = total_price / len(prices)

# Prints price with literal
print(f"average_price = {average_price}")

# Step 5
new_prices = [price - 5 for price in prices]
print(new_prices)

# Revenue
total_revenue = 0

# This creates a variable i that goes from 0 to len(hairstyles)
for i in range(len(hairstyles)):  
  total_revenue += prices[i] * last_week[i]

print(f"Total Revenue: {total_revenue}")

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Uses list comprehension to find haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

# Prints the list of haircuts that are underr $30
print(cuts_under_30)


