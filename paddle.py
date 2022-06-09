# this will be the paddle module
from turtle import *

# making the paddle class (inherits from the turtle class)
class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__() # this line of code will initialize all the attributes of the turtle class and the methods
        self.color('white') # making the color of the paddle -> white
        self.shape('square') 
        self.shapesize(stretch_wid=5, stretch_len=1) # stretching the shape of the turtle to make it look like a paddle
        self.penup() # if the paddle moves in directions, it won't make marks
        self.goto(position) # defining to go to a new co-ordinate

    # paddle will go up/down listening to the key press
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    