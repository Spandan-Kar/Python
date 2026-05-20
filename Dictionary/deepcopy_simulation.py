import copy

employee= {
    "name":"Spandan Kar",
    "age":21,
    "job":"Associate Analyst",
    "company":"Deloitte USI",
    "marks":{
        "Aptitude":90,
        "Reasoning":85,
        "Output Based":100,
        "Coding":100
    }
}

new_employee= copy.deepcopy(employee)

new_employee["marks"]["Aptitude"]= 75

print(new_employee)