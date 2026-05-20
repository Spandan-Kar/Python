nums = [1, 2, 3, 4, 1]
has_duplicate= False

seen= set()

for num in nums:
    if num in seen:
        has_duplicate= True
        break
    else:
        seen.add(num)

if(has_duplicate):
    print("It has duplicates.")
else:
    print("It doesn't have duplicates.")