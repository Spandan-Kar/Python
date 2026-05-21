import random

def total(numbers):
    print(sum(numbers))

nums= [random.randint(1000,10000) for _ in range(250)]

total(nums)