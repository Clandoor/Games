import random
from turtle import Turtle

LIST_OF_COLORS = ['skyblue', 'white', 'gray', 'gold', 'cyan']
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    This class is the Turtle class which the player is controlling to cross the road.
    """
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color(random.choice(LIST_OF_COLORS))
        self.penup()
        self.reset_player_position()
        self.setheading(90)

    def move_up(self):
        """
        The following function makes the turtle move up when the key press is detected.
        :return: None
        """
        self.forward(MOVE_DISTANCE)

    def reset_player_position(self):
        """
        This function resets the player's position whenever it reaches at the finish line.
        :return: None
        """
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self) -> bool:
        """
        This function checks whether the turtle has reached finish line or not (Successful crossing without
        colliding with any car).
        :return: boolean
        """
        if self.ycor() > 290:
            return True
        else:
            return False

    def change_player_color(self):
        """
        Changes the color of the player turtle by getting random value from the list. Invoked when player
        has successfully reached the other side of the road.
        :return: None
        """
        self.color(random.choice(LIST_OF_COLORS))
