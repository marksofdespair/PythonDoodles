# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
# Count the instances of 2
num_two_dollar_slices = prices.count(2)

# Print the result
print(num_two_dollar_slices)

# Stores length of toppings in num_pizzas
num_pizzas = len(toppings)

print(f"We sell {num_pizzas} different kinds of pizza!")

pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

# Printing the list to verify
print(pizza_and_prices)

# Sorting the list by the first element (price)
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# Remove slice since it was bought
removed_item = pizza_and_prices.pop()

# New topping to add
new_topping = [2.5, "peppers"]
pizza_and_prices.append(new_topping)

# 13 v
pizza_and_prices.sort()  # Make sure it's sorted by price

# Slice the first 3 elements
three_cheapest = pizza_and_prices[:3]

# Print the three cheapest pizzas
print(three_cheapest)

