import turtle
import os
import time

#WINDOW INIT
window = turtle.Screen()
window.title("PONG")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#SCORE
score_a = 0
score_b = 0

#GAME OVER RESET
reset = False

#PADDLE 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)

#PADDLE 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)

#BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(-0,0)
ball.dx = 0.2
ball.dy = -0.2

#GAME OVER TURTLE
game_over = turtle.Turtle()

#SCORETEXT
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("PLAYER A : 0       PLAYER B : 0", align="center", font=("Courier", 24, "normal"))

#MOVEMENT
def paddle1_up():
    y = paddle1.ycor()
    y+=20
    paddle1.sety(y)

def paddle1_down():
    y =paddle1.ycor()
    y-=20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y+=20
    paddle2.sety(y)

def paddle2_down():
    y =paddle2.ycor()
    y-=20
    paddle2.sety(y)


#KEYBOARD
window.listen()
window.onkeypress(paddle1_up, "z")
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")


#GAME LOOP
while True:
    window.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #collision
    if(ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -0.6

    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -0.6

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -0.6
        score_a += 1
        score.clear()
        score.write("PLAYER A : {}       PLAYER B : {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -0.6
        score_b += 1
        score.clear()
        score.write("PLAYER A : {}       PLAYER B : {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


    #PADDLE & BALL COLLISION 
    if ball.xcor() > 340 and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1    
    
    if ball.xcor() < -340 and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

    # #GAME OVER
    # if (score_a or score_b) == 3:

    #     paddle1.hideturtle()
    #     paddle2.hideturtle()
    #     ball.hideturtle()
    #     score.hideturtle()
    #     game_over.speed(0)
    #     game_over.color("red")
    #     game_over.penup()
    #     game_over.goto(0,0)
    #     game_over.hideturtle()
    #     game_over.pendown()
    #     game_over.write("GAME OVER : RESTART IN 3 SECONDS", align="center", font=("Courier", 24, "normal"))
    #     time.sleep(3)
    #     game_over.clear()
    #     score_a = 0
    #     score_b = 0
       
        

