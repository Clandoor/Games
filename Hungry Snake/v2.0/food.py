from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()

        # Changing the size of the object by half.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')

        # Setting up the speed to fastest so we don't have to see the transition of it to another position.
        self.speed('fastest')
        self.relocate_food()

    def relocate_food(self):
        """
        Changes the x coordinate and the y coordinate inside the plane so that the food changes its
        location once the snake has made contact with the food in game.
        :return: None
        """
        random_x_coordinate = random.randint(-280, 280)
        random_y_coordinate = random.randint(-280, 280)
        self.goto(random_x_coordinate, random_y_coordinate)
