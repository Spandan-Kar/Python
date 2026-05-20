#Low difficulty
add=  lambda a,b: a+b
print(add(163479,436927))

#Medium difficulty
largest= lambda a,b: a if a>b else b
print(largest(10,20))

#High difficulty
students= [
    ("Spandan",85),
    ("Sanemi",91),
    ("Obanai",79)
]

students.sort(key= lambda x: x[1])
print(students)