import turtle as t
import random

SCREEN_WIDTH=1000
SCREEN_HEIGHT=1000
STAR_COLOR="white"

t.Screen().tracer(0,0)
t.Screen().screensize(SCREEN_WIDTH,SCREEN_HEIGHT)
t.Screen().setworldcoordinates(-SCREEN_WIDTH,-SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_HEIGHT)
t.Screen().bgcolor("black")



def random_star():
  t.penup()
  t.color(STAR_COLOR, STAR_COLOR)

  x=random.randint(-SCREEN_WIDTH,SCREEN_WIDTH)
  y=random.randint(-SCREEN_HEIGHT,SCREEN_HEIGHT)

  dot_size=random.random()*3

  t.goto(x,y)
  t.dot(dot_size)


for _ in range(1000):
    random_star()

t.hideturtle()
t.Screen().update()