import pygame
from pygame import time


class Background():
    def __init__(self, window):
        self.window = window
        self.fase = 0
        self.posicao = 0
        self.velocidade = 0
        self.tiles = {
            'grama': pygame.transform.scale(pygame.image.load('tiles/grama.png'), (50, 50)),
            'terra': pygame.transform.scale(pygame.image.load('tiles/terra.png'), (50, 50)),
            'nuvem': pygame.transform.scale(pygame.image.load('tiles/nuvem.png'), (500, 500)),
            'chão caverna': pygame.transform.scale(pygame.image.load('tiles/chao_caverna.png'), (50, 50)),
            'montanha': pygame.transform.scale(pygame.image.load('tiles/montanha_nuvens.png'), (2400, 700)),
            'pedra': pygame.transform.scale(pygame.image.load('tiles/pedra.png'), (50, 50)),
            'caverna': pygame.transform.scale(pygame.image.load('tiles/fundo_caverna.png'), (2400, 700))
        }
        self.plano1 = [
            # fase 1
            [
                [0]*100,  # y = 0
                [0]*100,  # y = 50
                [0]*100,  # y = 100
                [0]*100,  # y = 150
                [0]*100,  # y = 200
                [0]*100,  # y = 250
                [0]*100,  # y = 300
                [0]*100,  # y = 350
                [0]*100,  # y = 400
                [0]*100,  # y = 450
                [0]*100,  # y = 500
                [0]*100,  # y = 550
                [0, 1, 0, 0, 0]*20,  # y = 600
                [1, 2, 0, 1, 1]*20,  # y = 650
            ],[
                # fase 2
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 0
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 50
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 100
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 150
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 200
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 250
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 300
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 350
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 400
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 450
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 500
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 550
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 600
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 650
            ],[
                # fase 3
                [0]*100,  # y = 0
                [0]*100,  # y = 50
                [0]*100,  # y = 100
                [0]*100,  # y = 150
                [0]*100,  # y = 200
                [0]*100,  # y = 250
                [0]*100,  # y = 300
                [0]*100,  # y = 350
                [0]*100,  # y = 400
                [0]*100,  # y = 450
                [0]*100,  # y = 500
                [0]*100,  # y = 550
                [0]*100,  # y = 600
                [0]*100,  # y = 650
            ],[
                # fase 4
                [0]*100,  # y = 0
                [0]*100,  # y = 50
                [0]*100,  # y = 100
                [0]*100,  # y = 150
                [0]*100,  # y = 200
                [0]*100,  # y = 250
                [0]*100,  # y = 300
                [0]*100,  # y = 350
                [0]*100,  # y = 400
                [0]*100,  # y = 450
                [0]*100,  # y = 500
                [0]*100,  # y = 550
                [0]*100,  # y = 600
                [0]*100,  # y = 650
            ],[
                # fase 5
                [0]*100,  # y = 0
                [0]*100,  # y = 50
                [0]*100,  # y = 100
                [0]*100,  # y = 150
                [0]*100,  # y = 200
                [0]*100,  # y = 250
                [0]*100,  # y = 300
                [0]*100,  # y = 350
                [0]*100,  # y = 400
                [0]*100,  # y = 450
                [0]*100,  # y = 500
                [0]*100,  # y = 550
                [0]*100,  # y = 600
                [0]*100,  # y = 650
            ],
        ]
        self.plano2 = [self.tiles['montanha'], self.tiles['caverna']]
        self.block_address_index = [
            [None, self.tiles['grama'], self.tiles['terra']],  # fase 1
            [None, self.tiles['chão caverna']],  # fase 2
            [None],  # fase 3
            [None],  # fase 4
            [None],  # fase 5
        ]
        self.blocos_solidos = [
            [1, 2],  # fase 1
            [1],  # fase 2
            [],  # fase 3
            [],  # fase 4
            [],  # fase 5

        ]
        self.game = True
    

    def load(self):
        self.posicao += self.velocidade
        self.window.fill((255,255,255))
        # segundo plano
        self.window.blit(self.plano2[self.fase], (self.posicao * 0.1, 0))
        # primeiro plano
        for y, linha in enumerate(self.plano1[self.fase]):
            for x, block_address in enumerate(linha):
                block = self.block_address_index[self.fase][block_address]
                if block_address != 0:
                    self.window.blit(block, (x*50 + self.posicao, y*50))
    

    def game_over(self):
        # implemantar música de game over
        time.sleep(5)
        # fazer tela de game over
        self.game = False
    

    def tela_inicio(self):
        # fazer tela de início com instrucões básicas de jogo
        self.window.fill((0, 0, 0))
        pygame.font.init()
        fonte = pygame.font.Font('Fonte.ttf', 32)

        linha1 = fonte.render('Bem vindo ao jogo HEXBLADE!', 1, (255,255,255))
        self.window.blit(linha1,(50,50))

        linha2 = fonte.render('Use as setas ou WASD para se movimentar', 1, (255,255,255))
        self.window.blit(linha2,(50, 150))

        linha3 = fonte.render('Aperte Q para atacar', 1, (255,255,255))
        self.window.blit(linha3,(50, 250))
        
        ultima_linha = fonte.render('Pressione ENTER para começar...', 1, (255,255,255))
        self.window.blit(ultima_linha,(50,600))

        pygame.display.update()
        
        # aperte enter para começar
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return


class Personagem():
    def __init__(self, window):
        self.window = window
        self.altura = 100
        self.largura = 50
        self.personagem = pygame.transform.scale(pygame.image.load('personagem_temporario.png'), (self.largura, self.altura))
        self.posicao_y = 500
        self.posicao_x = 200
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.esquerda = False
        self.direita = False
        self.pulando = False
    

    def load(self):
        self.posicao_x += self.velocidade_x
        self.posicao_y += self.velocidade_y
        self.window.blit(self.personagem, (self.posicao_x, self.posicao_y))