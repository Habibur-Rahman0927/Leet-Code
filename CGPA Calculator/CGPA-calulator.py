def gpa_calculator(grades):
    points = 0
    i = 0
    grade_c = {"A":4,"A-":3.67,"B+":3.33,"B":3.0,"B-":2.67, "C+":2.33,"C":2.0,"C-":1.67,"D+":1.33,"D":1.0,"F":0}
    if grades != []:
        for grade in grades:
            points += grade_c[grade]
        gpa = points / len(grades)
        return gpa
    else:
        return None
 
 
grades = [ 'A', 'B', 'A', 'C']
print(gpa_calculator(grades))
 
grades = ['A', 'B', 'C', 'F', 'A', 'B+']
print(gpa_calculator(grades))