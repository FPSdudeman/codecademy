# Three lists each corresponding to their respective places
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Created an empty variable to total up the list prices with the for loop below
total_price = 0

for i in prices:
  total_price += i

# Calculated an average price using the new value of total_price and printed out
average_price = total_price / len(prices)
print(average_price)

# Dropped all prices down by 5 and printed
new_prices = [num - 5 for num in prices]
print(new_prices)

# Calculating total revenu from last week sales
total_revenue = 0
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue:", total_revenue)

# Finding average revenue of last week
average_daily_revenue = total_revenue / 7
print("Average Revenue Last Week:", average_daily_revenue)

# Create a comprehensive list that only takes hairstyles under $30 and prints the results
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices) - 1) if new_prices[i] < 30]

print("These Hairstyles are UNDER $30!", cuts_under_30)
