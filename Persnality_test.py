import random
def ask():
    print("Which avenger you are:")
    fav_quality=input("What is your favorite quality in yourself?")
    weekness=input("What's your greatest weakness?")
    friends=input("How would your friends describe you?")
    power=input("If you could have any super power for a day, what would you choose?")
    fear=input("What's your greatest fear?")
    print(fav_quality)
    print(weekness)
    print(friends)
    print(power)
    print(fear)
    print("you selected these and the result is")
ask()

def output(you):
    avenger=random.choice(you)
    print(avenger)
    if avenger=='Hawkeye':
        print('''Introverted, Observant, Thinking, and Assertive
        .Hawkeye is strongly Introverted, solidly grounded in the real 
        world of an Observant personality, and a logical Thinking type.''')
    if avenger=='Iron Man':
        print('''Iron man is strongly willful, doesn't work well with any authority 
        other than his own, and will enthusiastically tear down just 
        about anyone who challenges him. He's complicated, 
        a little self-absorbed, and sometimes moody.''')
    if avenger=='Captain America':
        print(''' He is honest, up-front, loyal, extremely noble, and unfailingly dependable.
        His strengths don’t lie in creativity or brilliance, especially when compared to some 
        other Avengers, but he is the one who can step in and lead all the complex 
        personalities,skill sets, strengths, and weaknesses of this diverse team.''')
    if avenger=='Wanda':
        print('''Wanda is a serious and introverted individual with emotional fragility due to
        her upbringing. At her core, however, Wanda has a caring personality devoted to protecting
        innocents, and a willingness to fight for what she feels is right.''')            
    if avenger=='Vision':
        print(''' Vision wouldn’t immediately strike anyone as a powerful being. He’s eerily calm
        and mostly unmoved by emotions. He prefers to think through all possible options and then
        follow the most logical path. And rather than hide his thought process, he’s incredibly
        open and honest about his opinions.''')
    if avenger=='Spider man':
        print('''Peter exhibits behaviors of caring, kindness, loyalty, bravery, fear, worry, and 
        intelligent. His behaviors are most ifluenced by his environment. Peter exhibits more left
        brain activity as he uses his knowledge to assess his situations. His behavior is more of a
        result of his personality disordor.''')
    if avenger=='Black Widow':
        print('''Black Widow's personality is pretty consistent: she's resourceful, practical,
        doesn't back down,has some serious emotional walls in place but usually finds it 
        relatively easy to get along with people once she's gotten to know them.
        Her skills follow a pretty similar pattern.''')
output(you=['Hawkeye','Iron Man','Captain America','Wanda','Vision','Spider man','Black Widow'])
def call():
    inp=input("Want to run the program again y/any other key: ")
    while inp=='y':
        ask()
        output(you=['Hawkeye','Iron Man','Captain America','Wanda','Vision','Spider man','Black Widow'])
        inp=input("Want to run the program again y/any other key: ")
        if inp=='n':
            break 
    if inp=='n':
        pass
    else:
        print("exiting the program in 3,2,1")
call()