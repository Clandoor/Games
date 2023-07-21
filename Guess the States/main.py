import turtle
import pandas
from country_text import CountryText


# Setting up the proper image path.
IMAGE_PATH = "india_map.gif"
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
guessed_states = []

# Storing the states inside the list.
us_states = data_frame["state"].to_list()

while len(guessed_states) < 50:

    # The guessed state will be stored here.
    answer = main_screen.textinput(title=title, prompt="What's another state's name?").title()

    # If the user's answer was already guessed, then this will let them know.
    if answer in guessed_states:
        main_screen.textinput(title=title, prompt=f"{answer} already Guessed! Click Ok to continue.")
        continue

    if answer == "Exit":
        missing_states = [state for state in us_states if state not in guessed_states]
        missing_state_frame = pandas.DataFrame(missing_states)
        missing_state_frame.to_csv('states_to_remember.csv')
        break

    if answer in us_states:
        guessed_states.append(answer)
        state_data = data_frame[data_frame["state"] == answer]

        # Can also use 'states_name["state"].item()' instead of 'answer'
        text = CountryText(int(state_data["x"]), int(state_data["y"]), answer)
        current_score += 1
        title = f"{current_score} / {MAX_SCORE} States Correct"

main_screen.exitonclick()
