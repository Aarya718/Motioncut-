import csv
import datetime
import os
import tkinter as tk
from tkinter import ttk, messagebox

EXPENSE_FILE = "expenses.csv"


def initialize_file():
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])


def add_expense():
    date = datetime.date.today().strftime("%Y-%m-%d")
    amount = amount_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid amount. Please enter a number.")
        return
    
    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    
    messagebox.showinfo("Success", "Expense added successfully!")
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    view_expenses()


def view_expenses():
    for row in expense_tree.get_children():
        expense_tree.delete(row)
    
    try:
        with open(EXPENSE_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                expense_tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        messagebox.showinfo("Info", "No expenses recorded yet.")


root = tk.Tk()
root.title("Expense Tracker")
root.geometry("700x500")
root.configure(bg="#FFB6C1")  

style = ttk.Style()
style.configure("TFrame", background="#FFC0CB")  
style.configure("TLabel", background="#FFC0CB", foreground="black", font=("Arial", 12))
style.configure("TButton", background="#FF69B4", foreground="white", font=("Arial", 12, "bold"))
style.configure("Treeview", background="#FFFFFF", foreground="black", rowheight=25)
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.X)

sticker = tk.PhotoImage(file="sticker2.png")  
sticker_label = tk.Label(frame, image=sticker, bg="#FFC0CB")
sticker_label.grid(row=0, column=2, rowspan=3, padx=10)

ttk.Label(frame, text="Amount: ").grid(row=0, column=0, padx=5, pady=5, sticky="w")
amount_entry = ttk.Entry(frame)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Category: ").grid(row=1, column=0, padx=5, pady=5, sticky="w")
category_entry = ttk.Entry(frame)
category_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Description: ").grid(row=2, column=0, padx=5, pady=5, sticky="w")
description_entry = ttk.Entry(frame)
description_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = ttk.Button(frame, text="Add Expense", command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

columns = ("Date", "Amount", "Category", "Description")
expense_tree = ttk.Treeview(root, columns=columns, show="headings", style="Treeview")

for col in columns:
    expense_tree.heading(col, text=col)
    expense_tree.column(col, width=150)

expense_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

initialize_file()
view_expenses()

root.mainloop()