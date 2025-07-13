import math


def calculate_and_display():
    """
    Calculates and displays the square root, natural logarithm, and sine of a number provided by the user.
    """
    try:
        number = float(input("Enter a number: "))

        if number < 0:
            print("Cannot calculate square root or natural logarithm of a negative number.")
            return

        square_root = math.sqrt(number)
        _logarithm = math.log(number)
        sine_value = math.sin(number)

        print(f"Square root: {square_root}")
        print(f"logarithm: {_logarithm}")
        print(f"Sine: {sine_value}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


calculate_and_display()
