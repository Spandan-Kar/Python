#peak element is greater than both neighbors

nums= [1, 2, 3, 1]

for i in range(1, len(nums)-1):
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        peak= nums[i]

print("Peak element= ", peak)