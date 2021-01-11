def lot(user, v, y):
    import random
    x = random.randint(v, y)
    if x == user:
        print("congrats you won the lottery")
    else:
        print("sorry you lose the correct no. was-", x)
lot(user=int(input("type a random (between 1 to 7) no. to win lottery: ")), v=1, y=7,)


def play_again():
    call = 1
    while call<30:
        con=input("want to play again (y/any other key): ")
        con = con.lower()
        if con == 'y':
            lot(user=int(input("type a random (between 1 to 7) no. to win lottery: ")), v=1, y=7,)
        else:
            break
        
    call = call+1
play_again()

