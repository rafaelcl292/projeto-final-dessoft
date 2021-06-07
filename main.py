import classes
import pygame
import time


def calcula_vel_tela_movel(vel=10):
    if personagem.direita == personagem.esquerda:
        personagem.velocidade_x = 0
        background.velocidade = 0
    elif personagem.direita:
        if personagem.posicao_x > 500 - personagem.largura:
            if -background.posicao < len(background.plano1[background.fase][-1]) * 50 - w:
                personagem.velocidade_x = 0
                background.velocidade = - vel
            else:
                if personagem.posicao_x < w - personagem.largura:
                    personagem.velocidade_x = vel
                    background.velocidade = 0
                else:
                    personagem.velocidade_x = 0
                    background.velocidade = 0
        else:
            personagem.velocidade_x = vel
            background.velocidade = 0
    elif personagem.esquerda:
        if 50 > personagem.posicao_x:
            if background.posicao < 0:
                personagem.velocidade_x = 0
                background.velocidade = vel
            else:
                if 0 < personagem.posicao_x:
                    personagem.velocidade_x = - vel
                    background.velocidade = 0
                else:
                    personagem.velocidade_x = 0
                    background.velocidade = 0
        else:
            personagem.velocidade_x = - vel
            background.velocidade = 0


def verifica_colisoes():
    x = 0
    y = 0
    personagem.velocidade_y += 1
    for linha in background.plano1[background.fase]:
        for bloco in linha:
            if bloco in background.blocos_solidos[background.fase]:
                parede = pygame.Rect(x + background.posicao, y, 50, 50)
                player_atual = pygame.Rect(personagem.posicao_x, personagem.posicao_y, personagem.largura, personagem.altura)
                player_futuro_y = pygame.Rect(personagem.posicao_x, personagem.posicao_y + personagem.velocidade_y, personagem.largura, personagem.altura)
                player_futuro_x = pygame.Rect(personagem.posicao_x + personagem.velocidade_x - background.velocidade, personagem.posicao_y, personagem.largura, personagem.altura)
                # colisões no eixo x
                if player_futuro_x.colliderect(parede):
                    personagem.velocidade_x = 0
                    background.velocidade = 0
                # colisões no eixo y
                if player_futuro_y.colliderect(parede):
                    # colisao cima
                    if personagem.velocidade_y < 0:
                        personagem.velocidade_y = parede.bottom - player_atual.top
                    # colisao baixo
                    elif personagem.velocidade_y > 0:
                        personagem.velocidade_y = parede.top - player_atual.bottom
                        if personagem.pulando:
                            personagem.velocidade_y = -18
            x += 50
        x = 0
        y += 50


pygame.init()
w = 1200
h = 700
window = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

background = classes.Background(window)
personagem = classes.Personagem(window)

while background.game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            background.game = False
        # Movimentos no eixo X
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                personagem.esquerda = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                personagem.direita = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                personagem.esquerda = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                personagem.direita = False
                
        # Movimentos no eixo Y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                personagem.pulando = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                personagem.pulando = False

    calcula_vel_tela_movel()
    verifica_colisoes()

    # Carrega fases
    if personagem.posicao_x >= 1100 - personagem.largura:
        background.fase += 1
        personagem.posicao_y = 550
        personagem.posicao_x = 200
        background.posicao = 0
        personagem.velocidade_y = 0
        personagem.velocidade_x = 0
        background.velocidade = 0
    # Background
    background.load()
    # Personagem
    personagem.load()
    # Update
    pygame.display.update()
    # Clock tick
    clock.tick(30)

pygame.quit()