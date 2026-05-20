#Low difficulty
numbers= [1,2,3,4,5]
result= filter(
    lambda x: x%2==0,
    numbers
)

print(list(result))

#Medium difficulty
names=[
    "Gyeomi Himejima",
    "Sanemi Shinazugawa",
    "Muichiro Tokito",
    "Genya Shinazugawa"
]

result= filter(
    lambda name: len(name) >15,
    names
)

print(list(result))

#High difficulty
students= [
    {"name":"Spandan Kar", "marks":95},
    {"name":"Kokushibo", "marks":87},
    {"name":"Douma", "marks":85}
]

result= filter(
    lambda student: student["marks"]>=90,
    students
)

print(list(result))