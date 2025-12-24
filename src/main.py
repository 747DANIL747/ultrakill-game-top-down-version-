# src/main.py
#!/usr/bin/env python3
"""
ULTRAKILL-like Game
Курсовой проект по Python с Docker и Git
"""

import sys
import os

# Добавляем путь к модулям
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.game import Game

def main():
    """Основная функция запуска игры"""
    print("=" * 50)
    print("ULTRAKILL-like Game")
    print("Курсовой проект")
    print("=" * 50)
    print()
    
    try:
        # Создаем и запускаем игру
        game = Game()
        game.run()
        
    except KeyboardInterrupt:
        print("\n\nИгра прервана пользователем")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
        print("Пожалуйста, сообщите об ошибке разработчику")
        
    finally:
        print("\nСпасибо за игру!")
        print("=" * 50)

if __name__ == "__main__":
    main()