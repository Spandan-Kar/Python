graph= {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5
}

cloned= {}

for key, value in graph.items():
    cloned[key]= value

print(cloned)