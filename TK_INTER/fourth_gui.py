# in this code we will check the user fill all the fields of registraion form or not
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Registration form")
root.geometry("300x400")

def handleSubmit():
    name= name_textbox.get()
    email= email_textbox.get()
    
    if name and email:
        messagebox.showinfo("Status", "Data Submitted successfully !")
    else:
        messagebox.showwarning("warning", "Please fill all the fields")

name_lable= tk.Label(root, text="Name:")
name_lable.pack(anchor=tk.W, padx=10)
# creating a textbox 
name_textbox=tk.Entry(root)
name_textbox.pack(anchor=tk.W, padx=10)

email_lable= tk.Label(root, text="Email:")
email_lable.pack(anchor=tk.W, padx=10)
# creating a textbox 
email_textbox=tk.Entry(root)
email_textbox.pack(anchor=tk.W, padx=10)

# creating a button
submit_button= tk.Button(root, text="Submit", command=handleSubmit)
submit_button.pack(anchor=tk.W, padx=10)


root.mainloop()