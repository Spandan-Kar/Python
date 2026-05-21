#Check how many matching positions exist
x= [1,2,3,4,5]
y= [1,2,3,4,6]
count=0

for a,b in zip(x,y):
    if a==b:
        count += 1

print("No of matching positions= ", count)
