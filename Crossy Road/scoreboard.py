from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    This class will keep a track of score and displaying the score. It will also be responsible for
    displaying game over message at the center of the screen when the player gets hit by a car.
    """
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 260)
        self.write("Level: " + str(self.level), font=FONT)

    def _update_scoreboard(self):
        """
        This function updates the level text by displaying it again to make the changes / updates visible
        on the main screen.
        :return: None
        """

        # Clearing the old text
        self.clear()
        self.write("Level: " + str(self.level), font=FONT)

    def increment_level(self):
        """
        This function increases the level attribute by one unit when the turtle successfully crosses the
        road without colliding with any car.
        :return: None
        """
        self.level += 1
        self._update_scoreboard()

    def display_game_over(self):
        """
        This function displays the 'Game Over' message when the player collides with the car.
        :return: None
        """
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)
