fruits= ["apple", "orange", "banana", "kiwi", "pomegranate", "peach", "mulberry", "guava",
         "papaya", "watermelon", "grapes", "mango"]

print(fruits[1:4])

name= "Muzan Kibutsuji"
print(name[2:6])
print(name[6:])

#Skip elements using step
nums= [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])

#Reverse a list using slicing
print(nums[::-1])

#Extract first 3 and last 3 elements
print("First three= ", nums[:3])
print("Last three= ", nums[-3:])