import tkinter as tk
from tkinter import ttk, messagebox
class RestarurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.tiltle("Restraurent Management App")
        self.menu_items = {
            "FRIES MEALS": 2,
            "LUNCH MEALS": 3,
            "BURGER MEALS": 4,
            "PIZZA MEALS": 5,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }
        self.exchange_rate = 82
        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(frame,
                  text="Restraurent Order Management",
                  font=("Arial", 20, "bold")).grid(row=0, columnspan=3,padx=10, pady=10)
                