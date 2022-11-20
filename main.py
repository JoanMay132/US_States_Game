import turtle
import pandas as pd
from time import sleep
from timer import Countdown
screen= turtle.Screen()
screen.bgpic("blank_states_img.gif") #background image
screen.bgcolor("black") #change background color
time= Countdown()
#FONTS
FONT2=("Arial",20,'normal','bold','italic','underline')

#Read data
data= pd.read_csv("50_states.csv")
#convert into a list
states=data.state.to_list() #convert into a list
score=0

while score<50:
    time.timer() #start timer
    #Ask user to guess
    guessing= screen.textinput(title=f"{score}/50 Guess the state",prompt="What's the next state?").title() #title() capitalizes the first letter of each word
    
    if guessing in states: #if the user guess is in the list
        t=turtle.Turtle() #create a turtle
        t.hideturtle() 
        t.penup() #lift the pen
        state_data=data[data.state==guessing] #get the data of the state
        t.goto(int(state_data.x), int(state_data.y)) #go to the coordinates of the state
        t.write(guessing,align="center",font=("arial",9)) #write the name of the state
        score+=1 #add 1 to the score
    elif guessing not in states: #if the user guess is not in the list
        t=turtle.Turtle() #create a turtle
        t.hideturtle()
        t.penup()
        t.goto(0,100) #go to the coordinates of the state
        t.write("Incorrecto, intenta de nuevo.",align="center",font=FONT2) #write the name of the state
        sleep(1)
        t.clear()
screen.mainloop()