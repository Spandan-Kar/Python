word1= "apple"
word2= "angle"
result= []

for a,b in zip(word1, word2):
    if a==b:
        result.append(a)

print("Common= ", result)