weight = 2.4
flat_charge = 20.00
premium_ground = 125.00

# Ground Shipping
if weight <= 2:
    cost_ground = weight * 1.50 + flat_charge
elif weight <= 6:
    cost_ground = weight * 3.00 + flat_charge
elif weight <= 10:
    cost_ground = weight * 4.00 + flat_charge
else:
    cost_ground = weight * 4.75 + flat_charge

# print cost for ground customer
print(f"The cost of shipping is: ${cost_ground:.2f}")

# Drone Shipping
if weight <= 2:
    cost_drone = weight * 4.50 
elif weight <= 6:
    cost_drone = weight * 9.00 
elif weight <= 10:
    cost_drone = weight * 12.00 
else:
    cost_drone = weight * 14.25 

# print cost for drone customer
print(f"The cost of shipping is: ${cost_drone:.2f}")
