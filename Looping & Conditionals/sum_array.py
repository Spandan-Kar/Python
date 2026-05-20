import random
numbers= [47, 83, 12, 59, 31,74, 5, 96, 28, 67,3, 88, 41, 62, 15,99, 22, 55, 37, 70, 69, 47, 98, 100]
random_numbers= [random.randint(1000000000,100000000000) for _ in range(1000000000)]

sum=0

for num in random_numbers:
    sum += num

print("Sum= ", sum)