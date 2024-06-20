import turtle
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move=10
        self.y_move=10
        self.counter = 1
    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def bounce(self):
        self.y_move*=-1
    def bounce_paddle(self):
        self.x_move*=-1

    def reset(self):
        self.home()
        self.bounce_paddle()
        self.bounce()
