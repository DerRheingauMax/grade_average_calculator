import tkinter as tk
from tkinter import ttk
import grade_average_calculator as be
import math

root = tk.Tk()
root.geometry("600x500")
def submit_grade():
    input = grade_entry.get()
    if be.translate_grade(input) == False:
        return
    else:
        enter_in_table(be.translate_grade(input),third_row_widgets)
        grade_entry.delete(0, tk.END)
    
    

def enter_in_table(grade_float:float,row_widgets):
    grade_str = be.retranslate_grade(grade_float)
    print(grade_str,grade_float)
    if "+" in grade_str:
        text = int(row_widgets[round(grade_float)][0][1]["text"])
        print(text+"   l")
        row_widgets[round(grade_float)-1][0][1].config(text = str(text +1))
    elif "-" in grade_str:
        text = int(row_widgets[round(grade_float)][0][1]["text"])
        row_widgets[round(grade_float)-1][2][1].config(text = str(text +1))
    else:
        text = int(row_widgets[round(grade_float)][0][1]["text"])
        row_widgets[round(grade_float)-1][1][1].config(text = str(text +1))



def generate_table(frame):
    top_row =  ["1","2","3","4","5","6","Ø"]
    top_row_widgets = []
    second_row = [["1+","1","1-"],["2+","2","2-"],["3+","3","3-"],["4+","4","4-"],["5+","5","5-"],["6+","6","6-"],[""]]
    second_row_widgets = []
    third_row_widgets = []
    table = tk.Frame(frame, bg="lightgray")
    for index_first, i_first in enumerate(top_row):
        box = tk.Frame(table, highlightbackground="black", highlightthickness=1)
        label = tk.Label(box,text=i_first).pack(padx=50)
        top_row_widgets.append([box,label])
        box.grid(row=0, column=index_first)
        second_row_widgets.append([])
        third_row_widgets.append([])

        frame_second_row = tk.Frame(table)
        frame_third_row = tk.Frame(table)
        for index_second, i_second in enumerate(second_row[index_first]):
            box_second = tk.Frame(frame_second_row, highlightbackground="black", highlightthickness=1)
            label_second = tk.Label(box_second,text=i_second)
            second_row_widgets[index_first].append([box_second,label_second])
            box_second.grid(row=0,column=index_second)
            label_second.pack()
        
            box_third = tk.Frame(frame_third_row,highlightbackground="black", highlightthickness=1)
            label_third = tk.Label(box_third, text="0")
            third_row_widgets[index_first].append([box_third,label_third])
            box_third.grid(row=0,column=index_second)
            label_third.pack()
        frame_second_row.grid(row=1,column=index_first)
        frame_third_row.grid(row=2,column=index_first)


    return table,third_row_widgets



entry_frame = tk.Frame(root)
table_frame = tk.Frame(root,bg="lightgray",width=500)

grade_entry = tk.Entry(entry_frame)
grade_entry.bind("<Return>",lambda event: submit_grade())
submit_button = tk.Button(entry_frame, command=submit_grade)

table,third_row_widgets = generate_table(table_frame)

entry_frame.place(relx=0.5,anchor="center")
grade_entry.grid(column=0,row=0, padx=20,pady=30)
submit_button.grid(column=1,row=0)

table_frame.place(relx=0.5,rely=0.5, anchor="center")

table.pack()

root.mainloop()