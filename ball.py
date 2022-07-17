from turtle import Turtle

SPEED = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.speed(SPEED)


    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.setposition(x=new_xcor, y=new_ycor)


    def bounce(self):
        self.y_move *= -1


    def collision(self):
        self.x_move *= -1


    def refresh(self):
        self.goto(0, 0)




