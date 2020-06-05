import numpy as np
import scipy
import math as m
import turtle
import random
import time

wn=turtle.Screen()
wn.setup(width=1920,height=1200)
wn.bgcolor("black")
wn.title("Apocalypse Simulation")

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

def moon_xforce(x,alpha=10**3):
    return (alpha/((asteroid.xcor()-x)**2+(asteroid.ycor()-moon.ycor())**2)**1.5)*(-asteroid.xcor()+x)
def earth_xforce(x,beta=2*10**3):
    return (beta/((asteroid.xcor()-x)**2+(asteroid.ycor()-earth.ycor())**2)**1.5)*(-asteroid.xcor()+x)
def sun_xforce(x,gamma=5*10**3):
    return (gamma/((asteroid.xcor()-x)**2+(asteroid.ycor()-sun.ycor())**2)**1.5)*(-asteroid.xcor()+x)
def moon_yforce(y,alpha=10**3):
    return (alpha/((asteroid.xcor()-y)**2+(asteroid.ycor()-moon.ycor())**2)**1.5)*(-asteroid.ycor()+y)
def earth_yforce(y,beta=2*10**3):
    return (beta/((asteroid.xcor()-y)**2+(asteroid.ycor()-earth.ycor())**2)**1.5)*(-asteroid.ycor()+y)
def sun_yforce(y,gamma=5*10**3):
    return (gamma/((asteroid.xcor()-y)**2+(asteroid.ycor()-sun.ycor())**2)**1.5)*(-asteroid.ycor()+y)

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

moon.dangle=0.036
earth.dangle=0.003
asteroid.dx=0
asteroid.dy=0
while True:
    asteroid.dx+= moon_xforce(moon.xcor())+earth_xforce(earth.xcor())+sun_xforce(sun.xcor())
    asteroid.dy+= moon_yforce(moon.ycor())+earth_yforce(earth.ycor())+sun_yforce(sun.ycor())
    asteroid.setx(asteroid.xcor()+asteroid.dx)
    asteroid.sety(asteroid.ycor()+asteroid.dy)
    moon.setx(earth.xcor()+radius*m.cos(angle))
    moon.sety(earth.ycor()+radius*m.sin(angle))
    earth.setx(sun.xcor()-sun_distance*m.cos(sun_angle))
    earth.sety(sun.ycor()-sun_distance*m.sin(sun_angle))
    sun_angle=sun_angle+earth.dangle
    angle=angle+moon.dangle

wn.mainloop()

x

