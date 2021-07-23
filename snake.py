from turtle import Turtle


class Snake:
    positions = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    RIGHT = 0
    UP = 90
    LEFT = 180
    DOWN = 270

    def __init__(self, length=3):
        self.length = length
        self.segments = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for i in range(self.length):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(Snake.positions[i])
            self.segments.append(tim)
        self.head = self.segments[0]

    def move(self):
        for i in range(self.length - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(x=new_x, y=new_y)
        self.head.forward(Snake.MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != Snake.DOWN:
            self.head.setheading(Snake.UP)

    def move_down(self):
        if self.head.heading() != Snake.UP:
            self.head.setheading(Snake.DOWN)

    def move_left(self):
        if self.head.heading() != Snake.RIGHT:
            self.head.setheading(Snake.LEFT)

    def move_right(self):
        if self.head.heading() != Snake.LEFT:
            self.head.setheading(Snake.RIGHT)

    def increaseLength(self):
        tim = Turtle(shape="square")
        #tim.hideturtle()
        tim.color("white")
        tim.penup()
        x_cor = self.segments[-1].xcor()
        y_cor = self.segments[-1].ycor()
        tim.goto(x_cor,y_cor)
        #tim.showturtle()
        self.length += 1
        self.segments.append(tim)
