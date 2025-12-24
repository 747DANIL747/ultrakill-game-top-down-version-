# src/ui.py
import turtle
from src.constants import *

class GameUI:
    def __init__(self):
        self.score_display = None
        self.health_display = None
        self.combo_display = None
        self.messages_display = None
        self.nickname_display = None
        self.best_score_display = None
        self.leaderboard_display = None
        self.pause_display = None
        self.countdown_display = None
        self.crosshair = None
        self.game_over_display = None
        self.final_score_display = None
        
        self.create_ui_elements()
        
    def create_ui_elements(self):
        """Создает все элементы UI"""
        # Отображение счета
        self.score_display = self.create_text_turtle(-350, 250)
        
        # Отображение здоровья
        self.health_display = self.create_text_turtle(-350, 220)
        
        # Отображение комбо
        self.combo_display = self.create_text_turtle(-350, 190)
        
        # Сообщения комбо
        self.messages_display = self.create_text_turtle(0, 200)
        
        # Таблица лидеров
        self.leaderboard_display = self.create_text_turtle(280, 250)
        
        # Пауза
        self.pause_display = self.create_text_turtle(0, 0)
        
        # Отсчет
        self.countdown_display = self.create_text_turtle(0, 0)
        
        # Прицел
        self.crosshair = turtle.Turtle()
        self.crosshair.shape("circle")
        self.crosshair.color(COLORS["WHITE"])
        self.crosshair.shapesize(0.3)
        self.crosshair.penup()
        self.crosshair.speed(0)
        self.crosshair.hideturtle()
        
    def create_text_turtle(self, x, y):
        """Создает черепаху для отображения текста"""
        text_turtle = turtle.Turtle()
        text_turtle.color(COLORS["WHITE"])
        text_turtle.penup()
        text_turtle.hideturtle()
        text_turtle.goto(x, y)
        return text_turtle
        
    def update_score(self, score):
        """Обновляет отображение счета"""
        self.score_display.clear()
        self.score_display.write(f"SCORE: {score}", font=("Arial", 16, "normal"))
        
    def update_health(self, health):
        """Обновляет отображение здоровья"""
        self.health_display.clear()
        
        # Меняем цвет в зависимости от здоровья
        if health > 70:
            self.health_display.color(COLORS["GREEN"])
        elif health > 40:
            self.health_display.color(COLORS["ORANGE"])
        else:
            self.health_display.color(COLORS["RED"])
            
        self.health_display.write(f"HEALTH: {health}", font=("Arial", 16, "normal"))
        
    def update_combo(self, combo):
        """Обновляет отображение комбо"""
        self.combo_display.clear()
        
        # Меняем цвет в зависимости от комбо
        if combo >= 8:
            self.combo_display.color(COLORS["GOLD"])
        elif combo >= 5:
            self.combo_display.color(COLORS["PURPLE"])
        elif combo >= 3:
            self.combo_display.color(COLORS["ORANGE"])
        else:
            self.combo_display.color(COLORS["RED"])
            
        self.combo_display.write(f"COMBO: x{combo}", font=("Arial", 16, "normal"))
        
    def update_combo_messages(self, messages):
        """Обновляет сообщения комбо"""
        self.messages_display.clear()
        
        for i, msg in enumerate(messages[-3:]):
            self.messages_display.goto(0, 180 - i * 30)
            
            # Разные цвета для разных сообщений
            if "GODLIKE" in msg or "LEGENDARY" in msg:
                self.messages_display.color(COLORS["GOLD"])
            elif "ULTRA" in msg or "MONSTER" in msg:
                self.messages_display.color(COLORS["PURPLE"])
            elif "TRIPLE" in msg or "QUADRUPLE" in msg:
                self.messages_display.color(COLORS["ORANGE"])
            else:
                self.messages_display.color(COLORS["YELLOW"])
                
            self.messages_display.write(msg, align="center", font=("Arial", 14, "normal"))
            
    def show_nickname(self, nickname):
        """Показывает никнейм игрока"""
        self.nickname_display = self.create_text_turtle(-350, 270)
        self.nickname_display.color(COLORS["CYAN"])
        self.nickname_display.write(f"Игрок: {nickname}", font=("Arial", 14, "normal"))
        
    def update_best_score(self, best_score, current_score=0):
        """Обновляет лучший результат игрока"""
        if not hasattr(self, 'best_score_display') or self.best_score_display is None:
            self.best_score_display = self.create_text_turtle(-350, 160)
            
        self.best_score_display.clear()
        
        if current_score > best_score > 0:
            self.best_score_display.color(COLORS["GOLD"])
            self.best_score_display.write(f"НОВЫЙ РЕКОРД!: {current_score}", 
                                         font=("Arial", 12, "bold"))
        elif best_score > 0:
            self.best_score_display.color(COLORS["LIGHTGREEN"])
            self.best_score_display.write(f"ЛУЧШИЙ: {best_score}", 
                                         font=("Arial", 12, "normal"))
            
    def show_leaderboard(self, leaderboard_data, current_player=None):
        """Отображает таблицу лидеров"""
        self.leaderboard_display.clear()
        
        # Заголовок
        self.leaderboard_display.goto(280, 250)
        self.leaderboard_display.color(COLORS["YELLOW"])
        self.leaderboard_display.write("ЛИДЕРЫ:", align="right", font=("Arial", 16, "bold"))
        
        # Отображение записей
        y_pos = 220
        for i, (name, score) in enumerate(leaderboard_data[:5], 1):
            self.leaderboard_display.goto(280, y_pos)
            
            if name == current_player:
                # Проверяем лучший результат игрока
                self.leaderboard_display.color(COLORS["CYAN"])
            else:
                self.leaderboard_display.color(COLORS["WHITE"])
                
            self.leaderboard_display.write(f"{i}. {name}: {score}", 
                                          align="right", font=("Arial", 12, "normal"))
            y_pos -= 25
            
    def update_crosshair(self, x, y):
        """Обновляет позицию прицела"""
        self.crosshair.goto(x, y)
        self.crosshair.showturtle()
        
    def show_pause(self):
        """Показывает сообщение о паузе"""
        self.pause_display.clear()
        self.pause_display.goto(0, 100)
        self.pause_display.color(COLORS["WHITE"])
        self.pause_display.write("ПАУЗА", align="center", font=("Arial", 32, "bold"))
        
        self.pause_display.goto(0, 50)
        self.pause_display.write("Нажмите P для продолжения", align="center", 
                                 font=("Arial", 18, "normal"))
        
        self.pause_display.goto(0, 0)
        self.pause_display.write("Управление: WASD - движение, Пробел/LMB - стрельба в курсор",
                                 align="center", font=("Arial", 14, "normal"))
                                 
    def hide_pause(self):
        """Скрывает сообщение о паузе"""
        self.pause_display.clear()
        
    def show_countdown(self, value):
        """Показывает отсчет"""
        self.countdown_display.clear()
        self.countdown_display.goto(0, 0)
        
        # Разные цвета для разных значений
        if value == 3:
            self.countdown_display.color(COLORS["RED"])
        elif value == 2:
            self.countdown_display.color(COLORS["YELLOW"])
        else:
            self.countdown_display.color(COLORS["GREEN"])
            
        self.countdown_display.write(str(value), align="center",
                                    font=("Arial", 48, "bold"))
                                    
    def hide_countdown(self):
        """Скрывает отсчет"""
        self.countdown_display.clear()
        
    def show_game_over(self, nickname, score, best_score, leaderboard_data):
        """Показывает экран окончания игры"""
        # Очищаем экран
        turtle.clearscreen()
        screen = turtle.Screen()
        screen.bgcolor(COLORS["DARKRED"])
        
        # Game Over
        self.game_over_display = self.create_text_turtle(0, 100)
        self.game_over_display.color(COLORS["RED"])
        self.game_over_display.write("GAME OVER", align="center", font=("Arial", 32, "bold"))
        
        # Финальный счет
        self.final_score_display = self.create_text_turtle(0, 30)
        self.final_score_display.color(COLORS["WHITE"])
        self.final_score_display.write(f"FINAL SCORE: {score}", align="center", 
                                       font=("Arial", 24, "normal"))
        
        # Имя игрока
        player_name_display = self.create_text_turtle(0, -10)
        player_name_display.color(COLORS["CYAN"])
        player_name_display.write(f"Игрок: {nickname}", align="center", 
                                  font=("Arial", 20, "normal"))
        
        # Рекорд
        record_display = self.create_text_turtle(0, -50)
        record_display.color(COLORS["YELLOW"])
        
        if score == best_score and score > 0:
            record_display.write("НОВЫЙ ЛИЧНЫЙ РЕКОРД!", align="center", 
                                 font=("Arial", 18, "bold"))
        elif best_score > score:
            record_display.write(f"Ваш лучший результат: {best_score}", 
                                 align="center", font=("Arial", 16, "normal"))
        
        # Полная таблица лидеров
        self.show_full_leaderboard(leaderboard_data, nickname, score, 0, -120)
        
    def show_full_leaderboard(self, leaderboard_data, current_player, current_score, x, y):
        """Показывает полную таблицу лидеров"""
        leaderboard_title = self.create_text_turtle(x, y)
        leaderboard_title.color(COLORS["YELLOW"])
        leaderboard_title.write("ТАБЛИЦА ЛИДЕРОВ:", align="center", 
                               font=("Arial", 20, "bold"))
        
        y_pos = y - 40
        for i, (name, score_entry) in enumerate(leaderboard_data[:10], 1):
            entry_display = self.create_text_turtle(x, y_pos)
            
            if name == current_player:
                if score_entry == current_score:
                    entry_display.color(COLORS["LIME"])
                    entry_display.write(f"{i}. {name}: {score_entry} ← ВЫ!", 
                                       align="center", font=("Arial", 16, "bold"))
                else:
                    entry_display.color(COLORS["CYAN"])
                    entry_display.write(f"{i}. {name}: {score_entry} ← ВАШ РЕКОРД", 
                                       align="center", font=("Arial", 16, "normal"))
            else:
                entry_display.color(COLORS["WHITE"])
                entry_display.write(f"{i}. {name}: {score_entry}", 
                                   align="center", font=("Arial", 16, "normal"))
            y_pos -= 30