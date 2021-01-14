from tkinter import *
from tkinter import messagebox
root = Tk()
root.resizable(False, False)
root.title("All in one converter")
# Disclaimer:
# The code you're about to see is 
# is from a work-in-progress version of the code.
# Everything you see is potentially subject to change. 
# Defining all functions here
def def_area():
    types = Toplevel()    
def def_mass():
    types = Toplevel()    
def def_temp():
    global cel_entry
    global fah_entry
    def submit_temp():
        if cel_entry.get()== "" and fah_entry.get()== "":
            messagebox.showwarning("Both empty","Both of the null values are empty")
        if cel_entry.get() !="" and fah_entry.get()=="":
            cel_formula = celsius_entry.get()
    types = Toplevel()
    types.resizable(False, False)

    celsius_label = Label(types , text = "Celsius").grid(row = 0, column = 0)
    fahrenheit_label = Label(types , text = "fahrenheit").grid(row = 0, column = 1)
    celsius_entry = Entry(types , textvariable = cel_entry).grid(row = 1, column = 0)
    fahrenheit_entry = Entry(types, textvariable = fah_entry).grid(row = 1, column = 1)
    submit = Button(types , text = "SUBMIT" , command = submit_temp , padx = 40).grid(row = 2, column = 0 , columnspan = 2 , )
def def_curren():
    pass
# Defining widgets 
cel_entry = StringVar()
fah_entry = StringVar()
area = Button(root , text = "AREA" , command = def_area , padx = 81).pack()
mass = Button(root , text = "MASS" , command = def_mass , padx = 80).pack()
temp = Button(root , text = "TEMPERATURE" , command = def_temp , padx = 57).pack()
curren = Button(root , text = "CURRENCY" , command = def_curren , padx = 66).pack()


root.mainloop()