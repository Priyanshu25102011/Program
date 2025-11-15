from datetime import date
from tkinter import *

root = Tk()
root.title('Accurate Age Calculator')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=300, bg='#d0efff')

# --- Input Fields for Day, Month, and Year ---
lbl_day = Label(master=frame, text="Day (DD):", bg="#3895D3", fg="white", width=10)
day_entry = Entry(frame, width=5)

lbl_month = Label(master=frame, text="Month (MM):", bg="#3895D3", fg="white", width=10)
month_entry = Entry(frame, width=5)

lbl_year = Label(master=frame, text="Year (YYYY):", bg="#3895D3", fg="white", width=10)
year_entry = Entry(frame, width=7)

def calculate_age():
    # Clear previous results
    textbox.delete('1.0', END)
    
    try:
        # Get and convert user input to integers
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())
        
        # Get today's date
        today = date.today()
        
        # 1. Calculate the base age (Current Year - Birth Year)
        age = today.year - birth_year
        
        # 2. Adjust the age if the birthday hasn't passed yet this year
        # Check if the current month is BEFORE the birth month, OR
        # if the months are the same, check if the current day is BEFORE the birth day.
        if (today.month < birth_month) or \
           (today.month == birth_month and today.day < birth_day):
            age -= 1
            
        result_text = f"You are {age} years old."
        textbox.insert(END, result_text)
        
    except ValueError:
        textbox.insert(END, "Error: Please enter valid numbers for Day, Month, and Year.")
    except Exception as e:
        textbox.insert(END, f"An unexpected error occurred: {e}")

# --- UI Elements ---
textbox = Text(root, bg="#BEBEBE", fg="black", height=2, width=35)
btn = Button(root, text="Calculate Accurate Age", command=calculate_age, bg="red", fg="white")

# --- Placement ---
frame.place(x=20,y=10)

# Day, Month, Year input placement
lbl_day.place(x=20, y=20)
day_entry.place(x=130, y=20)

lbl_month.place(x=20, y=50)
month_entry.place(x=130, y=50)

lbl_year.place(x=20, y=80)
year_entry.place(x=130, y=80)

# Button and Textbox placement
btn.place(x=100, y=130)
textbox.place(x=20, y=180)

root.mainloop()
