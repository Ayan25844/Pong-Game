import time
from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import Score

end=False
screen=Screen()
screen.tracer(0)
screen.title("Pong")
screen.setup(800,600)
screen.bgcolor("black")

ball=Ball()
score=Score()
r_paddle=Paddle(350)
l_paddle=Paddle(-350)

screen.listen()
screen.onkey(l_paddle.up,"w")
screen.onkey(r_paddle.up,"Up")
screen.onkey(l_paddle.down,"s")
screen.onkey(r_paddle.down,"Down")

while(not end):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset()
        score.l_point()
    if ball.xcor()<-380:
        ball.reset()
        score.r_point()
    if score.l_score==10 or score.r_score==10:
        end=True
        score.over()

screen.exitonclick()