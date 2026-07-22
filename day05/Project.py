# Project: Password Creator
'----------------------------------'
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")

n_let = int(input("How many letters would you like in your password?\n"))
n_sym = int(input("How many symbols would you like in your password?\n"))
n_num = int(input("How many numbers would you like in your password?\n"))

pass_list = []

for char in range(1, n_let + 1):
    pass_list += random.choice(letters)

for char in range(1, n_sym + 1):
    pass_list += random.choice(symbols)

for char in range(1, n_num + 1):
    pass_list += random.choice(numbers)

random.shuffle(pass_list)
# print(pass_list)

password = '' 
for char in pass_list:
    password += char

print(f"Your password is: {password}")





