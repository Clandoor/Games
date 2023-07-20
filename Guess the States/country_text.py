from turtle import Turtle


class CountryText(Turtle):
    """
    This Class will manage each instance of the turtle text displayed on the screen and do appropriate
    actions based on it.
    """
    def __init__(self, x_cor, y_cor, state_name):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_cor, y_cor)
        self.write(arg=state_name)
