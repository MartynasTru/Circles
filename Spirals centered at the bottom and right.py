# Program name: question_2.py
# Author: Candidate Number: KGQM5

import turtle

START_RADIUS = 10
RADIUS_INCREMENT = 5


def tangential_circles(total_circles):
    for counter in range(total_circles):
        #drawing a bigger circle every time from the same starting point
        turtle.circle(START_RADIUS + RADIUS_INCREMENT * counter)
    pass


def move_to(position):
    turtle.penup()
    turtle.setpos(position)
    turtle.pendown()
    pass


def main():
    turtle.speed(10)
    move_to((-50, 0))
    tangential_circles(10)
    move_to((100, 0))
    turtle.rt(90)
    tangential_circles(10)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
