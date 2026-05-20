def palindrome_word(word):
    if word == word[::-1]:
        return True
    else:
        return False

word= input("Enter a word: ")
