import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 400))

dino_rect = pygame.Rect(100, 250, 64, 64)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, (100, 100, 100), dino_rect)

    pygame.display.update()
    
    
    
    
    