import tkinter as tk
from tkinter import messagebox

def show(value):
    current_text = entry_var.get()
    entry_var.set(current_text + value)

def clear():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression: {e}")
        entry_var.set("")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#17161b")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, font=("Arial", 20), padx=20, pady=20, bd=8, fg="white", bg="#2a2d36",
                    command=lambda t=text: show(t) if t != '=' else calculate())
    btn.grid(row=row, column=col, sticky="nsew")

# Configure row and column weights so that they expand proportionally
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()