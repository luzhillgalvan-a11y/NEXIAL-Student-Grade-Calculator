def grade_validation(theory_grades, practical_grades):
    """Validate that both theory and practical grade lists contain valid grades between 0 and 10.
    Checks non-empty lists, equal lengths, and numeric bounds [0, 10].
    Prints 'Invalid grades' and returns False if any check fails; otherwise prints 'All grades are correct' and returns True."""

    if len(theory_grades) == 0 or len(practical_grades) == 0:
        print("Error: Grade lists cannot be empty.")
        print("Invalid grades")
        return False

    for index, grade in enumerate(theory_grades):
        if grade < 0 or grade > 10:
            print(f"Error: Theory grade {grade} at position {index + 1} is out of range (0-10).")
            print("Invalid grades")
            return False

    for index, grade in enumerate(practical_grades):
        if grade < 0 or grade > 10:
            print(f"Error: Practical grade {grade} at position {index + 1} is out of range (0-10).")
            print("Invalid grades")
            return False

    print("All grades are correct")
    return True