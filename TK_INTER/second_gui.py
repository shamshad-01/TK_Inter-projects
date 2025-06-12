# in this code we have used some basic  styling on the page 
import tkinter
root=tkinter.Tk()
root.title("Registration form")
root.geometry("300x400")
root.configure(bg="green")   # to change the background color of the page 

name_lable= tkinter.Label(root, text="Name:")
name_lable.pack(anchor=tkinter.W, padx=10)
# creating a textbox 
name_textbox=tkinter.Entry(root)
name_textbox.pack(anchor=tkinter.W, padx=10)

email_lable= tkinter.Label(root, text="Email:")
email_lable.pack(anchor=tkinter.W, padx=10)
# creating a textbox 
email_textbox=tkinter.Entry(root)
email_textbox.pack(anchor=tkinter.W, padx=10)

# creating a button
submit_button= tkinter.Button(root, text="Submit")
submit_button.pack(anchor=tkinter.W, padx=10)


root.mainloop()