import pygame
import sys
import random
import time

pygame.init()

# Размеры экрана
WIDTH = 400
HEIGHT = 600

# Цвета
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Создание шрифта для отображения текста
font = pygame.font.Font(None, 36)

# Загрузка фона
bg = pygame.image.load('resources/bg.png')

# Работа цикла игры
running = True

# Класс для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 500)

    # Функция для движения игрока
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(5, 0)
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-5, 0)

# Класс для врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint (0 + self.rect.w // 2, WIDTH - self.rect.w) , 20))
        self.speed = 5

    # Функция для движения врага
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect[1] + self.rect[3] > HEIGHT:
            self.rect.center = ((random.randint (0 + self.rect.w // 2, WIDTH - self.rect.w) , 20))

    # Функция для создания нового врага
    def spawn(self):
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

# Событие для увеличения скорости врага
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Создание игрока и врага
E1 = Enemy()
P1 = Player()

# Создание групп спрайтов для врагов и всех спрайтов
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Определение различных типов монет с весами
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/coin.png')
        self.rect = self.image.get_rect()

    # Функция для появления монет
    def spawn(self):
        self.rect.center = (random.randint(0, WIDTH), 500)

# Отслеживание количества собранных монет
coin_count = 0

# Увеличение скорости врага, когда игрок зарабатывает N монет
N = 10  # Определение порога для увеличения скорости

# Добавление врага в группу врагов и в группу всех спрайтов
enemies.add(E1)
all_sprites.add(E1)
# Добавление игрока в группу всех спрайтов
all_sprites.add(P1)

# Создание группы для монеток и добавление в нее монетки
coins = pygame.sprite.Group()
coin = Coin()
coin.spawn()
coins.add(coin)

# Переменная для счетчика монет
coin_count = 0

# Количество кадров в секунду
FPS = 60

# Создание объекта Clock для управления частотой обновления экрана
clock = pygame.time.Clock()

# Основной цикл игры
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Увеличение скорости врага
        if coin_count >= N:
            E1.speed += 1
            N += 10 # Увеличение порога для следующего увеличения скорости

    # Отрисовка фона
    screen.blit(bg, (0, 0))

    # Отрисовка текста с количеством монет
    text = font.render("Coins: " + str(coin_count), True, colorWHITE)
    screen.blit(text, (10, 10))

    # Перемещение всех спрайтов и их отрисовка на экране
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    # Отрисовка всех монеток на экране
    for coin in coins:
        screen.blit(coin.image, coin.rect)
    
    # Проверка столкновения игрока с монеткой
    if pygame.sprite.spritecollide(P1, coins, True):
        coin_count += random.randint(1, 3)  # Увеличение счетчика монет

    #Cоздаем новую монетку и добавляем ее в группу монеток
        new_coin = Coin()
        new_coin.spawn()
        coins.add(new_coin)

    if pygame.sprite.spritecollideany(P1, enemies):
        print("Collision!")
        screen.fill(colorRED)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.flip()

    clock.tick(FPS)


pygame.time.set_timer(INC_SPEED, 0)

       
