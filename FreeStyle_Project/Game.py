import os
import turtle
import random
import math


#WINDOW
window = turtle.Screen()
window.bgcolor("black")
window.title("Freestyle Project")



#WINDOW BORDER
windowBorder = turtle.Turtle()
windowBorder.color("grey")
windowBorder.penup()
windowBorder.hideturtle()
windowBorder.speed(10)
windowBorder.setposition(-300,-300)
windowBorder.pendown()

for i in range(4):
    windowBorder.fd(600)
    windowBorder.lt(90)


#START CREATION
start = turtle.Turtle()
start.shape("square")
start.color("yellow")
start.shapesize(2,2)
start.speed(0)
start.penup()
start.setposition(-275,275)


#PLAYER CREATION
player = turtle.Turtle()
player.shape("triangle")
player.color("red")
player.speed(0)
player.penup()
player.setposition(-275,275)
playerSpeed = 15




#DOOR CREATION
door = turtle.Turtle()
door.shape("square")
door.color("yellow")
door.shapesize(2,2)
door.speed(0)
door.penup()
door.setposition(275,-275)




aantal_blocks = 50
blocks = []
xWaarden = 0.0
yWaarden = 0.0
gemY = 0.0
gemX = 0.0

for i in range(aantal_blocks):
    blocks.append(turtle.Turtle())
    
for block in blocks:
    #BLOCKS
    block.speed(0)
    block.color("pink")
    block.shape("square")
    block.penup()
    x = random.randrange(-230, 275,50)
    y = random.randrange(-230, 275,50)
    block.setposition(x,y)

#GEMMIDELDE LOC
xWaarden += block.xcor()
yWaarden += block.ycor()
gemX = xWaarden/50
gemY = yWaarden/50   


#KEY CREATION
key = turtle.Turtle()
key.shape("circle")
key.color("purple","orange")
key.speed(0)
key.penup()
key.setposition(gemX,gemY)



#MOVEMENT
def move_left():
    x = player.xcor()
    x -= playerSpeed
    player.setheading(180)
    if x < -285:
        x = -285
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerSpeed
    player.setheading(0)
    if x > 285:
        x = 285
    player.setx(x)

def move_up():
    y = player.ycor()
    y += playerSpeed
    player.setheading(90)
    if y > 285:
        y = 285
    player.sety(y)
    
def move_down():
    y = player.ycor()
    y -= playerSpeed
    player.setheading(-90)
    if y < -285:
        y = -285
    player.sety(y)
    
def isCollided(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False


#EVENT LISTENER
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")


keyIsCollected = False


#GAME LOOP
while True:
    

    for block in blocks:
        #Block pos
        x = block.xcor()       
        block.setx(x)
        #PLAYER EN BLOCK COLLISION DUS GAME OVER COLLISION
        if(isCollided(player,block)):
            player.setposition(-275,275)
            print("Game Over!")
            break
        
    #PLAYER EN KEY COLLISION    
    if(isCollided(player,key)):
        keyIsCollected = True
        key.hideturtle()
        turtle.clear()
        turtle.hideturtle()
        turtle.penup()
        turtle.setposition(-300,320)
        turtle.pendown()
        turtle.color("orange")
        turtle.write("KEY COLLECTED!", font=("Times New Roman", 14, "bold"))
        print("Key Collected!")
        
    #PLAYER EN DOOR COLLISION MET EN ZONDER KEY    
    if(isCollided(player,door)):
        if(keyIsCollected):
            turtle.clear()
            turtle.hideturtle()
            turtle.penup()
            turtle.setposition(-300,320)
            turtle.pendown()
            turtle.color("white")
            turtle.write("LEVEL PASSED!", font=("Times New Roman", 14, "bold"))
            print("LEVEL PASSED!")
            playerSpeed = 0
            break
        else:
            turtle.clear()
            turtle.hideturtle()
            turtle.penup()
            turtle.setposition(-300,320)
            turtle.pendown()
            turtle.color("red")
            turtle.write("YOU NEED TO FIND THE KEY!", font=("Times New Roman", 14, "bold"))
            print("YOU NEED TO FIND THE KEY")
