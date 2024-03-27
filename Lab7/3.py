import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 400))
ball_x = 400
ball_y = 200
ball_speed = 20

running = True

while running:

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', (ball_x, ball_y), 25)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ball_x > 50:
        ball_x -= ball_speed
    elif keys[pygame.K_RIGHT] and ball_x < 750:
        ball_x += ball_speed
    elif keys[pygame.K_UP] and ball_y > 50:
        ball_y -= ball_speed
    elif keys[pygame.K_DOWN] and ball_y < 350:
        ball_y += ball_speed

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    clock.tick(10)