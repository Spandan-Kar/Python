import string

lowercase_alphabets= list(string.ascii_lowercase) #main
uppercase_alphabets= list(string.ascii_uppercase)
all_alphabets= list(string.ascii_letters)

#TODO 1- Create a function called encrypt() that takes "original_text" and "shift_amount" as 2 inputs

#TODO 2- Inside the "encrypt()" function, shift each letter of the "original_text" forwards in alphabet
#by the shift amount and print the encrypted text

#hello
def encrypt(original_text, shift_amount):
    cipher_text= "" #j
    for letter in original_text:
        if letter not in lowercase_alphabets:
            cipher_text += letter
        else:
            shifted_position = lowercase_alphabets.index(letter) + shift_amount  # 7 -> 9
            shifted_position = shifted_position % len(lowercase_alphabets)
            cipher_text += lowercase_alphabets[shifted_position]  # j

    print("Here is your encoded result= ", cipher_text)

def decrypt(original_text, shift_amount):
    cipher_text= ""
    for letter in original_text:
        shifted_position= lowercase_alphabets.index(letter) - shift_amount
        shifted_position %= len(lowercase_alphabets)
        cipher_text += lowercase_alphabets[shifted_position]

    print("Here is your decoded result= ", cipher_text)

#TODO 3- Call the "encrypt()" function and pass user inputs. You should be able to test the code
#and encrypt a message


#TODO 4- What happens if you try to shift z forwards 9? Can you fix the code?
#Ans- shifted_position %= len(lowercase_alphabets)

should_continue= True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("No such operation exists.")

    question = input("Do you want to continue? Type 'yes' or 'no'")
    if(question == 'no'):
        print("Goodbye, User.")
        should_continue= False