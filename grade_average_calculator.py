import math





def translate_grade(grade_str: str):

    grade_float = 0.0

    try:

        grade_float = float(grade_str)

        grade_int = round(grade_float)

        if grade_int not in [1, 2, 3, 4, 5, 6]:

            return False

        elif grade_float > 0 and grade_float < 6.3:

            return grade_float

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

                if int(i) not in [1, 2, 3, 4, 5, 6]:

                    return False

            except:

                n_of_not_int += 1

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





def calculate_average(grades: list):

    grades_sum = 0.0

    for i in grades:

        grades_sum += i

    return grades_sum / len(grades)





def retranslate_grade(grade_float: float):

    if round(grade_float) - grade_float == 0:

        return str(round(grade_float))

    else:

        try:

            grade_decimal = round(grade_float % math.floor(grade_float), 3)

        except:

            # if 0 < grade_float < 1

            grade_decimal = round(grade_float, 3)

        if grade_decimal == 0.5:

            return f"{math.floor(grade_float)}-/{math.ceil(grade_float)}+"

        elif grade_decimal > 0.5 and grade_decimal <= 0.7:

            return f"{round(grade_float)}+"

        elif grade_decimal >= 0.3 and grade_decimal < 0.5:

            return f"{round(grade_float)}-"

        elif grade_decimal < 0.3 or grade_decimal > 0.7:

            return str(round(grade_float))





if __name__ == "__main__":

    grades = []

    grades_str = ""

    while True:

        grade = input("[grade]/(r)esult: ")

        if grade == "":

            break

        elif grade in ["r", "result"]:

            print(f"The avrage of the grades {grades_str}:")

            print(

                f"{round(calculate_average(grades),2)}       {retranslate_grade(calculate_average(grades))}"

            )

            break

        elif translate_grade(grade) != False:

            grades.append(translate_grade(grade))

            if len(grades_str) == 0:

                grades_str += grade

            else:

                grades_str += f", {grade}"

        elif translate_grade(grade) == False:

            print("Error: wrong Input: Input was ignored")
