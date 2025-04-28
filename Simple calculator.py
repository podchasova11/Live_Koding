### Simple calculator
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operation")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
