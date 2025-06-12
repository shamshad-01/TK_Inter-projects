import tkinter
root=tkinter.Tk()
root.title("Registration form")

name_lable= tkinter.Label(root, text="Name:")
name_lable.pack()
# creating a textbox 
name_textbox=tkinter.Entry(root)
name_textbox.pack()

email_lable= tkinter.Label(root, text="Email:")
email_lable.pack()
# creating a textbox 
email_textbox=tkinter.Entry(root)
email_textbox.pack()

# creating a button
submit_button= tkinter.Button(root, text="Submit")
submit_button.pack()


root.mainloop()