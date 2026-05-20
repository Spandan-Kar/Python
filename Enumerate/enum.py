fruits= ["apple", "orange", "banana", "kiwi", "pomegranate", "peach", "mulberry", "guava",
         "papaya", "watermelon", "grapes", "mango"]

for index, fruit in enumerate(fruits):
    print(index+1, fruit)

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)