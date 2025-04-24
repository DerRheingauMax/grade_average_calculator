import math


def translate_grade(grade_str: str):
    grade_float = 0.0
    try:
        grade_float = float(grade_str)
        grade_int = round(grade_float)
        if grade_int not in range(1, 7):
            return False
        elif grade_float > 0 and grade_float < 6.3:
            return grade_float
        else:
            return False
    except ValueError:
        if len(grade_str) != 2:
            return False
        elif "+" not in grade_str and "-" not in grade_str:
            return False
        n_of_not_int = 0
        for i in grade_str:
            try:
                if int(i) not in range(1, 7):
                    return False
            except ValueError:
                n_of_not_int += 1
        if n_of_not_int != 1:
            return
        for i in grade_str:
            try:
                grade_float = float(i)
                if grade_float == 6.0:
                    return False  # There is no 6+ or 6-
            except ValueError:
                if i == "-":
                    grade_float += 0.3
                elif i == "+":
                    grade_float -= 0.3
    return grade_float


def calculate_average(grades: list):
    grades_sum = 0.0
    for i in grades:
        grades_sum += i
    return grades_sum / len(grades)


def retranslate_grade(grade_float: float):
    if round(grade_float) - grade_float == 0:
        return str(round(grade_float))
    elif round(grade_float) == 6.0:
        return str(round(grade_float))  # There is no 6+ or 6-
    else:
        grade_decimal = round(grade_float - math.floor(grade_float), 3)
        if grade_decimal == 0.5:
            return f"{math.floor(grade_float)}-/{math.ceil(grade_float)}+"
        elif grade_decimal > 0.5 and grade_decimal <= 0.7:
            return f"{round(grade_float)}+"
        elif grade_decimal >= 0.3 and grade_decimal < 0.5:
            return f"{round(grade_float)}-"
        elif grade_decimal < 0.3 or grade_decimal > 0.7:
            return str(round(grade_float))


def point_to_grade(point_float: float):
    p_int = round(point_float)
    if p_int == 0:
        return 6
    try:
        faktor = -0.3 + 0.6 * (1 / (p_int % 3))
    except ZeroDivisionError:
        faktor = -0.3
    g_int = 6 - math.ceil(p_int / 3)
    g_float = g_int + faktor
    return g_float


def grade_to_point(grade_float: float):
    grade_int = round(grade_float)
    if grade_int == 6:
        return 0
    point_int = 14 - 3 * (grade_int - 1)
    grade_decimal = round(grade_float - math.floor(grade_float), 3)
    if grade_decimal >= 0.5 and grade_decimal <= 0.7:
        point_float = float(point_int + 1)
    elif grade_decimal >= 0.3 and grade_decimal < 0.5:
        point_float = float(point_int - 1)
    elif grade_decimal < 0.3 or grade_decimal > 0.7:
        point_float = float(point_int)
    return point_float


if __name__ == "__main__":
    grades = []
    grades_str = ""
    grade_type = "grades"
    while True:
        if grade_type== "grades":
            grade = input("[grade]/(r)esult/(s)ettings: ")
        elif grade_type=="points":
            grade = input("[points]/(r)esult/(s)ettings: ")
            
        if grade == "":
            break
        elif grade in ["r", "result"]:
            print(f"The avrage of the grades {grades_str}:")
            if grade_type == "grades":
                print(
                    f"{round(calculate_average(grades),2)}       {retranslate_grade(calculate_average(grades))}"
                )
            elif grade_type == "points":
                print(
                    f"{round(calculate_average(grades),2)}       {retranslate_grade(point_to_grade(calculate_average(grades)))}"
                )
            break
        elif grade in ["s", "settings"]:
            if grade_type == "grades":
                user_decicon = input(f"grade system [grades]/(p)oints: ")
            elif grade_type == "points":
                user_decicon = input(f"grade system (g)rades/[points]: ")
            if (
                user_decicon == ""
                or user_decicon == grade_type
                or user_decicon[0] == grade_type[0]
            ):
                continue
            elif user_decicon in ["g", "grades"]:
                grade_type = "grades"
                if grades != []:
                    print("Warning: All previos grades will be converted to grades.")
                    user_decicon_warning = input("Do you want to procced? [yes]/(n)o: ")
                    if user_decicon_warning in ["", "y", "yes"]:
                        for index, i in enumerate(grades):
                            grades[index] = point_to_grade(i)
                    elif user_decicon_warning in ["n", "no"]:
                        print("Info: The grade system wasn't changed.")
            elif user_decicon in ["p", "points"]:
                grade_type = "points"
                if grades != []:
                    print("Warning: All previos grades will be converted to points.")
                    user_decicon_warning = input("Do you want to procced? [yes]/(n)o: ")
                    if user_decicon_warning in ["", "y", "yes"]:
                        for index, i in enumerate(grades):
                            grades[index] = grade_to_point(i)
                    elif user_decicon_warning in ["n", "no"]:
                        print("Info: The grade system wasn't changed.")
            else:
                print("Error: Wrong input no setting has been changed.")
        elif grade_type == "grades" and translate_grade(grade) != False:
            grades.append(translate_grade(grade))
            if len(grades_str) == 0:
                grades_str += grade
            else:
                grades_str += f", {grade}"
        elif grade_type == "grades" and translate_grade(grade) == False:
            print("Error: wrong Input: Input was ignored")
        elif grade_type == "points":
            try:
                point_float = float(grade)
                if round(point_float) not in range(0, 16):
                    int("")  # to get the input ignored massage
                grades.append(point_float)
                if len(grades_str) == 0:
                    grades_str += grade
                else:
                    grades_str += f", {grade}"
            except ValueError:
                print("Error: wrong Input: Input was ignored")
