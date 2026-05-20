nums= [1,2,5,3,7,5,2,9,5]
target= int(input("Enter target: "))

first= -1
last= -1

for i in range(len(nums)):
    if nums[i] == target:
        if first == -1:
            first= i
        last=i

print("Locations are= ", [first,last])