word= input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome word")
else:
    print("Not Palindrome word")