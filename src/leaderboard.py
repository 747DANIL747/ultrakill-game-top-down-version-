# src/leaderboard.py
import os
from src.constants import LEADERBOARD_FILE

class Leaderboard:
    def __init__(self):
        self.file_path = LEADERBOARD_FILE
        
    def load(self):
        """Загружает таблицу лидеров из файла"""
        leaderboard = []
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and ',' in line:
                            name, score_str = line.rsplit(',', 1)
                            try:
                                score = int(score_str)
                                leaderboard.append((name.strip(), score))
                            except ValueError:
                                continue
            except Exception:
                leaderboard = []
        return leaderboard
        
    def save(self, name, score):
        """Сохраняет или обновляет результат игрока"""
        leaderboard = self.load()
        
        # Проверяем, есть ли уже игрок в таблице
        player_index = -1
        for i, (existing_name, existing_score) in enumerate(leaderboard):
            if existing_name == name:
                player_index = i
                break
        
        if player_index != -1:
            # Обновляем, если новый счет лучше
            if score > leaderboard[player_index][1]:
                leaderboard[player_index] = (name, score)
        else:
            # Добавляем нового игрока
            leaderboard.append((name, score))
        
        # Сортируем по убыванию счета
        leaderboard.sort(key=lambda x: x[1], reverse=True)
        
        # Ограничиваем топ-10
        leaderboard = leaderboard[:10]

        os.makedirs("data", exist_ok=True)
        
        # Сохраняем в файл
        with open(self.file_path, 'w', encoding='utf-8') as f:
            for name_entry, score_entry in leaderboard:
                f.write(f"{name_entry},{score_entry}\n")
                
    def get_player_best(self, name):
        """Получает лучший результат игрока"""
        leaderboard = self.load()
        for entry_name, entry_score in leaderboard:
            if entry_name == name:
                return entry_score
        return 0
        
    def get_top(self, limit=10):
        """Получает топ игроков"""
        leaderboard = self.load()
        return leaderboard[:limit]
