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
                player_atual = pygame.Rect(personagem.posicao_x + 50, personagem.posicao_y + 43, personagem.largura, personagem.altura)
                player_futuro_y = pygame.Rect(personagem.posicao_x + 50, personagem.posicao_y + personagem.velocidade_y + 43, personagem.largura, personagem.altura)
                player_futuro_x = pygame.Rect(personagem.posicao_x + personagem.velocidade_x - background.velocidade + 50, personagem.posicao_y + 43, personagem.largura, personagem.altura)
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
                # ambiente X magia
                for magia in magos.magias:
                    hitbox_magia = pygame.Rect(magia['x'] + background.posicao, magia['y'], 46, 20)
                    if hitbox_magia.colliderect(parede):
                        magos.magias.remove(magia)
                # ambiente X magia boss
                for magia_boss in boss.projeteis:
                    hitbox_magia_boss = pygame.Rect(magia_boss['x'] + background.posicao, magia_boss['y'], 60, 34)
                    if hitbox_magia_boss.colliderect(parede):
                        boss.projeteis.remove(magia_boss)
                # ambiente X projetil boss
                for projetil_boss in boss.projeteis2:
                    hitbox_projetil_boss = pygame.Rect(projetil_boss['x'] + background.posicao, projetil_boss['y'], 30, 21)
                    if hitbox_projetil_boss.colliderect(parede):
                        boss.projeteis2.remove(projetil_boss)
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
            ataque = pygame.Rect(personagem.posicao_x + 70 + personagem.correcao_flip, personagem.posicao_y, personagem.largura + 20, personagem.altura + 40)
            if hitbox_flecha.colliderect(ataque):
                if flecha in inimigos.flechas:
                    inimigos.flechas.remove(flecha)
    # colisões com inimigos
    for inimigo in inimigos.inimigos:
        ataque = pygame.Rect(personagem.posicao_x + 70 + personagem.correcao_flip, personagem.posicao_y, personagem.largura + 20, personagem.altura + 40)
        hitbox_inimigo = pygame.Rect(inimigo[0] + background.posicao, inimigo[1], 50, 100)
        # ataque X inimigo
        if hitbox_inimigo.colliderect(ataque) and personagem.contador_ataque < 12 and personagem.atacando:
            inimigos.inimigos.remove(inimigo)
    # colisões com magias
    for magia in magos.magias:
        # player X magia
        hitbox_magia = pygame.Rect(magia['x'] + background.posicao, magia['y'], 46, 20)
        if hitbox_magia.colliderect(player_atual):
            magos.magias.remove(magia)
            personagem.vidas -= 1
    # colisões com magos
    for mago in magos.magos:
        ataque = pygame.Rect(personagem.posicao_x + 70 + personagem.correcao_flip, personagem.posicao_y, personagem.largura + 20, personagem.altura + 40)
        hitbox_mago = pygame.Rect(mago[0] + background.posicao, mago[1], 50, 100)
        # ataque X mago
        if hitbox_mago.colliderect(ataque) and personagem.contador_ataque < 12 and personagem.atacando:
            magos.magos.remove(mago)
    if background.fase == 2:
        # colisões com magia boss
        for magia_boss in boss.projeteis:
            # player X magia boss
            hitbox_magia_boss = pygame.Rect(magia_boss['x'] + background.posicao, magia_boss['y'], 60, 34)
            if hitbox_magia_boss.colliderect(player_atual):
                boss.projeteis.remove(magia_boss)
                personagem.vidas -= 1
        # colisões com projetil boss
        for projetil_boss in boss.projeteis2:
            # player X flecha
            hitbox_projetil_boss = pygame.Rect(projetil_boss['x'] + background.posicao, projetil_boss['y'], 30, 21)
            if hitbox_projetil_boss.colliderect(player_atual):
                boss.projeteis2.remove(projetil_boss)
                personagem.vidas -= 1
            # ataque X flecha
            if personagem.atacando and personagem.contador_ataque < 12:
                ataque = pygame.Rect(personagem.posicao_x + 70 + personagem.correcao_flip, personagem.posicao_y, personagem.largura + 20, personagem.altura + 40)
                if hitbox_projetil_boss.colliderect(ataque):
                    if projetil_boss in boss.projeteis2:
                        boss.projeteis2.remove(projetil_boss)
        # colisões com o boss
        boss.contador_colisao_player += 1
        boss.contador_colisao_boss += 1
        if boss.teleportando == False:
            ataque = pygame.Rect(personagem.posicao_x + 70 + personagem.correcao_flip, personagem.posicao_y, personagem.largura + 20, personagem.altura + 40)
            hitbox_boss = pygame.Rect(boss.posicao_x + background.posicao - boss.correcao_teleporte + 180, boss.posicao_y + 50, 50, 120)
            # player X boss
            if hitbox_boss.colliderect(player_futuro_x):
                personagem.velocidade_x = 0
                background.velocidade = 0
                if boss.contador_colisao_player > 20:
                    boss.contador_colisao_player = 0
                    personagem.vidas -= 1
            if hitbox_boss.colliderect(player_futuro_y):
                personagem.velocidade_y = hitbox_boss.top - player_atual.bottom
                if boss.contador_colisao_player > 20:
                    boss.contador_colisao_player = 0
                    personagem.vidas -= 1
            # ataque X boss
            if hitbox_boss.colliderect(ataque) and personagem.atacando:
                if boss.contador_colisao_boss > 20:
                    boss.contador_colisao_boss = 0
                    boss.vidas -= 1
            # ataque boss X player
            if boss.espetada:
                ataque_boss_hitbox = pygame.Rect(boss.posicao_x + background.posicao + 40, boss.posicao_y + 60, 360, 40)
                if player_atual.colliderect(ataque_boss_hitbox):
                    if boss.contador_colisao_player > 20:
                        boss.contador_colisao_player = 0
                        personagem.vidas -= 1



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
    boss.projeteis = []
    boss.projeteis2 = []
    inimigos.flechas = []
    magos.magias = []


