# all ball related code will be performed here 
from turtle import Turtle

# creating the ball class (inherits from the turtle class)
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('yellow')
        self.shape('circle')
        
    # moving the ball in a direction
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)