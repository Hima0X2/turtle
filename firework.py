import turtle
import random
colors= ['red', 'blue', 'orange', 'yellow', 'magenta', 'purple', 'peru', 'ivory', 'dark orange','LightSalmon','FireBrick','MediumVioletRed','OrangeRed','Indigo','ForestGreen','Teal']
wn=turtle.Screen()
wn.bgcolor("black")
fir=turtle.Turtle()
fir.speed(0)
fir.hideturtle()
def draw(t):
	x=random.randint(-200,200)
	y=random.randint(-200,200)
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color(random.choice(colors))
	d=random.randint(20,100)
	for i in range(36):
		t.forward(d)
		t.backward(d)
		t.right(10)

for i in range(2):
	draw(fir)