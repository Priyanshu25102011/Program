from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Denominating Window")
root.config(bg="lightblue")
root.geometry("650x400")
upload = Image.open(r"app_img.jpg")
upload = upload.resize((300,300))
image= ImageTk.PhotoImage(upload)
label = Label(root, image =image, bg='Lightblue')
label.place(x=180,y=20)
label1 = Label(root,text = "Hey!User Welcome to Denominating Application", bg="lightblue" )
label1.place(relx=0.5, y=340, anchor=CENTER)
def msg():
    msgBox = messagebox.showinfo("Alert!","Do you want to calculate the denomination?")
    if msgBox == 'ok':
        topwin()
button1 = Button(root, text="Let's get started", command=msg, bg="brown", fg="white")
button1.place(x=260, y=360)
def topwin():
    top=Toplevel()
    top.geometry("600x350+50+50")
    top.title("Denomination Window")
    top.configure(bg="lightgreen")
    top.title("Denomination Window")

    label= Label(top, text="Enter the Amount:", bg="lightgrey")
    entry = Entry(top)
    lbl= Label(top, text="Here are Number of Notes for each Denomination", bg="lightgrey")

    l1 = Label(top,text="2000:", bg="lightgreen") 
    l2 = Label(top,text="500:", bg="lightgreen")
    l3 = Label(top,text="100:", bg="lightgreen")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def caculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amounty %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
    btn = Button(top, text="Calculate", command=caculator, bg="brown", fg="white")
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    top.mainloop()
root.mainloop()
