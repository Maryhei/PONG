from turtle import Turtle


class Newpaddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setposition(x=xcor, y=ycor)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self_new_ycor = self.ycor() + 20
        self.goto(self.xcor(), self_new_ycor)

    def down(self):
        self_new_ycor = self.ycor() - 20
        self.goto(self.xcor(), self_new_ycor)
