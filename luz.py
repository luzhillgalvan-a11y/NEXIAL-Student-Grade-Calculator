
def manage_student_data() -> list[dict]:
    """
    Collect student names and their three grades.

    Returns:
        list[dict]: Student names and grades.
    """
    students = []
    total = int(input("Number of students: "))

    for i in range(total):
        print("\nStudent", i + 1)
        name = input("Student name: ").strip()
        theory = input("Theory grade: ")
        practical = input("Practical grade: ")
        assignments = input("Assignments grade: ")

        # Store student information
        student = {
            "name": name,
            "theory": theory,
            "practical": practical,
            "assignments": assignments
        }

        students.append(student)
        print("Student added successfully:", name)

    # Return all collected students
    return students


if __name__ == "__main__":
    students = manage_student_data()
    print("\nStudent list:", students)
