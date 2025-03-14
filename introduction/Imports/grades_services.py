def grades_averages(grades):
    sum_grades = 0
    for grade in grades:
        sum_grades += grade
    total = sum_grades / len(grades) 
    return total