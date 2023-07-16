from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

main_screen = Screen()
main_screen.bgcolor('black')
main_screen.setup(width=800, height=600)
main_screen.title("PONG")

# Turning off the animation, so we don't see the paddles moving in their designated position.
main_screen.tracer(0)

# Here, we pass a tuple which is then further referenced to 'position' variable inside the class.
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Screen will start listening to the user inputs so the snake's direction can be changed by user.
main_screen.listen()
main_screen.onkey(right_paddle.move_up, "Up")
main_screen.onkey(right_paddle.move_down, "Down")
main_screen.onkey(left_paddle.move_up, "w")
main_screen.onkey(left_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)

    # Refreshing / Updating the screen so the paddles are already there in their position.
    main_screen.update()
    ball.move_ball()

    # Detecting collision with the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    # Detecting collision with the paddles.
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_ball_x()

    # Keeping both the conditions separate to calculate the score at a specific side.
    # Detect when the ball misses the right paddle.
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_ball_x()
        scoreboard.increment_left_score()
        scoreboard.update_scoreboard()

    # Detect when the ball misses the left paddle.
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_ball_x()
        scoreboard.increment_right_score()
        scoreboard.update_scoreboard()

main_screen.exitonclick()
