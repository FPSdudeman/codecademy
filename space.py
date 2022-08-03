print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
planets = {
  1: {'name': 'Venus', 'weight': 0.91}, 
  2: {'name': 'Mars', 'weight': 0.38},
  3: {'name': 'Jupiter', 'weight': 2.34},
  4: {'name': 'Saturn', 'weight': 1.06},
  5: {'name': 'Uranus', 'weight': 0.92},
  6: {'name': 'Neptune', 'weight': 1.19}
}
if planet <= 6:
  weight *= planets[planet]['weight']
  print("Relative gravity is " + str(planets[planet]['weight']) + " on " + str(planets[planet]['name']) + ".")
  print("Your weight will be equal to " + str(weight))
else:
  print("Not an option listed.")
