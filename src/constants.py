# src/constants.py
# Константы игры

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ULTRAKILL-like Game"

# Игровые константы
PLAYER_SPEED = 15
ENEMY_SPEED = 2
BULLET_SPEED = 10
ENEMY_SPAWN_RATE = 30  # кадры между спавном врагов
MAX_ENEMIES = 20

# Здоровье
MAX_HEALTH = 100
DAMAGE_PER_ENEMY = 10

# Очки
SCORE_PER_KILL = 10
SCORE_PER_COMBO_MULTIPLIER = 10

# Комбо
COMBO_DECAY_TIME = 30  # кадры до сброса комбо
COMBO_MESSAGES = {
    2: "+ BIPOLAR",
    3: "+ TRIPLE KILL",
    4: "+ QUADRUPLE KILL",
    5: "+ ULTRA KILL!",
    6: "+ MONSTER KILL!",
    7: "+ GODLIKE!",
    8: "+ LEGENDARY COMBO!"
}

# Цвета
COLORS = {
    "BLACK": "black",
    "WHITE": "white",
    "RED": "red",
    "GREEN": "green",
    "BLUE": "blue",
    "YELLOW": "yellow",
    "CYAN": "cyan",
    "ORANGE": "orange",
    "PURPLE": "purple",
    "GOLD": "gold",
    "LIGHTGREEN": "lightgreen",
    "DARKRED": "darkred",
    "LIME": "lime"
}

# Файлы
LEADERBOARD_FILE = "data/leaderboard.txt"
