from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move=10
        self.y_move=10
        self.createball()
        self.move_speed=0.1

    def createball(self):
        self.penup()
        self.color("white")
        self.shape("circle")

    def move(self):
        x_cor=self.xcor()+self.x_move
        y_cor=self.ycor()+self.y_move
        self.goto(x_cor,y_cor)

    def bounce_y(self):
        self.y_move*=-1
    
    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.9

    def reset(self):
        self.goto(0,0)
        self.x_move*=-1
        self.move_speed=0.1
