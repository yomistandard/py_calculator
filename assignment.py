# Function to perform and display the calculation
def perform_calculation(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero is undefined."
        result = num1 / num2
    else:
        return "Error: Invalid operation."
    
    return f"{num1} {operation} {num2} = {result}"

# Main program
def main():
    try:
        # Get user input for numbers and operation
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform calculation and print result
        result = perform_calculation(num1, num2, operation)
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

# Run the main program
if __name__ == "__main__":
    main()