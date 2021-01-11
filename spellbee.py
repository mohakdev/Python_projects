import random
import gtts
from playsound import playsound
from tkinter import Label , Button , Tk , DISABLED , NORMAL
root = Tk()
def spellbee():
    lst=['GLADIOLUS','ALBUMEN','PROMISCUOUS','auxiliary','clique','capricious','elicit','drudgery','dormitory','hypocrisy','malicious','oblique','sabotage','vengeance','vulnerable','versatile','accompaniment','accomplice','ambassador']
    global spelling
    spelling=random.choice(lst)

    bee=gtts.gTTS(spelling)
    vice=gtts.gTTS("I repeat"+spelling , slow=True)
    bee.save("spellbee_1.mp3")
    vice.save('spellbee_2.mp3')
    playsound("spellbee_1.mp3")
    playsound("spellbee_2.mp3")
def spell_tick():
    global see 
    see = Label(root , text = spelling)
    see.pack()
def delete_all():
    see.pack_forget()
introduc = Label (root , text = "Press the button to get a random dictation word")
click = Button (root , text = "click to get a random text" , command = spellbee)
spell_check = Button(root , text = "click to see the spelling. " , command = spell_tick)
delete = Button(root , text = "delete all text. " , command = delete_all)
introduc.pack()
click.pack()
spell_check.pack()
delete.pack()

root.mainloop()




