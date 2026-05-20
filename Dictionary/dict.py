student= {
    "name":"Spandan Kar",
    "age":21,
    "job":"Associate Analyst",
    "company":"Deloitte USI"
}

student["city"]= "Mumbai"
student["income"]= 24000

student.pop("age")
student.popitem()
student.update({"company":"Accenture"})

print(student)
print(student["company"])
print(student["income"])

for key,value in student.items():
    print(key," : ",value)