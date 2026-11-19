def display_results(results):
    """
    Displays the final grade and category of each student.

    Parameters:
        results (list[dict]): {"name", "final_grade", "category"} per student,
                              as returned by evaluate_student_performance().
    """
    if not results:
        print("Error: there are no results to display.")
        return

    print("\n" + "=" * 40)
    print(f"{'STUDENT GRADE RESULTS':^40}")
    print("=" * 40)
    for r in results:
        if r["final_grade"] is False:  # Javier returns False if grades are invalid
            print(f"{r['name']:<15} Invalid grades")
        else:
            print(f"{r['name']:<15} {r['final_grade']:>5.2f}  {r['category']}")
    print("=" * 40)


def generate_class_report(results):
    """
    Prints a class report: average, highest and lowest grade,
    number of passes and fails, and pass percentage.

    Parameters:
        results (list[dict]): {"name", "final_grade", "category"} per student,
                              as returned by evaluate_student_performance().
    Returns:
        dict | None: the report data, or None if there are no valid grades.
    """
    grades = [r["final_grade"] for r in results if r["final_grade"] is not False]
    if not grades:
        print("Error: there are no valid grades to report.")
        return None

    passed = sum(1 for g in grades if g >= 5)
    failed = len(grades) - passed
    report = {
        "average": sum(grades) / len(grades),
        "highest": max(grades),
        "lowest": min(grades),
        "passed": passed,
        "failed": failed,
        "pass_rate": passed / len(grades) * 100,
    }

    print("\n" + "=" * 30)
    print(f"{'CLASS REPORT':^30}")
    print("=" * 30)
    print(f"Class average: {report['average']:.2f}")
    print(f"Highest grade: {report['highest']:.2f}")
    print(f"Lowest grade:  {report['lowest']:.2f}")
    print(f"Passed: {passed}  |  Failed: {failed}")
    print(f"Pass rate: {report['pass_rate']:.1f}%")
    print("=" * 30)
    return report


if __name__ == "__main__":
    from luz import manage_student_data
    from hector import evaluate_student_performance

    students = manage_student_data()
    results = evaluate_student_performance(students)
    display_results(results)
    generate_class_report(results)
