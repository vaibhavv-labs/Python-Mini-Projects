import random
import string

length = int(input("\n Enter Password Length : "))

characters = string.ascii_letters + string.digits

password = " "

for i in range(length):
    password += random.choice(characters)

print("\n", "Generate Any Random password := [", password, "]")
print("\n", "#" * 25, "\n")
