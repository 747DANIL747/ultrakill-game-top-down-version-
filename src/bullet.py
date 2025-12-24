# src/bullet.py
import turtle
import math
from src.constants import *

class Bullet:
    def __init__(self, start_x, start_y, target_x, target_y):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(COLORS["YELLOW"])
        self.turtle.shapesize(0.5)
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(start_x, start_y)
        
        # Вычисляем направление
        dx = target_x - start_x
        dy = target_y - start_y
        distance = max(0.1, math.sqrt(dx*dx + dy*dy))
        
        self.dx = (dx / distance) * BULLET_SPEED
        self.dy = (dy / distance) * BULLET_SPEED
        
    def move(self):
        """Двигает пулю"""
        self.turtle.setx(self.turtle.xcor() + self.dx)
        self.turtle.sety(self.turtle.ycor() + self.dy)
        
    def is_out_of_bounds(self):
        """Проверяет, вышла ли пуля за границы экрана"""
        x, y = self.turtle.xcor(), self.turtle.ycor()
        return (y > 300 or y < -300 or 
                x > 400 or x < -400)
                
    def hide(self):
        self.turtle.hideturtle()
        
    def is_visible(self):
        return self.turtle.isvisible()