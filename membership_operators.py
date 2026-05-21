fruits= ["apple", "orange", "banana", "kiwi", "pomegranate", "peach", "mulberry", "guava",
         "papaya", "watermelon", "grapes", "mango"]

print("apple" in fruits)
print("watermelon" in fruits)

colors= ["yellow", "orange", "blue"]
print("pink" not in colors)

word= "SHINAZUGAWA"
print("P" in word)

employee= {
    "name": "Spandan Kar",
    "age": 21,
    "designation": "Associate Analyst",
    "location": "Bangalore"
}

print("name" in employee)
print("age" not in employee)

#Jewels and Stone problem
jewels= "aA"
stones= "aaaAAbBBba"

count_j= 0
for stone in stones:
    if stone in jewels:
        count_j += 1

