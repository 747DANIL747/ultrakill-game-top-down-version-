# src/enemy.py
import turtle
import random
from src.constants import *

class Enemy:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(COLORS["RED"])
        self.turtle.shapesize(1)
        self.turtle.penup()
        self.turtle.speed(0)
        
        # Устанавливаем начальную позицию на краю экрана
        self.spawn_at_edge()
        
    def spawn_at_edge(self):
        side = random.choice(["top", "right", "bottom", "left"])
        
        if side == "top":
            x = random.randint(-350, 350)
            y = 290
        elif side == "right":
            x = 390
            y = random.randint(-250, 250)
        elif side == "bottom":
            x = random.randint(-350, 350)
            y = -290
        else:  # left
            x = -390
            y = random.randint(-250, 250)
            
        self.turtle.goto(x, y)
        
    def move_towards(self, target_x, target_y):
        """Двигается к цели"""
        current_x = self.turtle.xcor()
        current_y = self.turtle.ycor()
        
        dx = target_x - current_x
        dy = target_y - current_y
        distance = max(0.1, (dx**2 + dy**2)**0.5)
        
        move_x = (dx / distance) * ENEMY_SPEED
        move_y = (dy / distance) * ENEMY_SPEED
        
        self.turtle.setx(current_x + move_x)
        self.turtle.sety(current_y + move_y)
        
    def check_collision_with_bullet(self, bullet):
        """Проверка столкновения с пулей"""
        distance = self.turtle.distance(bullet.turtle)
        return distance < 20
        
    def check_collision_with_player(self, player_pos):
        """Проверка столкновения с игроком"""
        distance = self.turtle.distance(player_pos[0], player_pos[1])
        return distance < 25
        
    def hide(self):
        self.turtle.hideturtle()
        
    def is_visible(self):
        return self.turtle.isvisible()