import turtle
import os
import math
import random


#window
window = turtle.Screen()
#window background color
window.bgcolor("black")
#window title
window.title("Space Invaders || Breakout on Steroids")


#window border
border_pen = turtle.Turtle()
#draw speed (zet de speed op 1 om alles duidelijker te zien uitgevoerd worden)
border_pen.speed(0)
#pen kleur
border_pen.color("white")
# pen up betekend dat pen niet schrijft op dit moment (denk aan een hand die een pen vast heeft als je hand UP is dus opgetild dan schrijf je niet meer)
border_pen.penup()
#pen gaat naar positie -300,-300
border_pen.setposition(-300,-300)
#pen gaat down dus denk aan als je hand een pen vast heeft en down gaat op het blad papier en je dus contact maakt met het papier en kan tekenen of schrijven
border_pen.pendown()
#pensize
border_pen.pensize(3)
# vierkant wordt geteken loop wordt 4 keer uitgevoerd 600 pixels forward een lijn dan 90 graden draaien en herhalen
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
#cursor van pen wordt weg gestopt anders oogt het niet mooi
border_pen.hideturtle()


#Speler
player = turtle.Turtle()
#GODS FAVORIETE KLEUR
player.color("cyan")
#Speler is een driehoek
player.shape("triangle")
player.penup()
player.speed(0)
#Speler positie
player.setposition(0,-250)
#draai speler 90 graden
player.setheading(90)
playerSpeed = 15



aantal_enemies = 5
#enemyList
enemies = []

for i in range(aantal_enemies):
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    #Enemy
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)
   
enemySpeed = 5

    


#Bullet
bullet = turtle.Turtle()
bullet.color("green")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
#verstop bullet
bullet.hideturtle()
bulletSpeed = 25




#Move left
def move_left():
    x = player.xcor()
    x -= playerSpeed
    if x < -290:
        x = -290
    player.setx(x)

    
#Move right 
def move_right():
    x = player.xcor()
    x += playerSpeed
    if x > 290:
        x = 290
    player.setx(x)

bulletstate = "ready"

#Bullet fire
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #bullet op player zijn locatie
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x,y) 
        bullet.showturtle()
        

#Bullet & Enemy Collision Detection
def isCollided(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    
    
#Keyboard event
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")


#GAME LOOP
while True:
    

    for enemy in enemies:
        #Move Enemy
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)
    
        #Collision Enemy, Move down
        if enemy.xcor() > 290:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1
                
        if enemy.xcor() < -290:
             for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
             enemySpeed *= -1
            
        #BULLET EN ENEMY COLLISION 
        if(isCollided(bullet,enemy)):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            
        #PLAYER EN ENEMY COLLISION DUS GAME OVER COLLISION
        if(isCollided(player,enemy)):
            enemy.hideturtle()
            player.hideturtle()
            bullet.hideturtle()
            print("Game Over!")
            break
        
    #Move bullet upwards
    y = bullet.ycor()
    y += bulletSpeed
    if y > 300:
        bullet.hideturtle()
        bulletstate = "ready"
    bullet.sety(y)
    

