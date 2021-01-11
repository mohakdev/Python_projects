from tkinter import  Tk , Label , Entry , Button
# Work in progress

# Work in progress
root = Tk()
root.title("Password manager")
service = Entry(root, width = 30)
mainacc = Entry(root , width =30)
youtube = Entry(root , width =30)
service.grid(row = 1 , column = 0 )
mainacc.grid(row = 1 , column = 1 )
youtube.grid(row = 1 , column = 2 )
service.insert(0,"Enter service name : ")
mainacc.insert(1,"Enter main account password: ")
youtube.insert(2,"Enter youtube account : ")
def execute():
    dbfile=open('manage-password.txt','a')
    dbfile.write('\n'+'--------------------------'+'\n')
    dbfile.write('Service        Main account password         Youtube account password'+'\n')
    dbfile.write(service.get()+'              '+mainacc.get()+'                '+youtube.get())
    dbfile.close()
submit= Button(root , text = "Submit" , command = execute)
submit.grid(row = 2 , column = 0)
def clear():
    dbfile=open('manage-password.txt','w')
    dbfile.truncate()
    dbfile.close()
clear_all = Button(root , text = "Clear all data" , command = clear)
clear_all.grid(row = 2 , column = 1)
def view():
    dbfile=open('manage-password.txt','r')
    view_data = Label(root , text = dbfile.read())
    view_data.grid(row = 3 , column = 0)
    dbfile.close()
view_entries = Button(root , text = "View all data" , command = view)
view_entries.grid(row = 2 , column = 2)
root.mainloop()



