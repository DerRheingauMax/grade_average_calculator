import math
import tkinter as tk
from tkinter import ttk
import grade_average_calculator as be

root = tk.Tk()
root.geometry("600x500")

grades = []
grade_type = "points"
grade_row_widgets = []

def submit_grade():
    global grades, grade_type,grade_row_widgets
    input = grade_entry.get()
    if grade_type == "grades" and be.translate_grade(input) != False:
        grade_float = be.translate_grade(input)
        grades.append(grade_float)
        enter_in_table(grade_float, grade_row_widgets)
        grade_entry.delete(0, tk.END)
        grade_row_widgets[-1][0][1].config(text=round(be.calculate_average(grades), 2))
    elif grade_type == "points":
        try:
            point_float = float(input)
            if round(point_float) not in range(0, 16):
                    int("")  # to get the input ignored massage
            grades.append(point_float)
            enter_in_table(point_float,grade_row_widgets)
            grade_entry.delete(0,tk.END)
            grade_row_widgets[-1][1].config(text=round(be.calculate_average(grades), 2))
        except ValueError:
            print("no")
            return
    else:
        print("no")
        return



def enter_in_table(grade_float: float, row_widgets):
    global grade_type
    if grade_type == "gardes":
        grade_str = be.retranslate_grade(grade_float)
        if "+" in grade_str:
            row_widgets[round(grade_float - 1)][0][2] += 1
            text = row_widgets[round(grade_float - 1)][0][2]
            row_widgets[round(grade_float) - 1][0][1].config(text=str(text))
        elif "-" in grade_str:
            row_widgets[round(grade_float - 1)][2][2] += 1
            text = row_widgets[round(grade_float - 1)][2][2]
            row_widgets[round(grade_float) - 1][2][1].config(text=str(text))
        else:
            row_widgets[round(grade_float - 1)][1][2] += 1
            text = row_widgets[round(grade_float - 1)][1][2]
            row_widgets[round(grade_float) - 1][1][1].config(text=str(text))
    elif grade_type == "points":
        grade_str = str(round(grade_float))
        print(row_widgets)
        print(row_widgets[16-round(grade_float)][2])
        row_widgets[16-round(grade_float)][2] +=1
        text = row_widgets[16-round(grade_float)][2]
        row_widgets[16-round(grade_float)][1].config(text=text)


def switch_grade_type():
    global grade_type
    if grade_type == "grades":
        grade_type = "points"
        grade_table.pack_forget()
        point_table.pack()
    elif grade_type == "points":
        grade_type = "grades"
        point_table.pack_forget()
        grade_table.pack()

def generate_grade_table(frame):
    top_row = ["1", "2", "3", "4", "5", "6", "Ø"]
    top_row_widgets = []
    second_row = [
        ["1+", "1", "1-"],
        ["2+", "2", "2-"],
        ["3+", "3", "3-"],
        ["4+", "4", "4-"],
        ["5+", "5", "5-"],
        ["6+", "6", "6-"],
        [""],
    ]
    second_row_widgets = []
    third_row_widgets = []
    table = tk.Frame(frame, bg="lightgray")
    for index_first, i_first in enumerate(top_row):
        box = tk.Frame(table, highlightbackground="black", highlightthickness=1)
        label = tk.Label(box, text=i_first).pack(padx=50)
        top_row_widgets.append([box, label])
        box.grid(row=0, column=index_first)
        second_row_widgets.append([])
        third_row_widgets.append([])
        frame_second_row = tk.Frame(table)
        frame_third_row = tk.Frame(table)
        for index_second, i_second in enumerate(second_row[index_first]):
            box_second = tk.Frame(
                frame_second_row, highlightbackground="black", highlightthickness=1
            )
            label_second = tk.Label(box_second, text=i_second)
            second_row_widgets[index_first].append([box_second, label_second])
            box_second.grid(row=0, column=index_second)
            label_second.pack()
            box_third = tk.Frame(
                frame_third_row, highlightbackground="black", highlightthickness=1
            )
            label_third = tk.Label(box_third, text="0")
            third_row_widgets[index_first].append([box_third, label_third, 0])
            box_third.grid(row=0, column=index_second)
            label_third.pack()
        frame_second_row.grid(row=1, column=index_first)
        frame_third_row.grid(row=2, column=index_first)
    return table, third_row_widgets

def generate_point_table(frame):
    top_row = ["15","14","13","12","11","10","9","8","7","6","5","4","3","2","1","0", "Ø"]
    top_row_widgets = []
    second_row_widgets = []
    table = tk.Frame(frame, bg="lightgray")
    for index, i in enumerate(top_row):
        box = tk.Frame(table, highlightbackground="black", highlightthickness=1)
        label = tk.Label(box, text=i).pack(padx=20)
        top_row_widgets.append([box, label])
        box.grid(row=0, column=index)
        box_second = tk.Frame(
                table, highlightbackground="black", highlightthickness=1
            )
        label_second = tk.Label(box_second, text="0")
        second_row_widgets.append([box_second,label_second,0])
        box_second.grid(row=1,column=index)
        label_second.pack()
    return table, second_row_widgets
        

entry_frame = tk.Frame(root)
table_frame = tk.Frame(root, bg="lightgray", width=500)
grade_entry = tk.Entry(entry_frame)
grade_entry.bind("<Return>", lambda event: submit_grade())
submit_button = tk.Button(entry_frame, command=submit_grade,text="Enter")
switch_button = tk.Button(entry_frame, command=switch_grade_type,text=grade_type)


grade_table, grade_row_widgets = generate_grade_table(table_frame)

point_table, point_row_widgets = generate_point_table(table_frame)

entry_frame.place(relx=0.5, rely=0.3, anchor="center")
grade_entry.grid(column=0, row=0, padx=20, pady=30)
submit_button.grid(column=1, row=0)
switch_button.grid(column=2,row=0)
table_frame.place(relx=0.5, rely=0.5, anchor="center")

if grade_type == "grades":
    grade_table.pack()
elif grade_type == "points":
    point_table.pack()

root.mainloop()
