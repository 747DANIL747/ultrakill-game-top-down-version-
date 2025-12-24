# src/game.py
import turtle
import random
import time
from src.player import Player
from src.enemy import Enemy
from src.bullet import Bullet
from src.leaderboard import Leaderboard
from src.ui import GameUI
from src.constants import *

class Game:
    def __init__(self):
        # Инициализация экрана
        self.screen = turtle.Screen()
        self.setup_screen()
        
        # Получение никнейма игрока
        nickname = self.get_nickname()
        
        # Инициализация компонентов игры
        self.player = Player(nickname)
        self.ui = GameUI()
        self.leaderboard = Leaderboard()
        
        # Состояние игры
        self.bullets = []
        self.enemies = []
        self.game_paused = False
        self.countdown_active = False
        self.countdown_value = 0
        self.game_over = False
        self.enemy_timer = 0
        
        # Сообщения комбо
        self.combo_messages = []
        
        # Настройка управления
        self.setup_controls()
        
        # Инициализация UI
        self.initialize_ui()
        
    def setup_screen(self):
        """Настраивает игровой экран"""
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.title(SCREEN_TITLE)
        self.screen.bgcolor(COLORS["BLACK"])
        self.screen.tracer(0)
        
    def get_nickname(self):
        """Получает никнейм игрока"""
        nickname = self.screen.textinput(SCREEN_TITLE, "Введите ваш никнейм:")
        return nickname if nickname else "Player"
        
    def setup_controls(self):
        """Настраивает управление"""
        self.screen.listen()
        
        # Движение
        self.screen.onkeypress(self.player.move_left, "a")
        self.screen.onkeypress(self.player.move_left, "A")
        self.screen.onkeypress(self.player.move_right, "d")
        self.screen.onkeypress(self.player.move_right, "D")
        self.screen.onkeypress(self.player.move_up, "w")
        self.screen.onkeypress(self.player.move_up, "W")
        self.screen.onkeypress(self.player.move_down, "s")
        self.screen.onkeypress(self.player.move_down, "S")
        
        # Стрельба
        self.screen.onkeypress(self.shoot_at_cursor, "space")
        
        # Пауза
        self.screen.onkeypress(self.toggle_pause, "p")
        self.screen.onkeypress(self.toggle_pause, "P")
        
        # Мышь
        self.screen.onscreenclick(self.handle_mouse_click)
        self.screen.onscreenclick(self.update_cursor_position)
        
    def initialize_ui(self):
        """Инициализирует пользовательский интерфейс"""
        self.ui.show_nickname(self.player.nickname)
        
        # Показываем лучший результат игрока
        best_score = self.leaderboard.get_player_best(self.player.nickname)
        self.ui.update_best_score(best_score)
        
        # Показываем начальную таблицу лидеров
        leaderboard_data = self.leaderboard.get_top(5)
        self.ui.show_leaderboard(leaderboard_data, self.player.nickname)
        
    def shoot_at_cursor(self):
        """Стрельба в направлении курсора"""
        if self.game_paused or self.countdown_active:
            return
            
        # Получаем текущую позицию курсора
        x, y = self.get_cursor_position()
        self.create_bullet(x, y)
        
    def handle_mouse_click(self, x, y):
        """Обработка клика мыши"""
        if self.game_paused or self.countdown_active:
            return
            
        self.create_bullet(x, y)
        
    def create_bullet(self, target_x, target_y):
        """Создает пулю"""
        player_x, player_y = self.player.get_position()
        bullet = Bullet(player_x, player_y, target_x, target_y)
        self.bullets.append(bullet)
        
    def update_cursor_position(self, x, y):
        """Обновляет позицию курсора"""
        if not self.game_paused and not self.countdown_active:
            self.ui.update_crosshair(x, y)
            
    def get_cursor_position(self):
        """Возвращает текущую позицию курсора"""
        # В реальной реализации нужно получать позицию мыши
        # Для упрощения возвращаем текущую позицию прицела
        return self.ui.crosshair.xcor(), self.ui.crosshair.ycor()
        
    def toggle_pause(self):
        """Включает/выключает паузу"""
        if self.countdown_active:
            return
            
        if not self.game_paused:
            self.game_paused = True
            self.ui.show_pause()
            self.ui.crosshair.hideturtle()
        else:
            self.countdown_active = True
            self.countdown_value = 3
            self.ui.hide_pause()
            self.start_countdown()
            
    def start_countdown(self):
        """Запускает отсчет"""
        self.countdown_step()
        
    def countdown_step(self):
        """Шаг отсчета"""
        if self.countdown_value > 0:
            self.ui.show_countdown(self.countdown_value)
            self.countdown_value -= 1
            self.screen.ontimer(self.countdown_step, 1000)
        else:
            self.ui.hide_countdown()
            self.game_paused = False
            self.countdown_active = False
            self.ui.crosshair.showturtle()
            
    def create_enemy(self):
        """Создает нового врага"""
        if len(self.enemies) < MAX_ENEMIES:
            enemy = Enemy()
            self.enemies.append(enemy)
            
    def handle_combo(self):
        """Обрабатывает комбо"""
        combo = self.player.add_combo()
        
        # Добавляем сообщение комбо
        if combo in COMBO_MESSAGES:
            message = COMBO_MESSAGES[combo]
        elif combo >= 8:
            message = f"+ {combo}x LEGENDARY COMBO!"
        else:
            message = "+ KILL"
            
        self.combo_messages.append(message)
        
        # Вычисляем бонусные очки
        base_points = SCORE_PER_KILL
        combo_bonus = combo * SCORE_PER_COMBO_MULTIPLIER
        total_points = base_points + combo_bonus
        
        self.player.add_score(total_points)
        
        # Восстановление здоровья за высокие комбо
        if combo >= 5:
            heal_amount = min(15, combo * 2)
            self.player.heal(heal_amount)
            
        # Дополнительный бонус за очень длинные комбо
        if combo >= 10:
            self.player.add_score(100)  # Mega bonus
            
    def update_game_state(self):
        """Обновляет состояние игры"""
        if self.game_paused or self.countdown_active or self.game_over:
            return
            
        # Обновление комбо
        if self.player.update_combo():
            self.combo_messages.append(f"COMBO LOST! x{self.player.combo}")
            
        # Создание врагов
        self.enemy_timer += 1
        if self.enemy_timer >= ENEMY_SPAWN_RATE:
            self.create_enemy()
            self.enemy_timer = 0
            
        # Обновление пуль
        for bullet in self.bullets[:]:
            bullet.move()
            
            if bullet.is_out_of_bounds():
                bullet.hide()
                self.bullets.remove(bullet)
                
        # Обновление врагов
        player_pos = self.player.get_position()
        
        for enemy in self.enemies[:]:
            # Движение к игроку
            enemy.move_towards(player_pos[0], player_pos[1])
            
            # Проверка столкновений с пулями
            for bullet in self.bullets[:]:
                if enemy.check_collision_with_bullet(bullet):
                    bullet.hide()
                    self.bullets.remove(bullet)
                    enemy.hide()
                    self.enemies.remove(enemy)
                    self.handle_combo()
                    break
                    
            # Проверка столкновений с игроком
            if enemy.check_collision_with_player(player_pos):
                enemy.hide()
                self.enemies.remove(enemy)
                self.player.take_damage(DAMAGE_PER_ENEMY)
                
                # Сброс комбо при получении урона
                if self.player.combo > 0:
                    lost_combo = self.player.reset_combo()
                    self.combo_messages.append(f"УРОН! Комбо сброшено: x{lost_combo}")
                    
        # Проверка окончания игры
        if self.player.health <= 0:
            self.end_game()
            
    def update_ui(self):
        """Обновляет пользовательский интерфейс"""
        self.ui.update_score(self.player.score)
        self.ui.update_health(self.player.health)
        self.ui.update_combo(self.player.combo)
        self.ui.update_combo_messages(self.combo_messages)
        
        # Обновляем лучший результат
        best_score = self.leaderboard.get_player_best(self.player.nickname)
        self.ui.update_best_score(best_score, self.player.score)
        
        # Обновляем таблицу лидеров
        if not self.game_paused and not self.countdown_active:
            leaderboard_data = self.leaderboard.get_top(5)
            self.ui.show_leaderboard(leaderboard_data, self.player.nickname)
            
    def end_game(self):
        """Завершает игру"""
        self.game_over = True
        
        # Сохраняем результат
        self.leaderboard.save(self.player.nickname, self.player.score)
        
        # Получаем данные для экрана окончания
        best_score = self.leaderboard.get_player_best(self.player.nickname)
        leaderboard_data = self.leaderboard.get_top(10)
        
        # Очищаем экран
        self.clear_game_objects()
        
        # Показываем экран окончания игры
        self.ui.show_game_over(self.player.nickname, self.player.score, 
                              best_score, leaderboard_data)
        
    def clear_game_objects(self):
        """Очищает игровые объекты"""
        self.player.hide()
        
        for bullet in self.bullets:
            bullet.hide()
            
        for enemy in self.enemies:
            enemy.hide()
            
    def run(self):
        """Запускает основной игровой цикл"""
        while not self.game_over:
            self.screen.update()
            
            self.update_game_state()
            self.update_ui()
            
            time.sleep(0.03)
            
        # Ждем клика для закрытия
        self.screen.exitonclick()