numbers= (47, 83, 12, 59, 31,74, 5, 96, 28, 67,12, 88, 41, 62, 15,99, 22, 55, 12, 70)
target= int(input("Enter target: "))

seen= set()
for num in numbers:
    complement= target - num
    if complement in seen:
        print("Pair found: ", complement, " & ", num)
    seen.add(num)