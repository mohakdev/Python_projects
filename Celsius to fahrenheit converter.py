from tkinter import Button , Tk , Entry , Label , LabelFrame

root = Tk()
root.geometry("260x130")
root.resizable(False, False)
root.title("Celsius to fahrenheit converter")

# Defining all functions here
def processing():
    global Celsius
    global fahrenheit
    if Celsius.get() =="" and fahrenheit.get() == "":
        empty = Label(root , text = "Please enter only a no.")
        empty.grid(row = 5, column =0)
    elif Celsius.get()=="":
        answer = (int(fahrenheit.get())-32)*5/9
        Celsius.insert(0,answer)
    elif fahrenheit.get()=="":
        answer = (int(Celsius.get())*9/5)+32
        fahrenheit.insert(0,answer)
    elif type(Celsius.get()) ==str :
        int_error = Label(root , text = "ONLY integers allowed")
        int_error.grid(row = 4 , column = 0) 
    elif type(fahrenheit.get()) ==str :
        int_error = Label(root , text = "ONLY integers allowed")
        int_error.grid(row = 4, column = 2) 
# Defining all widgets here
Celsius = Entry(root)
fahrenheit = Entry(root)
Celsius.insert(0,"CELSIUS")
fahrenheit.insert(0 , "FAHRENHEIT")
frame = LabelFrame(root , padx = 3 , pady = 3)
window_error = Label(frame , text = "---------------ERROR WINDOW---------------")

convert = Button(root , text = "CONVERT", padx = 100 , command = processing)
# Creating all widgets here
Celsius.grid(row = 0 , column =0)
fahrenheit.grid(row = 0 , column =1)
convert.grid(row = 2 , column =0 , columnspan = 2)
frame.grid(row = 3, column =0 , padx = 0 , pady = 1 , columnspan = 2)
window_error.pack()

root.mainloop()