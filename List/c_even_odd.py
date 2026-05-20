numbers= [47, 83, 12, 59, 31,74, 5, 96, 28, 67,3, 88, 41, 62, 15,99, 22, 55, 37, 70]

even_count= 0
odd_count= 0

for num in numbers:
    if num %2 ==0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers= ", even_count)
print("odd numbers= ", odd_count)