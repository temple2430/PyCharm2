from tkinter import *

root = Tk()

e = Entry(root,borderwidth=5)
e.pack()
e.insert(0, "Enter your Name")

def myClick():
    Hello = "Hello " + e.get()
    myLabel = Label(root,text=Hello)
    myLabel.pack()

#myButton = Button(root, text = "Click Me", padx=20, pady=20, command=myClick, fg="purple")
myButton = Button(root, text = "Enter your name", command=myClick, fg="purple", bg="yellow")
myButton.pack()

root.mainloop()

