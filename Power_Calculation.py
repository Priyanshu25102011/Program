a = int(input("Enter the first number: "))
sign = input("Enter the operator (+, -, *, /): ")
b = int(input("Enter the second number: "))
if (sign == '+'):
    print("Result:", a + b)
elif (sign == '-'):
    print("Result:", a - b)
elif (sign == '*'):
    print("Result:", a * b)
else:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed.")