# src/player.py
import turtle
from src.constants import *

class Player:
    def __init__(self, nickname="Player"):
        self.nickname = nickname
        self.score = 0
        self.health = MAX_HEALTH
        self.combo = 0
        self.combo_time = 0
        self.combo_messages = []
        
        # Графический объект
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(COLORS["BLUE"])
        self.turtle.shapesize(1.5)
        self.turtle.penup()
        self.turtle.speed(0)
        
    def move_left(self):
        x = self.turtle.xcor()
        if x > -380:
            self.turtle.setx(x - PLAYER_SPEED)
    
    def move_right(self):
        x = self.turtle.xcor()
        if x < 380:
            self.turtle.setx(x + PLAYER_SPEED)
    
    def move_up(self):
        y = self.turtle.ycor()
        if y < 280:
            self.turtle.sety(y + PLAYER_SPEED)
    
    def move_down(self):
        y = self.turtle.ycor()
        if y > -280:
            self.turtle.sety(y - PLAYER_SPEED)
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
            
    def heal(self, amount):
        self.health = min(MAX_HEALTH, self.health + amount)
        
    def add_score(self, points):
        self.score += points
        
    def add_combo(self):
        self.combo += 1
        self.combo_time = COMBO_DECAY_TIME
        return self.combo
        
    def update_combo(self):
        if self.combo_time > 0:
            self.combo_time -= 1
        elif self.combo > 0:
            self.combo = 0
            return True  # комбо сброшено
        return False
        
    def reset_combo(self):
        lost_combo = self.combo
        self.combo = 0
        self.combo_time = 0
        return lost_combo
        
    def get_position(self):
        return self.turtle.xcor(), self.turtle.ycor()
        
    def hide(self):
        self.turtle.hideturtle()