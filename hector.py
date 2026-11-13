# MIT License
#
# Copyright (c) 2026 NEXIAL team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
