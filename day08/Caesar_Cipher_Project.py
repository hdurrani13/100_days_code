# Project: Caesar Cipher
# -------------------------- #
from project_logo import logo
import string 

def caesar(original_text, shift_amount, encode_or_decode):
        cipher_text = ""
        if encode_or_decode == "decode":
            shift_amount *= -1
        for letter in original_text:
            if letter not in alpha:
                cipher_text += letter
            else:
                shifted_position = alpha.index(letter) + shift_amount
                shifted_position %= len(alpha)
                cipher_text += alpha[shifted_position]
        print(f"{encode_or_decode}d result: '{cipher_text}'")

alpha = string.ascii_lowercase

print(logo)

play = True
while play:
    direction = input("Type 'encode' to encrypt, type 'decode' decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # charac = ""
    # letters = ""

    # for char in text:
    #     if char.isalpha():
    #         letters += char
    #     else:
    #         charac += char

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again, Otherwise type 'no'.\n")
    if restart == "yes":
        play = True 
        continue
    elif restart == "no":
        play = False
        print("Goodbye")
    else:
        print("Error")



# print(alpha)

# def caesar():
#     direction = input("Type 'encode' to encrypt, type 'decode' decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     def encrypt(original_text, shift_amount):
#         cipher_text = ""
#         for letter in original_text:
#             shifted_position = alpha.index(letter) + shift_amount
#             shifted_position %= len(alpha)
#             cipher_text += alpha[shifted_position]
#         print(f"Encoded result: '{cipher_text}'.")

#     def decrypt(original_text, shift_amount):
#         cipher_text = ""
#         for letter in original_text:
#             shifted_position = alpha.index(letter) - shift_amount
#             shifted_position %= len(alpha)
#             cipher_text += alpha[shifted_position]
#         print(f"Decoded result: '{cipher_text}")
    
#     if direction == "encode":
#         encrypt(text, shift)
#     elif direction == "decode":
#         decrypt(text, shift)
#     else:
#         print("Error")
