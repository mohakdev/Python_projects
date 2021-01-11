import os
def rename():
    name=input("Enter the current name of the file: ")
    # path=input("Enter the path of the file")
    rename1=input("Enter the new name of the file: ")
    os.rename(name,rename1)
rename()
