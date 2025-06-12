# in this code we have used an action by clicking on the submit button  
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Registration form")
root.geometry("300x400")

def handleSubmit():
    name= name_textbox.get()
    email= email_textbox.get()
    messagebox.showinfo("Captured data", name)
    # messagebox.showinfo("Captured data", email)

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