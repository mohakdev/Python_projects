from tkinter import Label , Button , Entry , Tk 
root = Tk()
root.title("Leap year program")
#Defining all functions here
def clicked():
    try:
        global answer
        year = int(data.get())
        if year%4==0:
            answer =Label(root , text = "Yes the year is a leap year")
            answer.pack()
        else:
            answer = Label(root , text = "No the year is not a leap year")
            answer.pack()
    except ValueError:
        error=Label(root,text = "Only excepts a number")
        error.pack()
def delete_func():
    answer.pack_forget()

# Defining all things here.
intro = Label(root , text = "Enter the year in the textbox and click the button to see if the year is a leap year or not.")
data = Entry(root, width = 20)
check_button = Button(root , text = "Check to see if a loop year or not." , fg = "red" , command = clicked)
delete_button = Button(root, text = "Delete all results" , command =delete_func)
# Packing all things into the screen here.
intro.pack()
data.pack()
check_button.pack()
delete_button.pack()
root.mainloop()