def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 5
print("Enter a number", num, ": 5",)
print("The factorial of", num, "is:", factorial(num))




