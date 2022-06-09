# importing the screen class to make an object
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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

# creating the scoreboard object for keeping track of the scores
scoreboard = Scoreboard()
    
# listening the screen to move the paddle up/down
screen.listen()
screen.onkeypress(right_paddle.go_up, 'i')
screen.onkeypress(right_paddle.go_down, 'k')
screen.onkeypress(left_paddle.go_up, 'w')
screen.onkeypress(left_paddle.go_down, 's')

# game will continue to run
game_on = True
while game_on:
    time.sleep(ball.move_speed) # reasonable speed (screen updates a little slower)
    screen.update() # swithing on the animation
    ball.move()
    
    # bouncing the ball (by hitting the wall)
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()
        
    # bouncing the ball by hitting the paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 470) or (ball.distance(left_paddle) < 50 and ball.xcor() < -470):
        ball.bounce_x()

    # if the paddles misses the balls..!
    # right-paddles misses the ball
    if ball.xcor() > 530:
        ball.reset_position()
        scoreboard.l_point()
    
    # left-paddles misses the ball
    if ball.xcor() < -530:
        ball.reset_position()
        scoreboard.r_point()
        
# screen will not be closed until we manually close it
screen.exitonclick()