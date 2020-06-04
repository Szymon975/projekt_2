import numpy as np
import scipy
import math as m
import turtle
import random
import time

f=file_object  = open("dane.txt", "w+")
wn=turtle.Screen()
wn.setup(width=1920,height=1200)
wn.bgcolor("black")
wn.title("Apocalypse Simulation")
wn.tracer(0)

def distance(x,y):
    return m.sqrt(x**2+y**2)

m_sun=5
m_moon=1
m_earth=2
m_asteroid=0.1

moon = turtle.Turtle()

radius=90
sun_distance=400
moon.shape("circle")
moon.color("gray")
moon.resizemode()
moon.shapesize(stretch_wid=1, stretch_len=1)
moon.penup()
moon.speed(0)
moon.goto(-radius-sun_distance,0)

earth = turtle.Turtle()

earth.shape("circle")
earth.color("blue")
earth.resizemode()
earth.shapesize(stretch_wid=2.3, stretch_len=2.3)
earth.penup()
earth.speed(0)
earth.goto(-sun_distance,0)


sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.resizemode()
sun.shapesize(stretch_wid=5, stretch_len=5)
sun.penup()
sun.speed(0)
sun.goto(0,0)

turtle
angle=0
sun_angle=0
turtle
area_width=[-900,earth.xcor()]
area_height=[-500,500]

def g_xforce(x,y,alpha):
    return (alpha/((asteroid.xcor()-x)**2+(asteroid.ycor()-y)**2)**1.5)*(-asteroid.xcor()+x)
def g_yforce(x,y,alpha):
    return (alpha/((asteroid.xcor()-x)**2+(asteroid.ycor()-y)**2)**1.5)*(-asteroid.ycor()+y)

y=random.uniform(area_height[0], area_height[1])
x=random.uniform(area_width[0], area_width[1])

asteroid = turtle.Turtle()
asteroid.shape("circle")
asteroid.color("red")
asteroid.resizemode()
asteroid.shapesize(stretch_wid=0.3, stretch_len=0.3)
asteroid.penup()
asteroid.speed(0)
asteroid.goto(x,y)

moon.dangle=2.4/10**4
earth.dangle=2/10**5
asteroid.dx=random.uniform(1/10,0)
asteroid.dy=random.uniform(-1/10,0)
while True:
    wn.update()
    asteroid.dx+= g_xforce(moon.xcor(),moon.ycor(),10)+g_xforce(earth.xcor(),earth.ycor(),20)+g_xforce(sun.xcor(),sun.ycor(),70)
    asteroid.dy+= g_yforce(moon.xcor(),moon.ycor(),10)+g_yforce(earth.xcor(),earth.ycor(),20)+g_yforce(sun.xcor(),sun.ycor(),70)
    asteroid.setx(asteroid.xcor()+asteroid.dx)
    asteroid.sety(asteroid.ycor()+asteroid.dy)
    moon.setx(earth.xcor()+radius*m.cos(angle))
    moon.sety(earth.ycor()+radius*m.sin(angle))
    earth.setx(sun.xcor()-sun_distance*m.cos(sun_angle))
    earth.sety(sun.ycor()-sun_distance*m.sin(sun_angle))
    sun_angle=sun_angle+earth.dangle
    angle=angle+moon.dangle
    if distance(asteroid.xcor(),asteroid.ycor())< distance(50,50) or distance(asteroid.xcor()-earth.xcor(),asteroid.ycor()-earth.ycor())< distance(20,20):
        asteroid.hideturtle()
    if distance(asteroid.xcor()-moon.xcor(),asteroid.ycor()-moon.ycor())< distance(10,10):
        asteroid.hideturtle()
        for i in range(1,1001):
            f.write("%5.2f %10.4e\n" % (i, angle))
wn.mainloop()
