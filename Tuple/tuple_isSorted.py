numbers= (1,2,3,4,6,5,10)

is_sorted= True

for i in range(len(numbers)-1):
    if(numbers[i] > numbers[i+1]):
        is_sorted= False

if(is_sorted):
    print("Tuple is sorted.")
else:
    print("Tuple is not sorted.")