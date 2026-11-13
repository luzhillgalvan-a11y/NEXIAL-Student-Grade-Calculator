

from luz import manage_student_data
from jonas import validate_student_data
from javier import calculate_final_grade


def evaluate_student_performance(students: list[dict]) -> list[dict]:
    """Classify each student's final grade (Fail, Pass, Good, Excellent).

    Args:
        students (list[dict]): {"name": str, "grades": [n1, n2, n3]} per student.
    Returns:
        list[dict]: {"name": str, "final_grade": float, "category": str} per student.
    """
    results = []
    for student in students:
        final_grade = calculate_final_grade(student["grades"])
        if final_grade >= 9:
            category = "Excellent"
        elif final_grade >= 7:
            category = "Good"
        elif final_grade >= 5:
            category = "Pass"
        else:
            category = "Fail"
        results.append({"name": student["name"], "final_grade": final_grade, "category": category})
    return results
