import turtle

class Paddle(turtle.Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.x_cor=x_cor
        self.y_cor=y_cor
        self.x_coremove=20
        self.y_coremove=20
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(self.x_cor,self.y_cor)
    def go_up(self):
        self.y_cor+=self.y_coremove
        self.goto(self.x_cor, self.y_cor)
    def go_down(self):
        self.y_cor-=self.y_coremove
        self.goto(self.x_cor, self.y_cor)