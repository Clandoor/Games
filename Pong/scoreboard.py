from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard making the text display again in order to make the score change visible on
        the main screen.
        :return: None
        """

        # Clearing the old score text / data on the screen before updating the score.
        self.clear()

        self.goto(-100, 200)
        self.write(self.left_score, align='center', font=("Courier ", 60, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align='center', font=("Courier ", 60, "normal"))

    def increment_left_score(self):
        """
        Increments the score of the left side by one unit if the right paddle misses the ball.
        :return: None
        """
        self.left_score += 1

    def increment_right_score(self):
        """
        Increments the score of the right side by one unit if the left paddle misses the ball.
        :return: None
        """
        self.right_score += 1
