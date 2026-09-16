num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))
op = input("Enter Operation (+, -, *, /) : ")

if op == "+":
    print(f"Addition : {num1+num2}")
elif op == "-":
    print(f"Substraction : {num1-num2}")
elif op == "*":
    print(f"Multiplication : {num1*num2}")
elif op == "/":
    print(f"Division : {num1/num2}")
else:
    print("Invalid Operation !!")
