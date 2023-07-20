import turtle
import pandas
from country_text import CountryText


# Setting up the proper image path.
IMAGE_PATH = "blank_states_img.gif"
MAX_SCORE = 50

main_screen = turtle.Screen()
main_screen.title("USA States Game")
main_screen.setup(width=1.0, height=1.0)


# Adding a new shape in the list of available shapes.
main_screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)


# Reading the data_frame.
data_frame = pandas.read_csv("50_states.csv")


game_continue = True
title = "Guess the State"
current_score = 0
correct_guesses = []

while game_continue:

    # If the user guessed the correct state, then this will store the row of that state.
    answer = main_screen.textinput(title=title, prompt="What's another state's name?").title()
    states_name = data_frame[data_frame["state"] == answer]
    print(states_name)

    # Converting the Series into a List.
    state_x_coordinate = states_name["x"].tolist()
    state_y_coordinate = states_name["y"].tolist()

    """ If the user's guess was not correct, then the generated list will be empty, so we continue the
    iteration of the loop and keep prompting the user. """
    if not state_x_coordinate:
        continue

    # If the user's answer was already guessed, then this will let them know.
    if answer in correct_guesses:
        main_screen.textinput(title=title, prompt=f"{answer} already Guessed! Click Ok to continue.")
        continue

    """ If the user's guess is valid, then we convert the list to float and instantiate the Turtle
    Object displaying the text and making it move to a specific location based on the .CSV file."""
    text = CountryText(float(state_x_coordinate[0]), float(state_y_coordinate[0]), answer)
    current_score += 1
    title = f"{current_score} / {MAX_SCORE} States Correct"
    correct_guesses.append(answer)

main_screen.exitonclick()
