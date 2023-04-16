class Circle:
    def __init__(self, x_axis, y_axis, radius, turtle, color):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.radius = radius
        self.turtle = turtle
        self.color = color

    def draw(self):
        self.turtle.hideturtle()
        self.turtle.up()
        self.turtle.goto(self.x_axis, self.y_axis)
        self.turtle.down()
        self.turtle.pencolor(self.color)
        self.turtle.circle(self.radius)


class Line:
    def __init__(self, x1_axis, y1_axis, x2_axis, y2_axis, turtle, color):
        self.x1_axis = x1_axis
        self.y1_axis = y1_axis
        self.x2_axis = x2_axis
        self.y2_axis = y2_axis
        self.turtle = turtle
        self.color = color

    def draw(self):
        self.turtle.hideturtle()
        self.turtle.up()
        self.turtle.goto(self.x1_axis, self.y1_axis)
        self.turtle.down()
        self.turtle.pencolor(self.color)
        self.turtle.goto(self.x2_axis, self.y2_axis)


class Rectangle:
    def __init__(self, x1_axis, y1_axis, x2_axis, y2_axis, turtle, color):
        self.x1_axis = x1_axis
        self.y1_axis = y1_axis
        self.x2_axis = x2_axis
        self.y2_axis = y2_axis
        self.turtle = turtle
        self.color = color

    def draw(self):
        self.turtle.hideturtle()
        self.turtle.up()
        self.turtle.goto(self.x1_axis, self.y1_axis)
        self.turtle.down()
        self.turtle.pencolor(self.color)
        self.turtle.goto(self.x2_axis, self.y1_axis)
        self.turtle.goto(self.x2_axis, self.y2_axis)
        self.turtle.goto(self.x1_axis, self.y2_axis)
        self.turtle.goto(self.x1_axis, self.y1_axis)
