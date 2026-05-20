x= float(input("Enter a number: "))
res= round(x)
print("Rounded no= ",res)

pi= 3.1415926535
res= round(pi,2)
print("Value of pi= ",res)

total_marks= 500
secured_marks= int(input("Enter secured marks (out of 500): "))
percent= (secured_marks/total_marks)*100
print("Score= ", round(percent,1))

scores = [85, 90, 92, 88]
average= sum(scores)/len(scores)
print("Average score= ",round(average,1))