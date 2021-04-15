# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 01:23:47 2021

@author: Junio
"""
import pygame
import random
import numpy as np
import textReader as t
from turtle import Turtle, Screen

text = t.text
relation = t.relation_entre_matiere(text)

RADIUS = 5

FONT_SIZE = 18

FONT = ("Arial", FONT_SIZE, "normal")

def randomF(nb):
    return random.randint(0,nb)

def exist(nb, liste):
    for k in liste:
        if nb in [nb-70, nb+70]:
            return True
        else: return False
    
def draw_node(turtle, text, x, y):
    turtle.up()
    turtle.goto(x, y - RADIUS)
    turtle.down()
    turtle.circle(RADIUS)
    turtle.up()
    turtle.goto(x, y - FONT_SIZE // 2)
    turtle.write(text, align="center", font=FONT)

def draw_design(turtle):
    turtle.color("white")
    turtle.pensize(4)
    
    list_x = []
    list_y = []
    
    for modules in relation.items():
        module = modules[0].split(' - ')[0]
        
        x = randomF(300)
        y = randomF(200)
        
        while exist(x, list_x):
            x = randomF(300)
        list_x.append(x)
        
        while exist(y, list_y):
            y = randomF(200)
        list_y.append(y)
        
        draw_node(turtle, module, x, y)


screen = Screen()
screen.setup (width=800, height=600, startx=0, starty=0)
screen.bgcolor("blue")
yertle = Turtle(shape="turtle")
draw_design(yertle)
yertle.home()
screen.exitonclick()