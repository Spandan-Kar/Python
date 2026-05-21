sentence= input("Enter a sentence: ")

words= sentence.split()
words= words[::-1]
result= " ".join(words)
print("Reverse words= ", result)