from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.penup()
        self.move_speed = 0.1

    def move_ball(self):
        """
        Changes the x and y coordinate of the ball to make it look like moving forward.
        :return: None
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball_y(self):
        """
        This function reverses the direction of the specific variable so the ball moves away from the
        wall.
        :return: None
        """
        self.y_move *= (-1)

    def bounce_ball_x(self):
        """
        This function reverses the direction of the specific variable so the ball moves away from the
        wall.
        :return: None
        """
        self.x_move *= (-1)
        self.move_speed *= 0.9

    def reset_position(self):
        """
        This function resets the position of the ball back to center if it misses any paddles.
        :return: None
        """
        self.goto(0, 0)

        # Resetting the move speed to the original value whenever it misses the paddles.
        self.move_speed = 0.1
