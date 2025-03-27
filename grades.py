def translate_grade(grade_str:str):
    grade_float:float
    try:
        grade_int = int(grade_str)
        if grade_int not in [1,2,3,4,5,6]:
            return False
        else:
            grade_float = float(grade_int)
    except:
        if len(grade_str) != 2:
            return False
        elif "+" not in grade_str and "-" not in grade_str:
            return False
        n_of_not_int = 0
        for i in grade_str:
            try:
                if int(i) not in [1,2,3,4,5,6]:
                    return False
            except:
                n_of_not_int +=1
        if n_of_not_int != 1:
            return
        for i in grade_str:
            try:
                grade_float = float(i)
            except:
                if i == "-":
                    grade_float += 0.3
                elif i == "+":
                    grade_float -= 0.3
    return grade_float

def calculate_avrage(grades:list):
    grades_sum:float
    for i in grades:
        grades_sum += i
    return grades_sum/len(grades)


if __name__ == "__main__":
    grades = []
    while True:
        grade = input("grade: ")
        if grade == "":
            break
        elif not translate_grade(grade):
            grades.append(translate_grade(grade))
        elif grade == "a":
            print(calculate_avrage(grades))
            break