pygame.init()
w = 1200
h = 700
window = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

background = classes.Background(window)
personagem = classes.Personagem(window)
inimigos = classes.Inimigos(window)
magos = classes.Magos(window)
boss = classes.Boss(window)

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
            if event.key == pygame.K_SPACE or event.key == pygame.K_q:
                personagem.atacando = True


    calcula_vel_tela_movel()
    verifica_colisoes()

    # Carrega fases
    if personagem.posicao_x >= 1200 - personagem.largura:
        background.fase += 1
        inimigos.inimigos = inimigos.inimigos_iniciais[background.fase].copy()
        magos.magos = magos.magos_iniciais[background.fase].copy()
        reset_posicoes()
    # Game Over
    if personagem.posicao_y > 700 or personagem.vidas <= 0:
        background.game_over()
        background.fase = 0
        personagem.vidas = 3
        boss.vidas = 7
        inimigos.flechas = list()
        inimigos.inimigos = inimigos.inimigos_iniciais[background.fase].copy()
        magos.magos = magos.magos_iniciais[background.fase].copy()
        reset_posicoes()
    # Vitória
    if boss.vidas <= 0:
        background.vitoria()
        background.fase = 0
        personagem.vidas = 3
        boss.vidas = 7
        inimigos.flechas = list()
        inimigos.inimigos = inimigos.inimigos_iniciais[background.fase].copy()
        magos.magos = magos.magos_iniciais[background.fase].copy()
        reset_posicoes()
    # Background
    background.load()
    # Inimigos
    inimigos.load(background.posicao, personagem.posicao_x)
    magos.load(background.posicao, personagem.posicao_x)
    boss.load(background.fase, personagem.posicao_x, background.posicao)
    # Personagem
    personagem.load()
    # Vidas
    personagem.load_vidas()
    boss.load_vidas(background.fase)
    # Update
    pygame.display.update()
    # Clock tick
    clock.tick(30)

pygame.quit()