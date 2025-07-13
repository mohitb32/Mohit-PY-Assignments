def get_student_mark():
    """
    Creates a dictionary of student names and marks, then retrieves and displays marks based on user input.
    """
    student_marks = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95, "Eve": 88}

    student_name = input("Enter the student's name: ")

    if student_name in student_marks:
        print(f"The marks for {student_name} are: {student_marks[student_name]}")
    else:
        print(f"Student '{student_name}' not found.")

    student_name = input("Enter the student's name: ")

    if student_name in student_marks:

        print(f"The marks for {student_name} are: {student_marks[student_name]}")
    else:
        print(f"Student not found.")

get_student_mark()