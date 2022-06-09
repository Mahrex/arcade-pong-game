# all ball related code will be performed here 
from turtle import Turtle

# creating the ball class (inherits from the turtle class)
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('yellow')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    # moving the ball in a direction
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    # bouncing back of the ball by hitting back the wall (reverses the y coordinate)
    def bounce_y(self):
        self.y_move *= -1 # we are just simply reversing the
        
    # bouncing back of the ball by hitting back the wall (reverses the x coordinate)
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        
    # reseting the position of the ball and starts by moving in the opposite direction
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()