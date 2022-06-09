# all score related code will be updated here
from turtle import Turtle

# font constants
FONT = ("Courier", 80, "normal")

# creating the scoreboard class (inherits from the turtle class)
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('#fff')
        self.penup()
        self.hideturtle()
        self.l_score = 0 # left player score
        self.r_score = 0 # right player score
        self.update_scoreboard()
        
    # updating the scoreboard everytime a player gets a point
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,240)
        self.write(self.l_score, align='center', font=FONT)
        self.goto(100,240)
        self.write(self.r_score, align='center', font=FONT)
        
    # players getting the points
    def l_point(self):
        self.l_score += 1 # left player gets the point
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score += 1 # right player gets the point
        self.update_scoreboard()