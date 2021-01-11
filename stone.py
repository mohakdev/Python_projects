import random
from tkinter import Tk , Label , Button , DISABLED , NORMAL , messagebox

# Disclaimer:
# The code you're about to see is 
# is from a work-in-progress version of the code.
# Everything you see is potentially subject to change. 
root = Tk()
root.geometry("800x400")
root.resizable(False , False)
root.title("ROCK , PAPER , SCISSORS")
root.iconbitmap(r"C:\Users\pramo\Desktop\CODING\STONE.ico")
#Defining all functions here
Computer_Score = 0
Player_Score = 0
run_not =5
def game_start(player_choice):
    global run_not
    global Computer_Score
    global total_score
    global Player_Score
    global status
    global rock
    global paper
    global scissors
    global computer_choice_label
    run_not = 10
    all_choices = ['ROCK','PAPER','SCISSORS']
    computer_choice = random.choice(all_choices)
    computer_choice_label = Label(root , text = computer_choice , font = 400)
    computer_choice_label.place(x = 600 , y=180)
    rock["state"]=DISABLED
    paper["state"]=DISABLED
    scissors["state"]=DISABLED
    if player_choice=='rock' and computer_choice =='ROCK':
        # Start coding from here.
        Player_Score +=0
        Computer_Score += 0
        total_score = Label(root , text = str(Player_Score)+'|'+str(Computer_Score ),font=100 )
        total_score.place(x = 380 , y = 150)
        status = Label(root , text = "it's a TIE" , font = 100)
        status.place( x=300 , y= 340)
    elif player_choice=='rock' and computer_choice =='PAPER':
        # Start coding from here.
        Player_Score +=0
        Computer_Score += 1
        total_score = Label(root , text = str(Player_Score)+'|'+str(Computer_Score ),font=100 )
        total_score.place(x = 380 , y = 150)
        status = Label(root , text = "YOU LOSE" , font = 100)
        status.place( x=300 , y= 340)
    elif player_choice=='rock' and computer_choice =='SCISSORS':
        # Start coding from here.
        Player_Score +=1
        Computer_Score += 0
        total_score = Label(root , text = str(Player_Score)+'|'+str(Computer_Score ),font=100 )
        total_score.place(x = 380 , y = 150)
        status = Label(root , text = "YOU WON" , font = 100)
        status.place( x=300 , y= 340)
    elif player_choice=='paper' and computer_choice =='ROCK':
        # Start coding from here.
        Player_Score +=1
        Computer_Score += 0
        total_score = Label(root , text = str(Player_Score)+'|'+str(Computer_Score ),font=100 )
        total_score.place(x = 380 , y = 150)
        status = Label(root , text = "YOU WON" , font = 100)
        status.place( x=300 , y= 340)
    elif player_choice=='paper' and computer_choice =='PAPER':
        # Start coding from here.
        Player_Score +=0
        Computer_Score += 0
        total_score = Label(root , text = str(Player_Score)+'|'+str(Computer_Score ),font=100 )
        total_score.place(x = 380 , y = 150)
        status = Label(root , text = "It's a TIE" , font = 100)
        status.place( x=300 , y= 340)
    elif player_choice=='paper' and computer_choice =='SCISSORS':
        # Start coding from here.
        Player_Score +=0
        Computer_Score += 1
        total_score = Label(root , text = str(Player_Score)+'|'+str(Computer_Score ),font=100 )
        total_score.place(x = 380 , y = 150)
        status = Label(root , text = "YOU LOSE" , font = 100)
        status.place( x=300 , y= 340)
    elif player_choice=='scissors' and computer_choice =='ROCK':
        # Start coding from here.
        Player_Score +=0
        Computer_Score += 1
        total_score = Label(root , text = str(Player_Score)+'|'+str(Computer_Score ),font=100 )
        total_score.place(x = 380 , y = 150)
        status = Label(root , text = "YOU LOSE" , font = 100)
        status.place( x=300 , y= 340)
    elif player_choice=='scissors' and computer_choice =='PAPER':
        # Start coding from here.
        Player_Score +=1
        Computer_Score += 0
        total_score = Label(root , text = str(Player_Score)+'|'+str(Computer_Score ),font=100 )
        total_score.place(x = 380 , y = 150)
        status = Label(root , text = "YOU WON" , font = 100)
        status.place( x=300 , y= 340)
    elif player_choice=='scissors' and computer_choice =='SCISSORS':
        # Start coding from here.
        Player_Score +=0
        Computer_Score += 0
        total_score = Label(root , text = str(Player_Score)+'|'+str(Computer_Score ),font=100 )
        total_score.place(x = 380 , y = 150)
        status = Label(root , text = "It's a TIE" , font = 100)
        status.place( x=300 , y= 340)
def restart():
    global run_not
    if run_not == 5:
        messagebox.showinfo("Null Value","You didn't select rock,paper or scissors")
    run_not=5
    global status
    global total_score
    global computer_choice_label
    global rock
    global paper
    global scissors
    computer_choice_label.place_forget()
    status.place_forget()
    total_score.place_forget()
    rock["state"]=NORMAL
    paper["state"]=NORMAL
    scissors["state"]=NORMAL   

#Defining all widgets  here

rock = Button(root , text = "ROCK" , padx = 20 , pady =8 ,command =lambda : game_start('rock'))
paper = Button(root , text = "Paper", padx = 20 , pady =8,command =lambda : game_start('paper') )
scissors = Button(root , text = "Scissors", padx = 20 , pady =8,command =lambda : game_start('scissors') )
Score_label = Label(root , text = "SCORE" , font= 100)
computer_label = Label(root , text = "COMPUTER CHOICE" , font= 100)
choose_label = Label(root , text = "SCORE" , font= 100)
play_again = Button(root , text = "PLAY AGAIN" , padx = 370 , pady = 40 , command = restart)
#creating all widgets  here
rock.place(x = 0 , y=160)
paper.place(x = 0 , y=200)
scissors.place(x = 0 , y=240)
Score_label.place(x = 360 , y=100)
computer_label.place(x = 600 , y=100)
choose_label.place(x = 0 , y=100)
play_again.place(x = 0 , y=0)





root.mainloop()