from turtle import Turtle as turtle
from turtle import Screen

def blink():
    for turtle in screen.turtles():
        turtle.fillcolor('yellow' if turtle.fillcolor() == 'black' else 'black')

    screen.ontimer(blink, 1000)
turtle.write(arg="Home = ", move=True, align="center")

turtle.write((0,0), True)
def Base():
    for i in range(0, 4):
        pen9 = Turtle(shape='square')
        pen9.color('white')
        pen9.penup()
        pen9.speed(100)
        pen9.sety(-100)
        pen9.setx(-200+(i*100))
        pen9.shapesize(1, 2)
        pen9.color('black')


def Pole():
    for i in range(0, 4):
        pen9 = Turtle(shape='square')
        pen9.shapesize(9, 1)
        pen9.color('white')
        pen9.speed(100)
        pen9.penup()
        pen9.sety(-15)
        pen9.setx(-200+(i*100))
        pen9.color('black')


def Back():
    for i in range(0,4):
        pen9 = Turtle(shape='square')
        pen9.color('white')
        pen9.shapesize(7.6, 2.5)
        pen9.speed(100)
        pen9.color('black')
        pen9.penup()
        pen9.sety(150)
        pen9.setx(-200+(i*100))


def Lights(num):
    for i in range(0, 4):
        if(i==num):
            continue
        else:
            pen1 = Turtle(shape='circle')
            pen1.color('white')
            pen1.speed(100)
            pen1.shapesize(2)
            pen1.color('red')
            pen1.penup()
            pen1.sety(200)
            pen1.setx(-200+(i*100))

            pen2 = Turtle(shape='circle')
            pen2.color('white')
            pen2.speed(100)
            pen2.shapesize(2)
            pen2.color('yellow')
            pen2.penup()
            pen2.sety(150)
            pen2.setx(-200+(i*100))

            pen3 = Turtle(shape='circle')
            pen3.color('white')
            pen3.speed(100)
            pen3.shapesize(2)
            pen3.color('green')
            pen3.penup()
            pen3.sety(100)
            pen3.setx(-200+(i*100))



screen = Screen()
#Pole()
#Base()
#Back()

#Lights(1)
#blink()
#board=turtle.Turtle()

screen.mainloop()