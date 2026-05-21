names= ["Sanemi", "Obanai", "Giyu", "Gyeomi"]
marks= [98,95,97,100]

for name, mark in zip(names, marks):
    print(name," scored ",mark)

combined= list(zip(names, marks))
print(combined)

hashira= dict(zip(names, marks))
print(hashira)