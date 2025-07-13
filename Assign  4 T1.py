def read_and_print_file(filename="sample.txt"):
    """Reads a text file and prints its content line by line.
    Handles FileNotFoundError gracefully.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')  # end='' prevents extra newline
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage:
read_and_print_file()
