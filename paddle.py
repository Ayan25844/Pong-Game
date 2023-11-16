MOVE_DISTANCE=20
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.x_cor=x_cor
        self.createpaddle()

    def createpaddle(self):
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(self.x_cor,0)
        self.shapesize(stretch_wid=5,stretch_len=1)
    
    def up(self):
        self.goto(self.x_cor,self.ycor()+MOVE_DISTANCE)

    def down(self):
        self.goto(self.x_cor,self.ycor()-MOVE_DISTANCE)