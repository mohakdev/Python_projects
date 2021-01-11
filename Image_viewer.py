from tkinter import Tk , Button , Entry , Label , Image
from PIL import ImageTk , Image
root = Tk()
root.title("Image viewer app")
root.iconbitmap(r'C:\Users\pramo\Desktop\CODING\APP_development\favicon.ico')
img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\pramo\Desktop\CODING\Untitled design (4).png"))
img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\pramo\Desktop\CODING\Untitled design (5).png"))
img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\pramo\Desktop\CODING\Untitled design (7).png"))

image_lib =[img1 , img2 , img3]

img_label = Label(root, image = img1)
img_label.grid(row = 0 , column = 0 , columnspan = 2)

image_numb = 0
def back_func():
    global img_label
    global back_button
    global next_button
    global image_numb
    image_numb-=1
    img_label.grid_forget()
    if image_numb==-1:
        image_numb=2
    img_label = Label(root, image = image_lib[image_numb])
    img_label.grid(row = 0 , column = 0 , columnspan = 2)
def next_func():
    global image_numb
    global img_label
    global back_button
    global next_button
    image_numb+=1
    img_label.grid_forget()
    if image_numb==3:
        image_numb=0
    img_label = Label(root, image = image_lib[image_numb])
    img_label.grid(row = 0 , column = 0 , columnspan = 2)


back_button = Button(root , text = "PREVIOUS" , padx = 45 , command= back_func)
next_button = Button(root , text = "NEXT", padx = 55 , command=next_func)

back_button.grid(row = 1 , column = 0)
next_button.grid(row = 1 , column = 1)


root.mainloop()