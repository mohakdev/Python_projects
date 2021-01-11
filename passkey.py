import webbrowser
def main():
    server=open("passkeydb.txt","r")
    check=input("Type your passkey to enter the server: ")
    sell=str(server.read())
    if sell==check:
        webbrowser.open_new_tab('file:///C:/Users/pramo/Desktop/Programming/Python-files/passkey.html')
    else:
        webbrowser.open_new_tab('file:///C:/Users/pramo/Desktop/Programming/Python-files/passkey1.html')
main()

