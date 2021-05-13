import pygame

pygame.init()
w = 1024
h = 576
window = pygame.display.set_mode((w, h))
game = True

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        window.fill((255, 255, 255))
        pygame.display.update()

pygame.quit()