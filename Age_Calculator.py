from datetime import date
from tkinter import *
root = Tk()
root.title('Age Calculator')
root.geometry('400x400')
frame = Frame(master=root, height=200, width=300, bg='#d0efff')
lbl1 = Label(master=frame, text="Enter Birth date:", bg="#3895D3", fg="white", width=15)
year_entry = Entry(frame)
def calculate_age():
    birth_year = int(year_entry.get())
    current_year = date.today().date().month().year()
    age = current_year - birth_year
    result_text = f"You are {age} years old."
    textbox.insert(END, result_text)
textbox = Text(bg="#BEBEBE", fg="black")
btn = Button(text="Calculate Age", command=calculate_age, bg="red")
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
year_entry.place(x=180,y=20)
btn.place(x=130,y=80)
textbox.place(y=130)
root.mainloop()