s= input("Enter first string: ")
t= input("Enter second string: ")

count1= {}
count2= {}

for ch in s:
    if ch in count1:
        count1[ch] += 1
    else:
        count1[ch] = 1

for ch in t:
    if ch in count2:
        count2[ch] += 1
    else:
        count2[ch] = 1

if(count1 == count2):
    print("They are valid anagram.")
else:
    print("They aren't valid anagram.")