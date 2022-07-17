from turtle import Turtle, Screen

import ball
from mypaddle import Newpaddle
from ball import Ball
import score_line
from score_line import Score_line

screen = Screen()
screen.listen()
screen.tracer(0)


mypaddle = Newpaddle(xcor=350, ycor=0)
leftpaddle = Newpaddle(xcor=-350, ycor=0)
balls = Ball()
score = Score_line()
# score_line.drawline_andscore()


screen.onkey(fun=mypaddle.up, key="Up")
screen.onkey(fun=mypaddle.down, key="Down")
screen.onkey(fun=leftpaddle.up, key="w")
screen.onkey(fun=leftpaddle.down, key="s")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")


game_is_on = True
while game_is_on:

    screen.update()
    balls.move()


    if balls.ycor() > 280 or balls.ycor() < -280:
        balls.bounce()
    if balls.xcor() > 335 or balls.xcor() < -335:
        if balls.distance(mypaddle) < 50 or balls.distance(leftpaddle) < 50:
            balls.collision()
            ball.SPEED += 1
            if ball.SPEED > 10:
                ball.SPEED = 0
    if balls.xcor() > 380:
        score_line.LEFT_SCORE += 1
        score.clear()
        score.new_score()
        balls.refresh()
    if balls.xcor() < -380:
        score_line.RIGHT_SCORE += 1
        score.clear()
        score.new_score()
        score.new_score()
        balls.refresh()


screen.exitonclick()
