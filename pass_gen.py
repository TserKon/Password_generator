import random
import string

pass_length = int(input("Enter Length For Your Password: "))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = ""

for i in range(pass_length):
    ran_char = random.choice(chars)
    password += ran_char

print(f"Your random {pass_length} characters length password is: {password}")
