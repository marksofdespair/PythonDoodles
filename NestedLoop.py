sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

# Loop through the sales_data list using the following guidelines:

# 1) For our temporary variable of the for loop, call it location.
# 2) print() out each location list.

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
    
print(scoops_sold)

# nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.
# By the end, you should have the sum of every number in the sales_data nested list.
