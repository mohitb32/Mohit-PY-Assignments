# Mohit Assignment Task 1
# Function to perform basic mathematical operations
def basic_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = None
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (division by zero)"

    return addition, subtraction, multiplication, division


# Main function
def main():
    # Taking input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Performing operations
        addition, subtraction, multiplication, division = basic_operations(num1, num2)

        # Displaying results
        print(f"Addition: {num1} + {num2} = {addition}")
        print(f"Subtraction: {num1} - {num2} = {subtraction}")
        print(f"Multiplication: {num1} * {num2} = {multiplication}")
        print(f"Division: {num1} / {num2} = {division}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


# Running the main function
if __name__ == "__main__":
    main()
