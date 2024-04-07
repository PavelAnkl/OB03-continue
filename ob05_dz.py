import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Основные параметры окна
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка")

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Параметры змейки и еды
snake_pos = [[100, 50], [90, 50], [80, 50]]  # Список сегментов змеи
snake_speed = [10, 0]  # Начальное движение змеи по горизонтали
food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]  # Случайное расположение еды
food_spawn = True
score = 0

# ФПС
clock = pygame.time.Clock()
fps = 10

# Запуск основного цикла игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_speed[1] != 10:
                snake_speed = [0, -10]
            elif event.key == pygame.K_DOWN and snake_speed[1] != -10:
                snake_speed = [0, 10]
            elif event.key == pygame.K_LEFT and snake_speed[0] != 10:
                snake_speed = [-10, 0]
            elif event.key == pygame.K_RIGHT and snake_speed[0] != -10:
                snake_speed = [10, 0]

    # Движение змейки
    snake_pos.insert(0, list(map(lambda x, y: x + y, snake_pos[0], snake_speed)))
    if snake_pos[0] == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_pos.pop()

    # Появление новой еды
    if not food_spawn:
        food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
    food_spawn = True

    # Отрисовка
    screen.fill(BLACK)
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Проверка столкновения змейки со стенами или с собой
    if snake_pos[0][0] >= screen_width or snake_pos[0][0] < 0 or snake_pos[0][1] >= screen_height or snake_pos[0][1] < 0 or snake_pos[0] in snake_pos[1:]:
        running = False

    pygame.display.flip()
    clock.tick(fps)

print(f"Ваш счет: {score}")
pygame.quit()
sys.exit()
