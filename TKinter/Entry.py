from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text="I clicked the Button")
    myLabel.pack()

#myButton = Button(root, text = "Click Me", padx=20, pady=20, command=myClick, fg="purple")
myButton = Button(root, text = "Click Me", command=myClick, fg="purple", bg="yellow")
myButton.pack()

root.mainloop()

