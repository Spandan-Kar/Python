employee= {
    "name":"Spandan Kar",
    "age":21,
    "job":"Associate Analyst",
    "company":"Deloitte USI"
}

employee2= employee.copy()

print(employee == employee2)

employee2["age"]= 30

for key in employee:
    if employee[key] != employee2[key]:
        print(key+" changed")
