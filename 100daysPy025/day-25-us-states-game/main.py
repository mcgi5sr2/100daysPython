import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def create_turtle(state_name):
    """creates a turtle with text at the x, y location taken from the csv"""
    new_state = turtle.Turtle()
    new_state.penup()
    state = data[data.state == state_name]
    # print(f"{state} is at {state.x.item()}, {state.y.item()}")
    new_state.goto(state.x.item(), state.y.item())
    new_state.write(state_name, False, "center", ("Courier", 12, "normal"))


data = pandas.read_csv("50_states.csv")
# print(data)

count = 0
answers = []
while len(answers) < 50:
    answer = screen.textinput(title=f"States game {count}/50", prompt="Whats another state's name?").title()

    if answer == "Exit":
        data[~data['state'].isin(answers)].to_csv("states_to_learn.csv")
        break
    if data['state'].str.contains(answer).any():
        create_turtle(answer)
        answers.append(answer)
        count += 1