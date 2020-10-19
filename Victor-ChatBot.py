
"""
This is a program for a chatbot named Victor
1. The victor will start with a greeting and self intro and ask for name of the person.
2. The boomer will wish the person and list the tasks
3. Victor do tasks such as calculating basic math operations, 2 mathematical tricks, a mini game.
4. Victor will respond to users input appropriately.
"""



import random
from datetime import datetime


def greeting_and_introduction():
    Menu = [
        "Welcome Buddy, This is Victor.",
        "Wonderful, It is so nice to be in touch with you. I am Victor"
    ]
    print(random.choice(Menu))
    
def get_timeofday_greeting():
    current_time = datetime.now()
    timeofday_greeting = "Good Morning"
    if current_time.hour > 12 and current_time.hour < 17:
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour >=17 and current_time.hour < 22:
        timeofday_greeting = "Good Evening"
    elif current_time.hour >=22:
        timeofday_greeting = "Hey! It's going to be late for Bedtime."
    print(timeofday_greeting)
    
def welcome(name):
    messages = [
        "Nice to meet you",
        "Lets have some good time together"
    ]
    print(f"{random.choice(messages)}",name)
    
def guess_num():
    print("Step 1:Take a number in 1-9")
    print("Step 2:Multiply it with 5 and add 5 to the answer")
    print("Step 3:Next u do multiply the answer with 2 and add 2 to it")
    ans=int(input("Enter ur final answer: "))
    if ans>=22:
        ans=ans//10
        ans-=1
        print("Your number is: ",ans) 
        if int(input("Enter the number you took: "))==ans: 
            print("Yes, I got ur number")
            print("Isnt it Funny haha :)") 
        else:
            print("Please calculate(((num*5)+5)*2+2) properly")
        print("...............................")
        if int(input("Try another one, enter 1, if not enter 0"))==1:
            print("Step 1:Take a number in 1-9")
            print("Step 2:Multiply it with 2 and add 100 to the answer")
            print("Step 3:Next u make the answer half and subtract the guess number from it")
            print("Your Final answer is 50") 
            if int(input("What did u get: "))==50: 
                print("I got you","\N{hugging face}")
                print("haha I think u liked it :)")
            else:
                print("Your answer is wrong, calculate again")
            print("...............................")
    else:
        print("Do the calculation properly...!")  
    if int(input("Enter 1 to play again or 0 to menu: "))==1:
        guess_num()
    else:
        victor()
        
def game(): 
    print("Lets play game") 
    print("Rock paper scissor")
    RPS = {1:"rock",
    2:"paper",
    3:"scissor"}
    rps=[1,2,3]
    print(RPS)
    points=0
    for i in range(0,3):
        x=int(input("enter any of three(1,2,3): "))
        r=random.choice(rps)
        print(r)
        if x==r:
            points+=1
        else: 
            points+=0 
    if points>=2: 
        print("Congrats! You won","\N{money-mouth face}") 
    else:
        print("You lose :-( ")
    if int(input("Enter 1 to play again or 0 to menu: "))==1:
        game()
    else:
        victor()
    
def show_menu(): 
    print("Here it is, What can i do for you","\U0001f600")
    print("1. Calculate an expression")
    print("2. Guessing the number") 
    print("3. Game ")
    print("4. End this chat")
    print("..................")
    try:
        return int(input("Enter your choice [1-4]: "))
    except:
        print("Only enter choice from 1, 2, 3,4")
        return 0
def evaluate_expression():
    expr = input("Enter an expression: ")
    try:
        print("Result:", eval(expr))
    except Exception as e:
        print(str(e)) 
    if int(input("Enter 1 to play again or 0 to menu: "))==1:
        evaluate_expression()
    else:
        victor()
        
greeting_and_introduction()
print("************")
name = input("Enter ur name: ") 
print(" ")
get_timeofday_greeting()
welcome(name)

def victor():
    print(" ")
    choice = show_menu()
    if choice != 4:
        if choice == 1:
            evaluate_expression()
        elif choice == 2: 
            print("Welcome to Mathematic magic","\U0001f600")
            guess_num()
        elif choice==3: 
            game()
        else:
            print("I dont understand that")
        print("...............................")
    else:
        print("If you want to again to do, enter 1 or to confirm ending enter 0:") 
        if int(input())==1: 
            victor() 
        else:
            print("Thanks for using the bot, see you soon","\N{winking face}")
            print("This bot is in development stage ")
            print("\N{relieved face}")
victor()
