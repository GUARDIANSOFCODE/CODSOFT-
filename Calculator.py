def calculator():
    print("Simple Calculator")
    print("Operations: + (Addition), - (Subtraction), * (Multiplication), / (Division)")

    # Taking user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    # Performing the calculation
    if operation == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter +, -, *, or /.")

# Run the calculator
calculator()
