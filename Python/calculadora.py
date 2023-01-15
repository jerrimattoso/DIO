def calculator():
    while True:
        operation = input("What operation would you like to perform? (+, -, *, /): ")
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operator. Please enter a valid operator.")
            continue
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if operation == '+':
            print(num1 + num2)
        elif operation == '-':
            print(num1 - num2)
        elif operation == '*':
            print(num1 * num2)
        elif operation == '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(num1 / num2)
        again = input("Would you like to perform another operation? (yes/no) ")
        if again.lower() == 'no':
            break

calculator()
