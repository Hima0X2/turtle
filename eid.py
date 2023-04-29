import turtle
import random
wn=turtle.Screen()
wn.bgcolor("black")
colors= ['red', 'blue', 'orange', 'yellow', 'magenta', 'purple', 'peru', 'ivory', 'dark orange','LightSalmon','FireBrick','MediumVioletRed','OrangeRed','Indigo','ForestGreen','Teal']
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
bob = turtle.Turtle()
bob.speed(30)
bob.penup()
bob.goto((-200-350,-200))
bob.pendown()
eid = turtle.Turtle()
eid.reset()
eid.speed(10)
eid.pensize(5)
eid.color("white")
def latter_e(height):
    eid.forward(100) #1
    e = eid.position()
    
    eid.left(90)
    eid.forward(30) #2
    
    eid.left(90)
    eid.forward(70) #3 
    
    eid.right(90) #4
    eid.forward(30)
    
    eid.right(90) #5
    eid.forward(65)
    
    eid.left(90) #6
    eid.forward(30)
    
    eid.left(90) #7
    eid.forward(65)
    
    eid.right(90) #8
    eid.forward(30)
    
    eid.right(90) #9
    eid.forward(70)
    
    eid.left(90) #10
    eid.forward(30)
    
    eid.left(90) #11
    eid.forward(100)
    
    eid.left(90) #12
    eid.forward(150)
    eid.setpos(e)
    eid.left(90)
    
eid.penup()
eid.goto(-190+200-140,-100-50+80)
eid.pendown()
latter_e(150)

def gap_for_eid_mubarak(val):
    eid.penup()
    eid.forward(val)
    eid.pendown()
gap_for_eid_mubarak(30)
# I


def latter_i(height):
#    eid.begin_fill()
    eid.forward(100) #1
    i_endPos = eid.position()
    
    eid.left(90)
    eid.forward(30) #2
    
    eid.left(90)
    eid.forward(35) #3 
    
    eid.right(90)
    eid.forward(90) #4 
    
    eid.right(90)
    eid.forward(35) #5 
    
    eid.left(90)
    eid.forward(30) #6
    
    eid.left(90)
    eid.forward(100) #7
    
    eid.left(90)
    eid.forward(30) #8
    
    eid.left(90)
    eid.forward(35) #9
    
    eid.right(90)
    eid.forward(90) #10
    
    eid.right(90)
    eid.forward(35) #12
    
    eid.left(90)
    eid.forward(30) #13
#    eid.end_fill()
    eid.setpos(i_endPos)
    eid.left(90)
   
latter_i(150)
gap_for_eid_mubarak(30)

# D
def latter_d(height):
#    eid.begin_fill()
    
    eid.left(90)
    eid.forward(height)
    eid.right(90)
    
    eid.forward(20)
    
    eid.circle(-height / 2, 180, 30)
    eid.forward(20)
#    eid.end_fill()
    
    
    eid.penup()
    eid.backward(30)
    eid.right(90)
    eid.forward((height - 70) / 2)
    eid.pendown()
    

#    eid.begin_fill()
#    eid.color('white')
    eid.forward(70)
    eid.right(90)
    eid.circle(-70 / 2, 180, 30)
#    eid.end_fill()
latter_d(150)
eid.right(90)
eid.right(90)
# M
eid.penup()
eid.goto(-190+200-350,-100-220+80)
eid.pendown()

def latter_m(height): 
    eid.color('white')
#    eid.begin_fill()
    eid.left(90)
    eid.forward(height) #1
    
    eid.right(90)
    eid.forward(20) #2
    
    eid.right(45)
    eid.forward(70) #3
    
    eid.left(90)
    eid.forward(70) #4
    
    eid.right(45)
    eid.forward(20) #5
    
    eid.right(90)
    eid.forward(height) #6
    m_endPos = eid.position()
    
    eid.right(90)
    eid.forward(40) #7
    
    eid.right(90)
    eid.forward(85) #8
    
    eid.left(135)
    eid.forward(40) #9
    
    eid.right(90)
    eid.forward(40) #10
    
    eid.left(135)
    eid.forward(85) #11
    
    eid.right(90)
    eid.forward(45) #7
    
    eid.penup()
    eid.setpos(m_endPos)
    eid.left(180)
    eid.forward(10)
    eid.pendown()
    
#    eid.end_fill()
    
latter_m(150)

def latter_u(height,width):
#    eid.color('red')
#    eid.begin_fill()
    
    eid.left(90)
    eid.forward(height) #1
    
    eid.right(90)
    eid.forward(width/3) #2

    eid.right(90)
    eid.forward(height - height/4) #3

    eid.left(90)
    eid.forward(width/3) #4

    eid.left(90)
    eid.forward(height - height/4) #5  
    
    eid.right(90)
    eid.forward(width/3) #6   
    
    eid.right(90)
    eid.forward(height) #7  
    u_endPos = eid.position()
    
    
    eid.right(90)
    eid.forward(width) #1 
#    eid.end_fill()
    
    eid.setpos(u_endPos)
    eid.left(180)
    

latter_u(150,140)

gap_for_eid_mubarak(15+5)

# B
def latter_b(height,width):
#    eid.color('red')
#    eid.begin_fill()
    
    b_sPos = eid.position()
    
    eid.left(90)
    eid.forward(height) #1
    
    eid.right(90)
    eid.forward(width/3) #2
    
    eid.circle(-height / 4, 180, 30) #3
    
    eid.right(180)
    eid.circle(-height / 4, 180, 30) #4
    
    eid.forward(width/3) #5
