# Weight input
weight = 6

# Shipping Logic

ground_flat = 20 # Flat charge for ground shipping

# Dictionary for weight and price of ground and drone shipping
shipping_dict = {
    1: {'weight': 2, 'price': {'ground': 1.50, 'drone': 4.50}},
    2: {'weight': 6, 'price': {'ground': 3.00, 'drone': 9.00}},
    3: {'weight': 10, 'price': {'ground': 4.00, 'drone': 12.00}},
    4: {'weight': 11, 'price': {'ground': 4.75, 'drone': 14.25}}
  }

# Loop to define 'ground_cost' and 'drone_cost'
for i in range(1, 4):
  if shipping_dict[i]['weight'] >= weight:
    ground_cost = weight * shipping_dict[i]['price']['ground'] + ground_flat
    drone_cost = weight * shipping_dict[i]['price']['drone']
    break
  elif shipping_dict[4]['weight'] < weight:
    ground_cost = weight * shipping_dict[i]['price']['ground'] + ground_flat
    drone_cost = weight * shipping_dict[i]['price']['drone']
    break

# Printing out all costs as per instructions
print("Your shipment using 'Ground Shipping' will cost $", str(ground_cost))

print("Your shipment using 'Drone Shipping' will cost $", str(drone_cost))

print("Don't forget our 'Ground Shipping Premium' is $125.00 flat! No extra costs!")
