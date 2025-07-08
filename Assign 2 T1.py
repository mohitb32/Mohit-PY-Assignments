# The following code checks if a number is odd or even

# Taking user input
number = int(input("Enter a number : "))

# Condition checking

# if the number is divisible by 2, then even
# else number is odd
if number%2==0:
  print(number, "is even.")
else:
  print(number, "is odd.")
# The following code checks if a number is odd or even

# Taking user input
number = int(input("Enter a number : "))

# Condition checking

# if remainder of operation -> (number divided by 2) * 2 == number, then even
# else number is odd
if (number//2)*2==number:
  print(number, "is even.")
else:
  print(number, "is odd.")