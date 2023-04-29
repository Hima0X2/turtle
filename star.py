import turtle
wn=turtle.Screen()
wn.bgcolor("black")
colors= ['Red','purple','blue','yellow','Dark orange']
bob=turtle.Turtle()
bob.speed(20)
bob.color("white")#(outline,fill color)
bob.penup()
bob.pendown()
def star(turtle,size):
  if size<=10:
   return
  else:
    turtle.begin_fill()
    for x in range(5):
      turtle.pencolor(colors[x%6])
      turtle.width(x/100+1)
      turtle.forward(size)
      star(turtle,size/3)
      turtle.left(216)
    turtle.end_fill()
  
star(bob,120)


turtle.done()