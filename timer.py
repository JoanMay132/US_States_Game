#import this
from turtle import *
from time import *
from turtle import Screen


class Countdown(Turtle):

    def __init__(self):
        super().__init__()
        #create the turtle
        
      
        self.penup()
        
       
    def timer(self):
     
        self.count3=0
        self.speed(0)
        self.goto(0,260)
        #this is the loop
        for count2 in range(3):#replace the 3 with the number you want to count from
            count3 = 3 - count2
            self.clear()
            self.color("white")
            self.write(count3,align="center", font=("arial", 24, "normal"))
            sleep(1)

