from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT, UP, DOWN, LEFT = 0, 90, 270, 180


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_segments = []
        self.create_snake()

        # After create_snake() because without executing it, snake_segments will be empty.
        # Storing first element of snake_segments in a variable as is needed quite often.
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        """
        Creates three initial segments / blocks of the snakes and assigns them to their respective positions
        based on the tuples in 'starting_positions' list.
        :return: None
        """
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a new segment in the specific position in the snake body.
        :param position: Coordinates of the position passed (x, y).
        :return: None
        """
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend_snake(self):
        """
        When snake successfully makes contact with the food, this function will get called a new segment
        will be added behind the snake.
        :return: None
        """
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        """
        Gives the direction for the snake segments to move.
        Fetches the coordinates from the nearest segment and makes the current segment move to the adjacent
        segment's position to maintain the direction of all segments.
        :return: None
        """
        for segment_number in range((len(self.snake_segments) - 1), 0, -1):
            # Fetches the coordinates of the segment before the current segment.
            new_x_cor = self.snake_segments[segment_number - 1].xcor()
            new_y_cor = self.snake_segments[segment_number - 1].ycor()

            # Passing those coordinates in goto() to move the current segment in last segment's position.
            self.snake_segments[segment_number].goto(new_x_cor, new_y_cor)

        # Making sure the first segment moves after the iteration to start the chain movement.
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Sets the heading of the first segment to 90 degrees (Pointing upwards) so the first segment / head
        can change its direction followed by change in direction of other segments after it.
        Also makes sure that the snake cannot go in opposite direction relative to the current direction.
        :return: None
        """
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """
        Sets the heading of the first segment to 270 degrees (Pointing downwards) so first segment / head
        can change its direction followed by change in direction of other segments after it.
        Also makes sure that the snake cannot go in opposite direction relative to the current direction.
        :return: None
        """
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        """
        Sets the heading of the first segment to 180 degrees (Pointing left) so the first segment / head
        can change its direction followed by change in direction of other segments after it.
        Also makes sure that the snake cannot go in opposite direction relative to the current direction.
        :return: None
        """

        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        """
        Sets the heading of the first segment to 0 degrees (Pointing right) so the first segment / head
        can change its direction followed by change in direction of other segments after it.
        Also makes sure that the snake cannot go in opposite direction relative to the current direction.
        :return: None
        """
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

