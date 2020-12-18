from tkinter import *

# Initiate Frame:
root = Tk()

# creating an imput box:
entry_test = Entry(root).pack()

# reset Canvas:
def button_test():
    myLabel = Label(root, text = entry_test.get()).pack()

# Write text to gui:
# myLabel = Label(root, text="Hello").grid(row=10, column=0)
# myLabel1 = Label(root, text="test").grid(row=1,column=10)

print_entry = Button(root, text="Reset Canvas", 
                     padx=50, pady=50, command=button_test).pack()

# Keeps Canvas updated:
root.mainloop()