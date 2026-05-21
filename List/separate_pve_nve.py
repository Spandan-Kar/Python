numbers= [-42, 17, -8, 33, 5, -21, 64, -14, 0, 9, -56, 72, -3, 25, -99, 12, -27, 85, -5, 41, -73, 6, -18, 50, -31, 88, -62, 19, -47, 91]

positive= []
negative= []

for num in numbers:
    if(num >= 0):
        positive.append(num)
    else:
        negative.append(num)

print("Positive numbers= ", positive)
print("Negative numbers= ", negative)