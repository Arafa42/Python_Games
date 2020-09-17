import turtle
import os

#WINDOW INIT
window = turtle.Screen()
window.title("PONG")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

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



