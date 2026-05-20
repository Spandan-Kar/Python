nums= [0,1,2,3,4,5,6,8,9,10]
full_set= set(range(len(nums)))
missing= full_set - set(nums)
print("Missing no= ", missing)