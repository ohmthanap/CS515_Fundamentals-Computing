# Thanapoom Phatthanaphan
# This is a program to draw a house and human stick figure by creating classes to
# draw each part (Circle, Line, Rectangle) then import them from shapes.py file

from shapes import Circle, Line, Rectangle
import turtle


def main():
    """Draws a house and stick figure."""
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    turtle.colormode(255)
    turtle.setup(startx=0, starty=0)

    # Draw the stick figure
    face = Circle(100, 0, 10, turtle, black)
    body = Line(100, 0, 100, -80, turtle, black)
    arms = Line(80, -40, 120, -40, turtle, black)
    leftLeg = Line(100, -80, 80, -100, turtle, black)
    rightLeg = Line(100, -80, 120, -100, turtle, black)
    face.draw()
    body.draw()
    arms.draw()
    leftLeg.draw()
    rightLeg.draw()

    # Draw the house
    front = Rectangle(-180, -100, 0, 100, turtle, black)
    door = Rectangle(-120, -100, -60, 30, turtle, blue)
    roof1 = Line(-180, 100, -160, 120, turtle, red)
    roof2 = Line(-160, 120, -20, 120, turtle, red)
    roof3 = Line(-20, 120, 0, 100, turtle, red)
    front.draw()
    door.draw()
    roof1.draw()
    roof2.draw()
    roof3.draw()

    turtle.done()


main()
