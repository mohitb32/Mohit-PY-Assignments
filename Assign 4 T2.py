# 1. Write user input to a file
with open("output.txt", "w") as f:
    user_input = input("Enter some text to write to the file:")
    f.write(user_input + "\n")
    print("Data successfully written to output.txt.")

# 2. Append additional data
with open("output.txt", "a") as f:
    additional_data = input("Enter additional text to append:")
    f.write(additional_data + "\n")
    print("Data successfully appended")

# 3. Read and display the file content
with open("output.txt", "r") as f:
    content = f.read()
    print("Final content of output.txt:\n","Hello,Python!")
    print("Learning file handling in Python")