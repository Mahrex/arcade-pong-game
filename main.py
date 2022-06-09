# importing the screen class to make an object
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time

# making the screen and further adjustments
screen = Screen() # creating a screen object
screen.bgcolor('#000000') # setting up the background color of the screen
screen.title('Pong Game') # setting up the title of the screen
screen.setup(width=1100, height=700) # setting up the dimensions of the screen
screen.tracer(0) # swithing off the animation


# creating two paddles from the paddle class
right_paddle = Paddle((500,0)) # creating the right paddle
left_paddle = Paddle((-500,0)) # creating the left paddle

# creating a ball object from the Ball class   
ball = Ball() 
    
# listening the screen to move the paddle up/down
screen.listen()
screen.onkeypress(right_paddle.go_up, 'Up')
screen.onkeypress(right_paddle.go_down, 'Down')
screen.onkeypress(left_paddle.go_up, 'w')
screen.onkeypress(left_paddle.go_down, 's')

# game will continue to run
game_on = True
while game_on:
    time.sleep(0.1) # reasonable speed (screen updates a little slower)
    screen.update() # swithing on the animation
    ball.move()


# screen will not be closed until we manually close it
screen.exitonclick()