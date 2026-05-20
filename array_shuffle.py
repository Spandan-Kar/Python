arr= [1,2,3,4,5,6,7,8,9,10]
l= len(arr) // 2

result= []

for i in range(l):
    result.append(arr[i])
    result.append(arr[i+l])

print("Shuffled array= ", result)
