numbers= [47, 83, 12, 59, 31,74, 5, 96, 28, 67,3, 88, 41, 62, 15,99, 22, 55, 37, 70]

target= int(input("Enter target: "))

for index, num in enumerate(numbers):
    if num == target:
        print("Found at index: ", index)