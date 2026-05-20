planets= {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
planets.add("Rahu")
planets.remove("Earth")

print(planets)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common= set1 & set2
diff1= set1 - set2
diff2= set2 - set1

print("Common= ",common)
print("difference 1= ", diff1)
print("difference 2= ", diff2)