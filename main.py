import classes
import pygame


def calcula_vel_tela_movel(vel=8):
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
    for linha in background.plano1[background.fase]:
        for bloco in linha:
            if bloco in background.blocos_solidos[background.fase]:
                # print(x, y, personagem.posicao_x, personagem.posicao_y)
                pass
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

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
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
    if personagem.pulando:
        if personagem.contador_pulo >= -25:
            personagem.posicao_y -= personagem.contador_pulo ** 2 * 0.05 * -(int(personagem.contador_pulo < 0) * 2 - 1)
            personagem.contador_pulo -= 1
        else:
            personagem.pulando = False
            personagem.contador_pulo = 25
    calcula_vel_tela_movel()
    verifica_colisoes()

    # Carrega fases
    if personagem.posicao_x >= 1100 - personagem.largura:
        background.fase = 1
        personagem.pulando = False
        personagem.contador_pulo = 25
        personagem.posicao_y = 550
        personagem.posicao_x = 200
        background.posicao = 0
    
    # Background
    background.load()
    # Personagem
    personagem.load()
    # Update
    pygame.display.update()
    # Clock tick
    clock.tick(60)

pygame.quit()