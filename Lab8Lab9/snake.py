import pygame
import sys
import random
import time

pygame.init()

colorBLACK = (0, 0, 0)
colorGRAY = (200, 200, 200)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0) 
colorYELLOW = (255, 255, 0)

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 5

CELL = 30

def draw_grid():
    for i in range (HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY[(i+j) % 2], (i * CELL, j * CELL, CELL, CELL))

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range (HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i+j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.speed = 5  # speed и начальная скорость

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        head = self.body[0]
        head.x += self.dx
        head.y += self.dy

        # Проверка столкновения с границами экрана
        if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
            pygame.quit()
            sys.exit()

        # Проверка столкновения с собственным телом
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                pygame.quit()
                sys.exit()


    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))
    
    def check_collision(self):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            food.respawn()
            self.score += random.randint(1, 3)
            if self.score % 5 == 0:
                self.speed += 1  # Увеличиваем скорость змейки
            return True
        return False


class Food:
    def __init__(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        self.last_spawn_time = pygame.time.get_ticks()  # Запоминаем время последнего появления еды

    def respawn(self):
        while True:
            new_pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            # Проверяем, не находится ли новое местоположение еды внутри змеи
            if new_pos not in snake.body:
                self.pos = new_pos
                break
        self.last_spawn_time = pygame.time.get_ticks()  # Обновляем время последнего появления еды

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
        

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

done = False

snake = Snake()
food = Food()

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1

    draw_grid_chess()

    snake.move()
    snake.draw()

    # Отрисовываем еду на экране
    current_time = pygame.time.get_ticks()  # Получаем текущее время
    if current_time - food.last_spawn_time >= 10000:  # Проверяем, прошло ли 10 секунд
        food.respawn()  # Создаем новую еду
    food.draw()

    # Проверяем столкновение змейки с едой
    if snake.check_collision():
        pass  # Можно добавить что-то еще, если нужно

    pygame.display.flip()
    clock.tick(snake.speed)
