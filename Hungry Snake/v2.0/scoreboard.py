from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Verdana", 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())

        self.color('white')
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def increase_scoreboard(self):
        """
        Whenever the snake_head collides with the food instance, this method will be called, and it will
        succinctly increase the value of score by one unit.
        :return: None
        """
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Displays the score and the text on the top middle of the screen.
        :return: None
        """
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        """
        This function resets the current score if the user fails in the game.
        :return: None
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file_pointer:
                file_pointer.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """
    #     Displays the Game Over message once the game is over. Game is over when certain conditions are met.
    #     :return: None
    #     """
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
