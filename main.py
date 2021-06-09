import classes
import pygame


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
        if -30 > personagem.posicao_x:
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
    # colisões com o ambiente
    for linha in background.plano1[background.fase]:
        for bloco in linha:
            if bloco in background.blocos_solidos[background.fase]:
                parede = pygame.Rect(x + background.posicao, y, 50, 50)
                player_atual = pygame.Rect(personagem.posicao_x + 17 - personagem.correcao_flip, personagem.posicao_y + 43, personagem.largura, personagem.altura)
                player_futuro_y = pygame.Rect(personagem.posicao_x + 17 - personagem.correcao_flip, personagem.posicao_y + personagem.velocidade_y + 43, personagem.largura, personagem.altura)
                player_futuro_x = pygame.Rect(personagem.posicao_x + personagem.velocidade_x - background.velocidade + 17 - personagem.correcao_flip, personagem.posicao_y + 43, personagem.largura, personagem.altura)
                # colisões no eixo x (player X ambiente)
                if player_futuro_x.colliderect(parede):
                    personagem.velocidade_x = 0
                    background.velocidade = 0
                # colisões no eixo y (player X ambiente)
                if player_futuro_y.colliderect(parede):
                    # colisao cima
                    if personagem.velocidade_y < 0:
                        personagem.velocidade_y = parede.bottom - player_atual.top
                    # colisao baixo
                    elif personagem.velocidade_y > 0:
                        personagem.velocidade_y = parede.top - player_atual.bottom
                        if personagem.pulando:
                            personagem.velocidade_y = -18
                # ambiente X flechas
                for flecha in inimigos.flechas:
                    hitbox_flecha = pygame.Rect(flecha['x'] + background.posicao, flecha['y'], 72, 10)
                    if hitbox_flecha.colliderect(parede):
                        inimigos.flechas.remove(flecha)
            x += 50
        x = 0
        y += 50
    # colisões com flechas
    for flecha in inimigos.flechas:
        # player X flecha
        hitbox_flecha = pygame.Rect(flecha['x'] + background.posicao, flecha['y'], 72, 10)
        if hitbox_flecha.colliderect(player_atual):
            inimigos.flechas.remove(flecha)
            personagem.vidas -= 1
        # ataque X flecha
        if personagem.atacando and personagem.contador_ataque < 12:
            ataque = pygame.Rect(personagem.posicao_x + 40 + personagem.correcao_flip*3/4, personagem.posicao_y, personagem.largura + 20, personagem.altura)
            if hitbox_flecha.colliderect(ataque):
                if flecha in inimigos.flechas:
                    inimigos.flechas.remove(flecha)
    # colisões com inimigos
    for inimigo in inimigos.inimigos:
        ataque = pygame.Rect(personagem.posicao_x + 40 + personagem.correcao_flip*3/4, personagem.posicao_y, personagem.largura + 20, personagem.altura)
        hitbox_inimigo = pygame.Rect(inimigo[0] + background.posicao, inimigo[1], 50, 100)
        # ataque X inimigo
        if hitbox_inimigo.colliderect(ataque) and personagem.contador_ataque < 12 and personagem.atacando:
            inimigos.inimigos.remove(inimigo)


def reset_posicoes():
    personagem.posicao_y = 500
    personagem.posicao_x = 200
    background.posicao = 0
    personagem.velocidade_y = 0
    personagem.velocidade_x = 0
    background.velocidade = 0
    personagem.direita = False
    personagem.esquerda = False
    personagem.pulando = False


pygame.init()
w = 1200
h = 700
window = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

background = classes.Background(window)
personagem = classes.Personagem(window)
inimigos = classes.Inimigos(window)

# Tela de início
background.tela_inicio()

# Jogo
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
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                personagem.pulando = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                personagem.pulando = False
        
        # Ataque
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                personagem.atacando = True


    calcula_vel_tela_movel()
    verifica_colisoes()

    # Carrega fases
    if personagem.posicao_x >= 1100 - personagem.largura:
        background.fase += 1
        inimigos.inimigos = inimigos.inimigos_iniciais[background.fase].copy()
        reset_posicoes()
    # Game Over
    if personagem.posicao_y > 700 or personagem.vidas <= 0:
        background.game_over()
        personagem.vidas = 3
        inimigos.flechas = list()
        inimigos.inimigos = inimigos.inimigos_iniciais[background.fase].copy()
        reset_posicoes()
    # Background
    background.load()
    # Inimigos
    inimigos.load(background.posicao, personagem.posicao_x)
    # Personagem
    personagem.load()
    # Vidas
    personagem.load_vidas()
    # Update
    pygame.draw.rect(window, (255, 0 , 0), pygame.Rect(personagem.posicao_x + 40 + personagem.correcao_flip*3/4, personagem.posicao_y, personagem.largura + 20, personagem.altura))
    pygame.display.update()
    # Clock tick
    clock.tick(30)

pygame.quit()