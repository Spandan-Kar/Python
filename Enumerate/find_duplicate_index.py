nums = [1, 2, 3, 2, 4, 1]
seen= {}

for index, num in enumerate(nums):
    if num in seen:
        print("Duplicate of ",num," found at ",index)
    else:
        seen[num]= index
