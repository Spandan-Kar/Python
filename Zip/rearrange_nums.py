list= [2,0,1]
string= "123"

pairs= zip(list, string)
sorted_pairs= sorted(pairs)

for index, num in sorted_pairs:
    print(num, end="")