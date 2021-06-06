import pygame


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
            'montanha': pygame.transform.scale(pygame.image.load('tiles/montanha.png'), (2400, 700)),
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
                [1]*100,  # y = 450
                [0]*100,  # y = 500
                [0]*100,  # y = 550
                [0, 1, 0, 0, 0]*20,  # y = 600
                [1]*100,  # y = 650
            ],[
                # fase 2
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
                [1]*100,  # y = 650
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
            [None, self.tiles['grama'], self.tiles['nuvem']],  # fase 1
            [None, self.tiles['pedra']],  # fase 2
            [None],  # fase 3
            [None],  # fase 4
            [None],  # fase 5
        ]
        self.blocos_solidos = [
            [1],  # fase 1
            [],  # fase 2
            [],  # fase 3
            [],  # fase 4
            [],  # fase 5

        ]
    

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


class Personagem():
    def __init__(self, window):
        self.window = window
        self.altura = 100
        self.largura = 50
        self.personagem = pygame.transform.scale(pygame.image.load('personagem_temporario.png'), (self.largura, self.altura))
        self.posicao_y = 550
        self.posicao_x = 200
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.pulando = False
        self.contador_pulo = 25
        self.esquerda = False
        self.direita = False
    

    def load(self):
        self.posicao_x += self.velocidade_x
        self.window.blit(self.personagem, (self.posicao_x, self.posicao_y))