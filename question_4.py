# Program name: question_4.py
# Author: Candidate Number: KGQM5

import turtle

OUTER_CIRCLE_COLOR = "slate grey"
INSIDE_CIRCLE_RADIUS = 20
INSIDE_CIRCLE_COLOR = "orange"

def setup():
    '''Set turtle characteristics.'''
    turtle.speed(10)
    turtle.pu()     # pen up
    turtle.ht()     # hide turtle
    turtle.seth(0)  # set heading to 0 (east)

def draw_inside_circle():
    turtle.seth(-90) #turtle face down to make (0, 0) centre of inner circle
    turtle.forward(INSIDE_CIRCLE_RADIUS)
    turtle.seth(0)
    turtle.color(INSIDE_CIRCLE_COLOR)
    turtle.begin_fill()
    turtle.circle(INSIDE_CIRCLE_RADIUS)
    turtle.end_fill()
    pass

def draw_ring_of_circles(num_circles, outer_circle_radius, pattern_radius):
    for counter in range(num_circles):
        #turning turtle left with respect to the required circle
        turtle.lt(360/num_circles)
        turtle.fd(pattern_radius)
        turtle.color(OUTER_CIRCLE_COLOR)
        #starting filling up the cicle
        turtle.begin_fill()
        turtle.circle(outer_circle_radius)
        turtle.end_fill()
        #moving back to the centre after finished drawing the outter circle
        turtle.left(180)
        turtle.forward(pattern_radius)
        turtle.left(180)
    pass


def main():
    setup() # set up the turtle
    turtle.goto((0,0))
    turtle.seth(0) # face east
    draw_inside_circle()
    turtle.goto((0,0))
    turtle.seth(90) # face north
    draw_ring_of_circles(6, 40, 75)
    turtle.exitonclick()

if __name__ == "__main__":
    main()