# Basic Calculator Program

#  enter the first number
num1 = float(input("Enter the first number: "))

# enter the second number
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform calculation based on operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
