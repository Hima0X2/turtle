import turtle
import random
wn=turtle.Screen()
#wn.screensize(10000,10000000)
wn.bgcolor("black")
colors= ['red', 'blue', 'orange', 'yellow', 'magenta', 'purple', 'peru', 'ivory', 'dark orange']
moon = turtle.Turtle()
moon.speed(10)
star = turtle.Turtle()
star.speed(10)
moon.reset()
def eid_moon():    
    moon.up()
    moon.color('white')
    moon.goto(-80-280,100)
    moon.begin_fill()
    moon.circle(100)
    moon.end_fill()
    moon.up()
    moon.goto(10-80-280,10+100)
    moon.color('black')
    moon.begin_fill()
    moon.circle(100)
    moon.end_fill()
    moon.color('white')
eid_moon()
star.penup()
star.color('white')
star.forward(100)
star.goto(-10-80-300,100+100)
star.pendown()
star.begin_fill()
for x in range(5):
  star.forward(50)
  star.left(216)
star.end_fill()
star = turtle.Turtle()
star.speed(0)
star.hideturtle()
def draw_star(pos, color, length):
    x, y = pos
    star.color(color)
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.begin_fill()
    for i in range(5):
        star.forward(length)
        star.right(144)
        star.forward(length)
    star.end_fill()
def random_pos():
  return (random.randint(-190,190),random.randint(-190,190))
def random_length():
  return (random.randint(5,25))
n=10
i = 1
while i <= n:
    i = i+1 
    color=random.choice(colors)
    pos=random_pos()
    length=random_length()
    draw_star(pos, color, length)
