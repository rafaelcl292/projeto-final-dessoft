import classes
import pygame

pygame.init()
w = 1200
h = 700
window = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

background = classes.Background(window)
personagem = classes.Personagem(window)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Movimentos no background
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                background.velocidade += 8
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                background.velocidade -= 8
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                background.velocidade -= 8
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                background.velocidade += 8
        # Movimentos do personagem
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                personagem.pulando = True
    if personagem.pulando:
        if personagem.contador_pulo >= -25:
            personagem.posicao -= personagem.contador_pulo ** 2 * 0.05 * -(int(personagem.contador_pulo < 0) * 2 - 1)
            personagem.contador_pulo -= 1
        else:
            personagem.pulando = False
            personagem.contador_pulo = 25
    # Background
    background.load()
    # Personagem
    personagem.load()
    window.blit(pygame.transform.scale(pygame.image.load('tiles/nuvem.png'), (500, 500)), (0, 0))
    # Update
    pygame.display.update()
    # Clock tick
    clock.tick(60)

pygame.quit()