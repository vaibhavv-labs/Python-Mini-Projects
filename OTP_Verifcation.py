import random

print("OTP VERIFICATION")
otp = random.randint(100000, 999999)
print("Your OTP is", otp)
print("OTP send Successfully ")

print("RECEIVER")

user_otp = int(input("Enter Your OTP : "))

if user_otp == otp:
    print("OTP Recieve Successfully")
else:
    print("Wrong OTP")
