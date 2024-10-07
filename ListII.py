games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Code below:
# Orders games and creates a new list called games_sorted
games_sorted = sorted(games)

# Prints both games and games_sorted
print(games)
print(games_sorted)

# UNRELATED BELOW (BUT KINDA RELATED)

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Checks to see how many items are in our inventory/warehouse
inventory_len = len(inventory)

# Selects the first element in inventory. Save it to a variable called first.
first = inventory[0]

# Selects the last element from inventory. Saves it to a variable called last.
last = inventory[-1]

# Selects items from the inventory starting at index 2 and up to, but not including, index 6. Response saved to a variable called inventory_2_6.
inventory_2_6 = inventory[2:6]

# Selects the first 3 items of inventory. Saves it to a variable called first_3.
first_3 = inventory[:3]

# How many 'twin bed's are in inventory? Saves response to a variable called twin_beds.
twin_beds = inventory.count("twin bed")

# Removes the 5th element in the inventory. Saves the value to a variable called removed_item.
removed_item = inventory.pop(4)

# New item added to inventory called "19th Century Bed Frame". Uses the .insert() method to place the new item as the 11th element in the inventory.
inventory.insert(10, "19th Century Bed Frame")

# Sorts inventory using the .sort() method. The sorted() function could also be used.
inventory.sort()
print(inventory)
