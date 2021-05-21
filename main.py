import classes
import pygame

pygame.init()
w = 1200
h = 700
window = pygame.display.set_mode((w, h))
game = True

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        # Background
        background = classes.Background(window)
        background.load()
        # Personagem
        personagem = classes.Personagem(window)
        personagem.load()
        # Update
        pygame.display.update()

pygame.quit()