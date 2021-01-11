from tkinter import Tk , Label , Button , Entry
import webbrowser
#learning tkinter
root=Tk()
# Work in progress
title = Label(root , text = "write website name in the textbox")
title.pack()


# Work in progress
name = Entry(root , width = 30)
name.pack()
def visit():
    if name.get()=='amazon':
        webbrowser.open_new_tab('https://www.amazon.in')
    elif name.get()=='flipkart':
        webbrowser.open_new_tab('https://www.flipkart.com')
    elif name.get()=='myntra':
        webbrowser.open_new_tab('https://www.myntra.com')
    elif name.get()=='ajio':
        webbrowser.open_new_tab('https://www.ajio.com')
    elif name.get()=='croma':
        webbrowser.open_new_tab('https://www.croma.com')
    elif name.get()=='medlife':
        webbrowser.open_new_tab('https://www.medlife.com')
    elif name.get()=='aliexpress':
        webbrowser.open_new_tab('https://www.aliexpress.com')
    elif name.get()=='tata cliq':
        webbrowser.open_new_tab('https://www.tatacliq.com')
    elif name.get()=='ebay':
        webbrowser.open_new_tab('https://in.ebay.com')
    elif name.get()=='bewakoof':
        webbrowser.open_new_tab('https://www.bewakoof.com')
    elif name.get()=='bigbasket':
        webbrowser.open_new_tab('https://www.bigbasket.com')
    elif name.get()=='':
        null_val = Label(root , text = "You didn't type anything")
        null_val.pack()
    else:
        webbrowser.open_new_tab('file:///C:/Users/pramo/Desktop/Programming/Web%20Devlopment/python_help.html')    
submit = Button(root , text = "submit" , command = visit , fg = "red" , bg = "violet")
submit.pack()
root.mainloop()