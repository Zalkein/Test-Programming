from turtle import *

def square():
    penup()
    goto(-200,0 )
    pendown()
    for i in range(4):
        forward(100)
        left(90)

def triangle():
    penup()
    goto(200, 0)
    pendown()
    for i in range(3):
        forward(100)
        left(120)

