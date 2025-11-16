from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry('100x100')
def handel_keypress(event):
    print(event.char)
window.bind("<Key>", handel_keypress)
def handel_click(event):
    print("\nThe button was clicked!")
button = Button(text="Click me!")
button.pack()
button.bind("<Button-1>", handel_click)
window.mainloop()