from tkinter import *
import tkinter.messagebox as messagebox
import math
def calculate_simple_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Negative values are not allowed.")
        
        simple_interest = (principal * rate * time) / 100
        total_amount = principal + simple_interest
        
        messagebox.showinfo("Result", f"Simple Interest: {simple_interest}\nTotal Amount: {total_amount}")
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
root = Tk()
root.title("Simple Interest Calculator")
root.geometry("400x300")
label_principal = Label(root, text="Principal Amount:")
label_principal.pack(pady=5)
entry_principal = Entry(root)
entry_principal.pack(pady=5)
label_rate = Label(root, text="Rate of Interest (% per annum):")
label_rate.pack(pady=5)
entry_rate = Entry(root)
entry_rate.pack(pady=5)
label_time = Label(root, text="Time (years):")
label_time.pack(pady=5)
entry_time = Entry(root)
entry_time.pack(pady=5)
button_calculate = Button(root, text="Calculate Simple Interest", command=calculate_simple_interest)
button_calculate.pack(pady=20)
root.mainloop()