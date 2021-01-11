from tkinter import *
root = Tk()

Menu_Items = [
    ("Pizza",'pizza'),
    ('Burger','burger'),
    ('Sandwich','sandwich'),
    ('Pasta','pasta')
]
Pizza = StringVar()
Pizza.set("Pizza")

for item , store in Menu_Items:
    Radiobutton(root , text = item, variable = Pizza , value = store).pack()

def clicked(values):
    mylabel = Label(root , text = values).pack()
    root.mainloop()
# Radiobutton(root , text = "Option 1 " , variable = r ,value = 1 , command = lambda: clicked(1)).pack()
# Radiobutton(root , text = "Option 2" , variable = r ,value = 2 , command = lambda: clicked(2)).pack()
my_button = Button(root, text="confirm" , command = lambda: clicked(Pizza.get()))
my_button.pack()
root.mainloop()