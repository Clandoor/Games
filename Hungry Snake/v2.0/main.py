from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Screen will start listening to the user inputs so the snake's direction can be changed by user.
screen.listen()

# These are the keys which will get detected and functions associated with it will get executed.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Setting up the aspect ratio of the screen.
screen.setup(width=600, height=600)

screen.bgcolor('black')
screen.title("Hungry Snake")

# Turns the animation off, but until we call the update method, the screen is not going to refresh.
screen.tracer(0)

game_is_on = True

while game_is_on:
    """ If update is used right now, then all the segments of snakes are moved and then the screen is updated.
    It will look like the entire snake moving as a whole by x units. So when the screen is refreshed, the
    snake is already moved by x unit/s ahead."""
    screen.update()

    time.sleep(0.1)
    snake.move()

    # Detecting collision with the food. distance() returns the distance between the Turtle objects.
    # If it is visually touching it, then we can say that snake's head collided with the food.
    if snake.snake_head.distance(food) < 15:
        scoreboard.increase_scoreboard()
        food.relocate_food()
        snake.extend_snake()

    # Detecting collision with the wall.
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        # game_is_on = False
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detecting collision with the tail.
    for segment in snake.snake_segments[1:]:

        # For rest of the elements, we can this condition.
        if snake.snake_head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
