# Your code below:
# Topping options and prices
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2,6,1,3,2,7,2]

# Number of slices that cost 2 dollars
num_two_dollar_slices = prices.count(2)

# Number of toppings options
num_pizzas = len(toppings)

# Output asked to create
print("We sell", num_pizzas, "different kinds of pizza!")

# Empty list and loop to create a 2D list instead of making by hand
pizza_and_prices = []
for i in range(len(toppings)):
  pizza_and_prices += [[prices[i], toppings[i]]]

# Sorting by price
pizza_and_prices.sort()

# Test print
# print(pizza_and_prices) 

# Storing the value of cheapest and most expensive pizzas
cheapest_pizza = pizza_and_prices[1]
priciest_pizza = pizza_and_prices[-1]

# Ran out of last pizza option so removed
pizza_and_prices.pop()

# New topping option added to the list manually
pizza_and_prices.insert(4, [2.5, "peppers"])

# Customers wanting the three cheapest options stored in new var and printed
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