#    eid.end_fill()
    
    eid.penup()
    eid.backward(width/4)
    eid.right(90)
    eid.forward(height/8)
    eid.pendown()
    
#    eid.color('red','white')
#    eid.begin_fill()
    eid.forward((height/8)*2)
    eid.right(90)
    eid.circle((-(height/8)*2) / 2, 180, 30)
#    eid.end_fill()
    
    eid.right(90)
    eid.penup()
    eid.forward((height/8)*4)
    eid.pendown()
    
#    eid.color('red','white')
#    eid.begin_fill()
    eid.forward((height/8)*2)
    eid.right(90)
    eid.circle((-(height/8)*2) / 2, 180, 30)
#    eid.end_fill()
    
    eid.penup()
    eid.setpos(b_sPos)
    eid.left(180)
    
    
latter_b(150,140)

# A
eid.forward(70)
eid.pendown()
gap_for_eid_mubarak(20+5)


def latter_a(height,width):
#    eid.color('red')
#    eid.begin_fill()
    
    eid.left(75)
    eid.forward(height) #1
    
    eid.right(75)
    eid.forward(width/2) #2
    
    eid.right(75)
    eid.forward(height) #3
    a_endPos = eid.position()
    
    
    eid.right(105)
    eid.forward(width/3) #4
    
    eid.right(75)
    eid.forward(height/4) #5
    
    eid.left(75)
    eid.forward(width/4) #6
    
    eid.left(75)
    eid.forward(height/4) #7
    
    eid.right(75)
    eid.forward(width/3) #8
#    eid.end_fill()
    
    eid.penup()
    eid.backward(width/2)
    eid.right(90)
    eid.forward((height/3)*2.2)
    eid.pendown()
    
#    eid.color('red','white')
#    eid.begin_fill()
    eid.right(90)
    for _ in range(3):
        eid.right(60)
        eid.forward(height/3.5)
        eid.right(60)
#    eid.end_fill()
    
    eid.penup()
    eid.setpos(a_endPos)
    
    
latter_a(150,125)

gap_for_eid_mubarak(8+5)
# R
def latter_r(height,width):
    r_endPos = eid.position()
#    eid.color('red')
#    eid.begin_fill()
    
    eid.left(90)
    eid.forward(height) #1
    
    eid.right(90)
    eid.forward(width/2) #2
    
    eid.circle(-height / 4, 180, 30) #3
    
    eid.left(135)
    eid.forward(height/1.4) #4
    
    eid.right(135)
    eid.forward(width/2.5) #5
    
    eid.right(45)
    eid.forward(height/3) #6
    
    eid.left(135)
    eid.forward(height/4.3) #7
    
    eid.right(90)
    eid.forward(width/2.5) #8
#    eid.end_fill()
    
    
    eid.penup()
    eid.backward(width/4)
    eid.right(90)
    eid.forward((height/4)*2.5)
    eid.pendown()
    
#    eid.color('red','white')
#    eid.begin_fill()
    eid.forward((height/8)*2)
    eid.right(90)
    eid.forward(width/6)
    eid.circle((-(height/8)*2) / 2, 180, 30)
    eid.forward(width/6)
#    eid.end_fill()
    
    eid.penup()
    eid.setpos(r_endPos)
    eid.left(180)
    
latter_r(150,140)

eid.forward(115)
eid.pendown()
gap_for_eid_mubarak(35+5)

# A A
latter_a(150,125)

gap_for_eid_mubarak(16)

## k
def latter_k(height,width):
    eid.left(90)
    eid.forward(height) #1
    eid.right(90)
    eid.forward(width/4) #2
    eid.right(90)
    eid.forward((height / 7)*3) #3
    eid.left(135)
    eid.forward((width/4)*2) #4
    eid.right(135)
    eid.forward(width / 4) #5
    eid.right(45)
    eid.forward((width / 4)* 1.5) #6
    eid.left(90)
    eid.forward((width / 4)*2.5) #7
    eid.right(135)
    eid.forward(width / 4)  #8
    eid.right(45)
    eid.forward((width / 4)*1.5) #9
    eid.left(135)
    eid.forward(width/4) #10
    eid.right(90)
    eid.forward(width/4) #11
latter_k(150,140)
star = turtle.Turtle()
star.speed(100)
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
  return (random.randint(-300,700),random.randint(110,360))
def random_length():
  return (random.randint(5,10))
n=60
i = 1
while i <= n:
    i = i+1 
    color=random.choice(colors)
    pos=random_pos()
    length=random_length()
    draw_star(pos, color, length)
fir=turtle.Turtle()
fir.speed(0)
fir.hideturtle()
def draw(t):
    x=random.randint(-300,600)
    y=random.randint(110,360)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(random.choice(colors))
    d=random.randint(20,50)
    for i in range(36):
        t.forward(d)
        t.backward(d)
        t.right(10)

for i in range(10):
    draw(fir)
def star1(turtle,size):
  if size<=10:
   return
  else:
    turtle.begin_fill()
    for x in range(5):
      turtle.pencolor(colors[x%6])
      turtle.width(x/100+1)
      turtle.forward(size)
      star1(turtle,size/3)
      turtle.left(216)
    turtle.end_fill()
  
star1(bob,120)
turtle.done()
