# in this code we will check the user fill all the fields of registraion form or not
import tkinter as tk
import openpyxl
from tkinter import messagebox
from openpyxl import load_workbook
import re

root=tk.Tk()
root.title("Registration form")
root.geometry("300x400")

file_path=r"C:\Users\sksha\OneDrive\Documents\registration.xlsx"
A=openpyxl.load_workbook(file_path)
B=A["Registration"]

# Validation functions
def is_valid_name(name):
    # Allows only letters (uppercase/lowercase) and spaces
    return re.fullmatch(r'[A-Za-z ]+', name.strip())
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Submit function
def handleSubmit():
    name = name_textbox.get()
    email = email_textbox.get()
    
    if not name or not email:
        messagebox.showwarning("Warning", "Please fill all the fields")
    elif not is_valid_name(name):
        messagebox.showerror("Error", "Name must contain only letters")
    elif not is_valid_email(email):
        messagebox.showerror("Error", "Please enter a valid email address")
    else:
        B.append([name, email])
        A.save(file_path)
        messagebox.showinfo("Status", "Data submitted successfully!")
        name_textbox.delete(0, tk.END)
        email_textbox.delete(0, tk.END)


# UI Elements
tk.Label(root, text="Name:").pack(anchor=tk.W, padx=10)
name_textbox = tk.Entry(root)
name_textbox.pack(anchor=tk.W, padx=10)

tk.Label(root, text="Email:").pack(anchor=tk.W, padx=10)
email_textbox = tk.Entry(root)
email_textbox.pack(anchor=tk.W, padx=10)

submit_button = tk.Button(root, text="Submit", command=handleSubmit)
submit_button.pack(anchor=tk.W, padx=10)


root.mainloop()