from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "lightgreen"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """
    This class will generate all the random cars and move them across the screen.
    """
    def __init__(self):
        super().__init__()
        self.list_of_cars = []
        self.accelerate = 0

    def create_car(self):
        """
        This function creates cars with 1/6 probability and then adds those cards in the list of cars.
        :return: None
        """

        # This ensures that the screen is not flooded with the cars.
        probability = random.randint(1, 6)
        if probability == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_position = (300, random.randint(-250, 250))
            new_car.goto(random_position)
            self.list_of_cars.append(new_car)

    def move_car(self):
        """
        This function iterates through the list of cars and then makes each car move in a specific
        direction.
        :return: None
        """
        for car in self.list_of_cars:
            car.backward(STARTING_MOVE_DISTANCE + self.accelerate)

    def increase_car_speed(self):
        """
        This function increases the class' attribute by certain amount which is then further added in
        the move distance of car to increase the car speed overall visually.
        :return: None
        """
        self.accelerate += 2
