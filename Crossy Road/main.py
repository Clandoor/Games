import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

LIST_OF_COLORS = ['maroon', 'navy', 'darkgreen', 'brown', 'black', 'purple', 'turquoise',
                  'chocolate']

main_screen = Screen()
main_screen.setup(width=600, height=600)
main_screen.title("Crossy Road")
main_screen.bgcolor('black')
main_screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

main_screen.listen()
main_screen.onkey(player.move_up, 'Up')

game_is_on = True
count_iterations = 0
list_of_cars = []

while game_is_on:
    time.sleep(0.1)
    main_screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detecting the collision with the car.
    for car in car_manager.list_of_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.display_game_over()

    # Detecting when the turtle reaches the finish line.
    if player.is_at_finish_line():
        player.reset_player_position()
        car_manager.increase_car_speed()
        scoreboard.increment_level()
        main_screen.bgcolor(random.choice(LIST_OF_COLORS))
        player.change_player_color()

main_screen.exitonclick()
