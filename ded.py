def gradingStudents(gradesList):
    rounded_grades = []
    for grade in gradesList:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            next_multiple_of_5 = (grade//5 + 1) * 5
            if (next_multiple_of_5 - grade) < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)
    return rounded_grades

n = int(input())
gradesList = [int(input()) for _ in range(n)]

result = gradingStudents(gradesList)

for grade in result:
    print(grade)
