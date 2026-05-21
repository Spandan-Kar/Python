nums= [47, 83, 12, 59, 31,74, 5, 96, 28, 67,3, 88, 41, 62, 15,99, 22, 55, 37, 70, 54, 98, 13]
result= []

for i in range(len(nums)):
    product= 1

    for j in range(len(nums)):
        if i != j:
            product *= nums[j]

    result.append(product)

print("Products= ", result)