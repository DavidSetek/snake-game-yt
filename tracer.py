# Testovací soubor
from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("green")
screen.title("Vítejte v Hadí hře")
screen.setup(width=600, height=600)
screen.tracer(False)

square1 = Turtle("square")
square1.penup()
square1.goto(0, 0)
square2 = Turtle("square")
square2.penup()
square2.goto(-20, 0)

for _ in range(80):
    square1.forward(10)
    square2.forward(10)
    time.sleep(0.1)
    screen.update()

screen.exitonclick()