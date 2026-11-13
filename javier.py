def calculate_final_grade(first_exam, second_exam, final_exam):
    '''
        First our function checks if all the grades are between 0 and 10 (both included)
  
        Depending on the result, the program carry on with the calculation of the final_grade 
        or just returns “False”

        Finally the program will return the result of the final grade or False if the grades on
        any exam was invalid
    '''
    if validate_grades(first_exam, second_exam, final_exam) == True:
        final_grade = (0.4 * first_exam) + (0.4 * second_exam) + (0.2 * final_exam)
        return final_grade
    else:
        return False
