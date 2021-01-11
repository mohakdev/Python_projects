def tell():
    wht=input("Want to create a new list or access old list: ")
    wht=wht.lower()
    if wht=="new list":
        outfile=open("Taskerdb.txt","w")
        num=int(input("No of tasks-"))
        if num==1:
            task=input("Write Task no.1: ")
            outfile.write(task + '\n')
        elif num==2:
            task=input("Write Task no.1: ")
            task2=input("Write Task no.2: ")
            outfile.write(task + '\n')
            outfile.write(task2 + '\n')
        elif num==3:
            task=input("Write Task no.1: ")
            task2=input("Write Task no.2: ")
            task3=input("Write Task no.3: ")
            outfile.write(task + '\n')
            outfile.write(task2 + '\n')
            outfile.write(task3 + '\n')
            #Till here program works fine
            #no change req.
    elif wht=="access old list":        #Problem is it is not able to load data from db11.txt
        #solve it
        outfile=open("Taskerdb.txt","r")
        print(outfile.read())
        outfile.close()
    else:
        print("Error found")        
tell()                      