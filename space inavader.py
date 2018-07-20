import turtle
import os
import random
import math
screen=turtle.Screen()
screen.bgcolor('black')
screen.title('Space war')


square=turtle.Turtle()
square.color('white')
square.penup()
square.goto(-300,-300)
square.pendown()
square.speed(0)
square.pensize(3)
for i in range(4):
    square.fd(600)
    square.lt(90)
square.hideturtle()



me=turtle.Turtle()
me.color('yellow')
me.penup()
me.shape('triangle')
me.setposition(0,-250)

me.speed(0)
me.pensize(4)
me.setheading(90)
speed=15

bullet=turtle.Turtle()
bullet.color('blue')
bullet.penup()
bullet.shape('triangle')
bullet.speed(7)
bullet.pensize(1)
bullet.setheading(90)
bullet.hideturtle()
s="ready"
score=turtle.Turtle()
score.color('white')
score.penup()
score.hideturtle()
score.setposition(-300,300)
s1=0
best="score:%s"%s1
score.write(best)

enemy=turtle.Turtle()
enemy.color('red')
enemy.penup()
enemy.shape('circle')
enemy.speed(4)
r1=random.randrange(-260,200)
r2=random.randrange(250,300)
enemy.setposition(r1,r2)
enemyspeed=3
enemy.dy=6





def right1():
    x = me.xcor()
    x += speed
    me.setx(x+10)


def left1():
    x = me.xcor()
    x -= speed
    me.setx(x-10)

def shoot():
  global s
  if s=="ready":
   s="fire"
   x=me.xcor()
   y=me.ycor()
   bullet.setposition(x,y+1)
   bullet.showturtle()

def iscollision(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.xcor()-t2.xcor(),2))
    if d>15:
        return False
    else:
        return True


def over(t1,t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.xcor() - t2.xcor(), 2))
    if d > 15:
        return False
    else:
        return True


turtle.listen()
turtle.onkey(right1, "Right")
turtle.onkey(left1, "Left")
turtle.onkey(shoot,"Up")
shoot()

while True:

    x=enemy.xcor()
    y=enemy.ycor()
    enemy.setx(x+enemyspeed)
    if enemy.xcor()>260:
        enemy.sety(y-enemy.dy)
        enemyspeed*=-1

    if enemy.xcor()<-260:
        enemy.sety(y - enemy.dy)
        enemyspeed*=-1

    b = bullet.ycor()

    if b > 300:
        bullet.hideturtle()
        s = "ready"

    else:
        bullet.sety(b + speed)

    if iscollision(bullet,enemy):
        bullet.hideturtle()

        enemy.hideturtle()
        r1=random.randrange(-260,200)
        r2=random.randrange(200,300)
        enemy.setposition(r1,r2)
        enemy.showturtle()
        s1+=10
        score.clear()
        best = "score:%s" % s1
        score.write(best)
    if over(me,enemy):
        score.clear()
        score.write("Game over")
        print("Game over")
