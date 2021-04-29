# Program name: question_3.py
# Author: Candidate Number: KGQM5

import turtle

START_RADIUS = 10
RADIUS_INCREMENT = 10

def concentric_circles(total_circles):
    for counter in range(total_circles):
        #drawing circle with different radius every time
        turtle.circle(START_RADIUS + RADIUS_INCREMENT * counter)
        #moving turtle 
        move_to(START_RADIUS + RADIUS_INCREMENT )
    pass


def move_to(position):
    turtle.penup()
    turtle.right(90)
    turtle.fd(position/2)
    turtle.left(90)
    turtle.pendown()
    pass


def main():
    turtle.speed(10)
    #calling the function
    concentric_circles(10)
    turtle.exitonclick()


if __name__ == "__main__":
    main()