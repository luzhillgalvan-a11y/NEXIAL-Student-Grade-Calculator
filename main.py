
from luz import manage_student_data
from jonas import grade_validation
from hector import evaluate_student_performance
from jose import display_results, generate_class_report


def main():
    print("NEXIAL - Student Grade Calculator")

    students = manage_student_data()

    if not students:
        print("No students entered.")
        return

    # Convert grades to numbers
    try:
        for student in students:
            student["theory"] = float(student["theory"])
            student["practical"] = float(student["practical"])
            student["assignments"] = float(student["assignments"])
    except ValueError:
        print("Invalid grades")
        return

    # Validate theory and practical grades
    theory_grades = [student["theory"] for student in students]
    practical_grades = [student["practical"] for student in students]

    if grade_validation(theory_grades, practical_grades) == False:
        return

    # Validate assignment grades
    for student in students:
        if student["assignments"] < 0 or student["assignments"] > 10:
            print("Invalid assignment grade")
            return

    # Evaluate student performance
    results = evaluate_student_performance(students)

    # Display results
    display_results(results)
    generate_class_report(results)


if __name__ == "__main__":
    main()
