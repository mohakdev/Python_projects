import New_lang as nl 
def call(what):
    what=what.lower()
    if what=="converted":
        nl.convert(input("enter the converted word: "))
    elif what=="english":
        nl.main(input("Enter the real word: "))
    else:
        print('Error')
call(input("In which language-converted,english: "))
