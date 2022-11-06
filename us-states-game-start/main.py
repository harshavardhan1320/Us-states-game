import pandas
import turtle
FONT = ("courier", 10, "bold")

t = turtle.Turtle()
s = turtle.Screen()

s.title("U.S. States")
image = "blank_states_img.gif"
s.addshape(image)
t.shape(image)

# to find the coordinates on the map

# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()
states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = s.textinput(title=f"{len(guessed_states)}/50 States correct",
                               prompt="What's the other state names").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t1 = turtle.Turtle()
        t1.hideturtle()
        t1.penup()
        state_name = states_data[states_data.state == answer_state]
        t1.goto(int(state_name.x), int(state_name.y))
        t1.write(answer_state)
