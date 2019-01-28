import turtle
import math
import random
import winsound

#register Shapes
turtle.register_shape("bullet.gif")
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
# Create Screen

win=turtle.Screen()
win.bgcolor("green")
win.title("Space Invader by Shrijan")
#win.bgpic("space1.gif")
win.tracer(0)


#create a border
border_game=turtle.Turtle()
border_game.speed(0)
border_game.color("white")
border_game.penup()
border_game.setposition(-300,-300)
border_game.pendown()
border_game.pensize(3)
for side in range(4):
    border_game.pendown()
    border_game.fd(600)
    border_game.lt(90)
border_game.hideturtle()

#Create a Player

player_pen= turtle.Turtle()
player_pen.penup()
player_pen.speed(0)
player_pen.shape("triangle")
player_pen.color("black")
player_pen.setposition(0,-250)
player_pen.setheading(90)

# Score
score=0
score_pen=turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.speed(0)
score_pen.color("white")
score_pen.setposition(-280,260)
scorestring="Score:%s"%score
score_pen.write(scorestring,False,align="left",font=("Arial",15,"normal"))

#create enemies
enemies=[]
for i in range (5):
    enemies.append(turtle.Turtle())
for enemy_pen in enemies:
    enemy_pen.shape("circle")
    enemy_pen.penup()
    enemy_pen.speed(0)
    enemy_pen.color("red")
    x=random.randint(-250,250)
    y=random.randint(100,250)
    enemy_pen.setposition(x, y)

bulletstate ="ready"
# move left and right
playerspeed= 50
def moveleft():
    x=player_pen.xcor()
    x-=playerspeed
    if x < -280:
        x=-280
    player_pen.setx(x)
def moveright():
    x=player_pen.xcor()
    x+=playerspeed
    if x>280:
        x=280
    player_pen.setx(x)

#Fire Bullet
bulletspeed = 20
def firebullet():
    global bulletstate
    if bulletstate=="ready":
       bulletstate = "fire"
       bullet_pen.setposition((player_pen.xcor()), ((player_pen.ycor()) +5))
       bullet_pen.showturtle()


#Collision
def collision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
       return True
    else:
       return False

#Collision for player
def pcollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance <30:
       return True
    else:
      return False

#create keyboard binding
turtle.listen()
turtle.onkey(moveleft, "Left")
turtle.onkey(moveright, "Right")
turtle.onkey(firebullet,"space")


#Create a bullet

bullet_pen=turtle.Turtle()
bullet_pen.speed(0)
bullet_pen.shape("triangle")
bullet_pen.shapesize(0.5,0.5)
bullet_pen.color("yellow")
bullet_pen.penup()
bullet_pen.setposition((player_pen.xcor()),((player_pen.ycor())+20))
bullet_pen.setheading(90)
bullet_pen.hideturtle()

#create keyboard binding
turtle.listen()
turtle.onkey(moveleft, "Left")
turtle.onkey(moveright, "Right")
turtle.onkey(firebullet,"space")


#Main Game
score=0
# Move Enemy left to right
enemyspeed=0.3
while True:
    win.update()
    for enemy_pen in enemies:
        x = enemy_pen.xcor()
        x += enemyspeed
        enemy_pen.setx(x)
        if enemy_pen.xcor()>280:
            for e in enemies:
                y=e.ycor()
                y -=50
                e.sety(y)
            enemyspeed *= -1

        if enemy_pen.xcor()<-280:
           for e in enemies:
             y=e.ycor()
             y -=50
             e.sety(y)
           enemyspeed *= -1
   
  ##  while collision
        if collision(bullet_pen,enemy_pen):
           bullet_pen.hideturtle()
           bulletstate="ready"
           x = random.randint(-250, 250)
           y = random.randint(100, 250)
           enemy_pen.setposition(x, y)
           score += 10
           scorestring = "Score:%s" % score
           score_pen.clear()
           score_pen.write(scorestring, False, align="left", font=("Arial", 15, "normal"))

    # while collision with player
        if pcollision(player_pen, enemy_pen):
           player_pen.hideturtle()
           enemy_pen.hideturtle()
           print("GAME OVER!!")
           print("Final Score:%s"%score)
           #exit()
           win2_pen = turtle.Screen()
           win2_pen.bgcolor("white")
           win2_pen.bgpic("gameover.gif")
           exit()
        if enemy_pen.ycor() < - 245:
            print("game over")
            print("Final Score:%s" % score)
            win2_pen = turtle.Screen()
            win2_pen.bgcolor("green")
            win2_pen.bgpic("gameover.gif")
            exit()
   # while firing
    if bulletstate == "fire":
       y = bullet_pen.ycor()
       y += bulletspeed
       bullet_pen.sety(y)

    if bullet_pen.ycor() > 280:
       bullet_pen.hideturtle()
       bulletstate = "ready"



