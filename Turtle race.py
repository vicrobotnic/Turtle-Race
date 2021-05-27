import time #for the delay before start another race
import turtle
from turtle import *
from random import randint

turtle.title("Python Turtle Graphics - Turtle Race")

while(True):
    penup()
    goto(-140,140)

    #first Turtle
    a = Turtle()
    a.shape('turtle')
    a.color('green')
    a.penup()
    a.goto(-140,100)

    #second Turtle
    b = Turtle()
    b.shape('turtle')
    b.color('red')
    b.penup()
    b.goto(-140,60)

    #third Turtle
    c = Turtle()
    c.shape('turtle')
    c.color('brown')
    c.penup()
    c.goto(-140,20)

    #fourth Turtle
    d = Turtle()
    d.shape('turtle')
    d.color('orange')
    d.penup()
    d.goto(-140,-10)


    speed(0)

    for step in range(15):
      write(step, align = 'center')
      right(90)
      
      for x in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
      
      penup()  
      #forward(150)
      backward(160)
      left(90)
      forward(20)



    a.right(360)
    a.pendown()
    a.speed(0)

    b.right(360)
    b.pendown()
    b.speed(0)

    c.right(360)
    c.pendown()
    c.speed(0)


    d.right(360)
    d.pendown()
    d.speed(0)

    for x in range(100):
      speed(0)
      a.forward(randint(1,5))
      
      b.forward(randint(1,5))
      
      c.forward(randint(1,5))
      
      d.forward(randint(1,5))
    time.sleep(1)
    turtle.clearscreen() 
      
