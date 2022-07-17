from turtle import Turtle
LEFT_SCORE = 0
RIGHT_SCORE = 0


class Score_line(Turtle):
    def __init__(self):
        super().__init__()
        self.drawline_andscore()
        self.leftscore()
        self.rightscore()




    def drawline_andscore(self):
        self.penup()
        self.shape("square")
        self.pencolor("white")
        self.pensize(5)
        self.setheading(270)
        self.hideturtle()
        self.speed(1)
        self.setposition(x=0, y=300)
        while self.ycor() > -400:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)
            self.pendown()


    def leftscore(self):
        self.penup()
        self.setposition(x=-150, y=200)
        self.pendown()
        self.write(f"{LEFT_SCORE}", align="left", font=('Arial', 80, 'normal'))


    def rightscore(self):
        self.penup()
        self.setposition(x=150, y=200)
        self.pendown()
        self.write(f"{RIGHT_SCORE}", align="RIGHT", font=('Arial', 80, 'normal'))


    def new_score(self):
        self.leftscore()
        self.rightscore()
        self.drawline_andscore()




