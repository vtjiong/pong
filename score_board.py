import turtle
class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.hideturtle()
        self.l_score =0
        self.r_score =0
        self.goto(-100,200)
        self.write(self.l_score,align='center',font=('Arial', 80, 'bold'))
        self.goto(100,200)
        self.write(self.r_score,align='center',font=('Arial', 80, 'bold'))

    def l_increase(self):
        self.clear()
        self.l_score +=1
        self.goto(-100,200)
        self.write(self.l_score,align='center',font=('Arial', 80, 'bold'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Arial', 80, 'bold'))

    def r_increase(self):
        self.clear()
        self.r_score += 1
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Arial', 80, 'bold'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Arial', 80, 'bold'))