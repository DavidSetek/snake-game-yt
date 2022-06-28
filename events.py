from turtle import Turtle, Screen

screen = Screen()
tommy = Turtle("turtle")

def move_forward():
    tommy.forward(20)

# Stisknutí klávesy
screen.listen()
screen.onkeypress(move_forward, "w")

screen.exitonclick()