str= input("Enter a string: ")
k= int(input("Enter k-rotations: "))

newStr= str[-k:] + str[:-k]
print("K-rotated string= ", newStr)