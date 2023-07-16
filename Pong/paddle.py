from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        """
        Moves the paddle upside by constantly incrementing the y coordinate by certain amount whenever
        the function is invoked.
        :return: None
        """
        new_y_coordinate = self.ycor() + 20
        self.goto(self.xcor(), new_y_coordinate)

    def move_down(self):
        """
        Moves the paddle down by constantly decrementing the y coordinate by certain amount whenever
        the function is invoked.
        :return: None
        """
        new_y_coordinate = self.ycor() - 20
        self.goto(self.xcor(), new_y_coordinate)
