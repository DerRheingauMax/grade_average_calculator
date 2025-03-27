def translate_grade(grade_str:str):
    grade_float =0.0
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
    grades_sum= 0.0
    for i in grades:
        grades_sum += i
    return grades_sum/len(grades)


if __name__ == "__main__":
    grades = []
    grades_str = ""
    while True:
        grade = input("[grade]/result: ")
        if grade == "":
            break
        elif grade in ["r","result"]:
            print(f'The avrage of the grades {grades_str}:')
            print(calculate_avrage(grades))
            break
        elif translate_grade(grade) != False:
            grades.append(translate_grade(grade))
            if len(grades_str) == 0:
            	grades_str += grade
            else:
            	grades_str += f', {grade}'
        elif translate_grade(grade) == False:
        	print("Error: wrong Input: Input was ignored")
