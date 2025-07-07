#Mohit Task 2
# Function to get user's full name and print a greeting
def greet_user():
    # Taking first name and last name as input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Concatenating first name and last name
    full_name = first_name + " " + last_name

    # Printing a personalized greeting message
    print(f"Hello, {full_name}! Welcome to the Python program!")


# Running the function
if __name__ == "__main__":
    greet_user()

