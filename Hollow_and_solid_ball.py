import pygame
pygame.init()
window = pygame.display.set_mode((400, 300))
window.fill((100, 100, 100))
BLUE = (0, 0, 139)
pygame.draw.circle(window, BLUE, (300,300), 25, )
pygame.draw.circle(window, BLUE, (100,100), 25, 3)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           runing = False
pygame.quit()