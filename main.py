from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [-70, -40, -10, 20, 50, 80]
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter a color")
racing_turtles = []
is_race_on = False

for turtles in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtles])
    new_turtle.goto(x=-230, y= y_axis[turtles])
    racing_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for race_turtle in racing_turtles:
        if race_turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = race_turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! {winning_turtle} turtle is the winner!")

        race_turtle.forward(randint(0,10))


screen.exitonclick()