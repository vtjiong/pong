import turtle
import paddle
import ball
import time
import score_board
delay_time=0.07
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
# Turn off animation
r_paddle=paddle.Paddle(350,0)
l_paddle=paddle.Paddle(-350,0)
ball=ball.Ball()
score_board=score_board.ScoreBoard()
screen.listen()
screen.onkey(fun=r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")
screen.onkey(fun=l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_down,key="s")

game_is_on=True
while game_is_on:
    time.sleep(delay_time)
    #keep on manually update the screen
    screen.update()
    ball.move()
    #Detect collision with wall
    if (ball.ycor() > 280 or ball.ycor()<-280) :
        ball.bounce()

    #Detect collision with r_paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce_paddle()
        if delay_time > 0:
            delay_time-=0.005


    if ball.xcor()>r_paddle.xcor():
        ball.reset()
        delay_time=0.07
        score_board.l_increase()

    if ball.xcor() <l_paddle.xcor():
        ball.reset()
        delay_time=0.07
        score_board.r_increase()

screen.exitonclick()