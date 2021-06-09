import pygame
import random


class Background():
    def __init__(self, window):
        self.window = window
        self.fase = 0
        self.posicao = 0
        self.velocidade = 0
        self.tiles = {
            'grama': pygame.transform.scale(pygame.image.load('tiles/grama.png'), (50, 50)),
            'terra': pygame.transform.scale(pygame.image.load('tiles/terra.png'), (50, 50)),
            'chão caverna': pygame.transform.scale(pygame.image.load('tiles/chao_caverna.png'), (50, 50)),
            'montanha': pygame.transform.scale(pygame.image.load('tiles/montanha_nuvens.png'), (2400, 700)),
            'caverna': pygame.transform.scale(pygame.image.load('tiles/fundo_caverna.png'), (2400, 700))
        }
        self.plano1 = [
            [
            # fase 1
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 0
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 50
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 100
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 150
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 200
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 250
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 300
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 350
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 400
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 450
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # y = 500
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 550
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 600
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # y = 650
            ],[
                # fase 2
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # y = 0
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # y = 50
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # y = 100
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # y = 150
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],  # y = 200
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],  # y = 250
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],  # y = 300
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # y = 350
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],  # y = 400
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],  # y = 450
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # y = 500
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # y = 550
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 600
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],  # y = 650
            ],[
                # fase 3
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # y = 0
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 50
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 100
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 150
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 200
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 250
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 300
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 350
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 400
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 450
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 500
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 550
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # y = 600
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # y = 650
            ],
        ]
        self.plano2 = [self.tiles['montanha'], self.tiles['caverna'], self.tiles['caverna']]
        self.block_address_index = [
            [None, self.tiles['grama'], self.tiles['terra']],  # fase 1
            [None, self.tiles['chão caverna']],  # fase 2
            [None, self.tiles['chão caverna']],  # fase 3
        ]
        self.blocos_solidos = [
            [1, 2],  # fase 1
            [1],  # fase 2
            [1],  # fase 3


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
        # fazer tela de game over
        self.window.fill((0, 0, 0))
        pygame.font.init()
        fonte = pygame.font.Font('Fonte.ttf', 128)
        linha1 = fonte.render('GAME OVER', 1, (200, 0, 0))
        self.window.blit(linha1, (400, 100))

        fonte = pygame.font.Font('Fonte.ttf', 64)
        penultima_linha = fonte.render('PRESSIONE S PARA SAIR', 1, (255,255,255))
        self.window.blit(penultima_linha, (50, 500))
        ultima_linha = fonte.render('PRESSIONE ENTER PARA RECOMEÇAR...', 1, (255,255,255))
        self.window.blit(ultima_linha, (50, 600))

        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
                    if event.key == pygame.K_s:
                        self.game = False
                        return
    

    def tela_inicio(self):
        # fazer tela de início com instrucões básicas de jogo
        self.window.fill((0, 0, 0))
        pygame.font.init()

        fonte = pygame.font.Font('Fonte.ttf', 100)
        linha1 = fonte.render('BEM VINDO AO JOGO HEXBLADE!', 1, (200, 0, 0))
        self.window.blit(linha1,(50,50))

        fonte = pygame.font.Font('Fonte.ttf', 64)
        linha2 = fonte.render('USE AS SETAS OU W A S D PARA SE MOVIMENTAR', 1, (255,255,255))
        self.window.blit(linha2, (50, 200))
        linha3 = fonte.render('APERTE ESPAÇO OU Q PARA ATACAR', 1, (255,255,255))
        self.window.blit(linha3, (50, 300))
        ultima_linha = fonte.render('PRESSIONE ENTER PARA COMEÇAR...', 1, (255,255,255))
        self.window.blit(ultima_linha, (50, 600))

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
        self.altura = 106
        self.largura = 30
        self.personagem = {
            'direita': {
                'parado': pygame.transform.scale(pygame.image.load('sprites_player/player_parado.png'), (130, 150)),
                'ataque 2': pygame.transform.scale(pygame.image.load('sprites_player/ataque_end.png'), (130, 150)),
            },
            'esquerda': {
                'parado': pygame.transform.flip(pygame.transform.scale(pygame.image.load('sprites_player/player_parado.png'), (130, 150)), True, False),
                'ataque 2': pygame.transform.flip(pygame.transform.scale(pygame.image.load('sprites_player/ataque_end.png'), (130, 150)), True, False),
            }
        }
        self.posicao_y = 500
        self.posicao_x = 200
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.correcao_flip = 0
        self.direcao = 'direita'
        self.esquerda = False
        self.direita = False
        self.pulando = False
        self.atacando = False
        self.contador_ataque = 0
        self.vidas = 3
        self.vida = pygame.transform.scale(pygame.image.load('sprites_player/heart.png'), (50, 50))
        # self.som_espada = pygame.mixer.Sound('sons/espada_puxando.mp3')
    

    def load(self):
        if self.velocidade_x > 0:
            self.direcao = 'direita'
            self.correcao_flip = 0
        if self.velocidade_x < 0:
            self.direcao = 'esquerda'
            self.correcao_flip = - 60
        self.posicao_x += self.velocidade_x
        self.posicao_y += self.velocidade_y
        if self.atacando:
            # if self.contador_ataque == 0:
            #     self.som_espada.play()
            if self.contador_ataque == 18:
                self.atacando = False
                self.contador_ataque = 0
            self.contador_ataque += 1
        if self.atacando and self.contador_ataque < 12:
            self.window.blit(self.personagem[self.direcao]['ataque 2'], (self.posicao_x, self.posicao_y))
        else:
            self.window.blit(self.personagem[self.direcao]['parado'], (self.posicao_x, self.posicao_y))
    

    def load_vidas(self):
        for i in range(self.vidas):
            self.window.blit(self.vida, (50 + i * 75, 50))


class Inimigos():
    def __init__(self, window):
        self.window = window
        self.inimigos_iniciais = [
            [
                # inimigos fase 1
                (15*50, 10*50),
                (26*50, 6*50),
                (50*50, 9*50),
                (68*50, 10*50),
                (71*50, 6*50),
                (89*50, 11*50),
                (92*50, 8*50),
                (99*50, 11*50) 
            ], [
                (26*50, 6*50),
                (19*50, 9*50),
                (57*50, 7*50),
                (66*50, 7*50),
            ], [
                # inimigos fase 3
                # (10*5, 6*50)
            ]
        ]
        self.inimigos = self.inimigos_iniciais[0].copy()
        self.sprites1 = [
            pygame.transform.scale(pygame.image.load('sprites_inimigos/inimigo_arco_0.png'), (50, 100)),
            pygame.transform.scale(pygame.image.load('sprites_inimigos/inimigo_arco_1.png'), (50, 100)),
        ]
        self.sprites2 = [
            pygame.transform.flip(self.sprites1[0], True, False),
            pygame.transform.flip(self.sprites1[1], True, False),
        ]
        self.contador = 0
        self.flechas = list()
    

    def flecha(self, direcao):
        if direcao:
            return pygame.transform.scale(pygame.image.load('projeteis/flecha_inimigo.png'), (72, 10))
        return pygame.transform.flip(pygame.transform.scale(pygame.image.load('projeteis/flecha_inimigo.png'), (72, 10)), True, False)


    def load(self, background, personagem):
        # load inimigos
        for x, y in self.inimigos:
            if x + background > personagem:
                sprite = self.sprites2
            else:
                sprite = self.sprites1
            if self.contador < 5:
                self.window.blit(sprite[0], (x + background, y))
            else:
                self.window.blit(sprite[1], (x + background, y))
        # load flechas
        flechas = list()
        for flecha in self.flechas:
            flecha_atualizada = dict()
            flecha_atualizada['x'] = flecha['x'] - (int(flecha['direcao']) * 2 - 1) * 8
            flecha_atualizada['y'] = flecha['y']
            flecha_atualizada['direcao'] = flecha['direcao']
            flechas.append(flecha_atualizada)
        self.flechas = flechas
        for flecha in self.flechas:
            self.window.blit(self.flecha(flecha['direcao']), (flecha['x'] + background, flecha['y']))
        # remove flechas fora da tela
        flechas_para_remover = []
        for flecha in self.flechas:
            if not (- 72 < flecha['x'] + background < 1200):
                flechas_para_remover.append(flecha)
        for flecha in flechas_para_remover:
            self.flechas.remove(flecha)

        self.contador += 0.125
        if self.contador == 10:
            self.contador = 0
            # nova flecha
            for x, y in self.inimigos:
                self.flechas.append(
                    {
                        'direcao': x + background > personagem,
                        'x': x - 36 if x + background > personagem else x + 14,
                        'y': y + 22
                    }
                )


class Magos():
    def __init__(self, window):
        self.window = window
        self.magos_iniciais = [
            [
                # magos fase 1

            ], [
                # magos fase 2
                (15*50, 10*50),
                (18*50, 3*50),
                (71*50, 6*50),
                (87*50, 12*50),
                (89*50, 8*50),
                (92*50, 12*50),
                (92*50, 8*50)
            ], [
                # inimigos fase 3

            ]
        ]
        self.magos = self.magos_iniciais[0].copy()
        self.sprites1 = [
            pygame.transform.scale(pygame.image.load('sprites_inimigos/inimigo_mago_1.png'), (50, 100)),
            pygame.transform.scale(pygame.image.load('sprites_inimigos/inimigo_mago_0.png'), (50, 100)),
        ]
        self.sprites2 = [
            pygame.transform.flip(self.sprites1[0], True, False),
            pygame.transform.flip(self.sprites1[1], True, False),
        ]
        self.contador = 0
        self.magias = list()
    

    def magia(self, direcao):
        if direcao:
            if int(self.contador/10) % 2 == 0:
                return pygame.transform.scale(pygame.image.load('projeteis/magia1.png'), (46, 20))
            else:
                return pygame.transform.scale(pygame.image.load('projeteis/magia2.png'), (46, 20))
        if int(self.contador/10) % 2 == 0:
            return pygame.transform.flip(pygame.transform.scale(pygame.image.load('projeteis/magia1.png'), (46, 20)), True, False)
        else:
            return pygame.transform.flip(pygame.transform.scale(pygame.image.load('projeteis/magia2.png'), (46, 20)), True, False)


    def load(self, background, personagem):
        # load magos
        for x, y in self.magos:
            if x + background > personagem:
                sprite = self.sprites2
            else:
                sprite = self.sprites1
            if self.contador < 40:
                self.window.blit(sprite[0], (x + background, y))
            else:
                self.window.blit(sprite[1], (x + background, y))
        # load magias
        magias = list()
        for magia in self.magias:
            magia_atualizada = dict()
            magia_atualizada['x'] = magia['x'] - (int(magia['direcao']) * 2 - 1) * 8
            magia_atualizada['y'] = magia['y']
            magia_atualizada['direcao'] = magia['direcao']
            magias.append(magia_atualizada)
        self.magias = magias
        for magia in self.magias:
            self.window.blit(self.magia(magia['direcao']), (magia['x'] + background, magia['y']))
        # remove magias fora da tela
        magias_para_remover = []
        for magia in self.magias:
            if not (- 46 < magia['x'] + background < 1200):
                magias_para_remover.append(magia)
        for magia in magias_para_remover:
            self.magias.remove(magia)

        self.contador += 1
        if self.contador == 80:
            self.contador = 0
            # nova magia
            for x, y in self.magos:
                self.magias.append(
                    {
                        'direcao': x + background > personagem,
                        'x': x - 10 if x + background > personagem else x + 40,
                        'y': y + 30
                    }
                )


class Boss():
    def __init__(self, window):
        self.window = window
        self.ataque = ''
        self.atacando = False
        self.contador = 0
        self.largura = 40
        self.altura = 140
        self.posicao_x = 1200
        self.posicao_y = 450
        self.posicao_x_teleporte = 0
        self.vidas = 7
        self.vida = pygame.transform.scale(pygame.image.load('sprites_player/heart.png'), (50, 50))
        self.projeteis = list()
        self.projeteis2 = list()
        self.magia = pygame.transform.scale(pygame.image.load('sprites_boss_corrigido/magia_do_boss.png'), (60, 34))
        self.magia_fliped = pygame.transform.flip(self.magia, True, False)
        self.flecha = pygame.transform.scale(pygame.image.load('sprites_boss_corrigido/projetil_boss_corrigido.png'), (30, 21))
        self.flecha_fliped = pygame.transform.flip(self.flecha, True, False)
        self.sprites = {
            'boss parado': pygame.transform.scale(pygame.image.load('sprites_boss_corrigido/boss_parado_corrigido.png'), (400, 200)),
            'boss magia 1': pygame.transform.scale(pygame.image.load('sprites_boss_corrigido/boss_magia_corrigido.png'), (400, 200)),
            'boss magia 2': pygame.transform.scale(pygame.image.load('sprites_boss_corrigido/boss_castando_magia.png'), (400, 200)),
            'boss telegraph': pygame.transform.scale(pygame.image.load('sprites_boss_corrigido/boss_telegraph_corrigido.png'), (400, 200)),
            'boss ataque': pygame.transform.scale(pygame.image.load('sprites_boss_corrigido/boss_atacando_corrigido.png'), (400, 200)),
            'teleporte 1': pygame.transform.scale(pygame.image.load('sprites_boss_corrigido/boss_tp_iniciando_corrigido.png'), (400, 200)),
            'teleporte 2': pygame.transform.scale(pygame.image.load('sprites_boss_corrigido/tp_1_corrigido.png'), (400, 200)),
            'teleporte 3': pygame.transform.scale(pygame.image.load('sprites_boss_corrigido/tp_2_corrigido.png'), (400, 200)),
        }
        self.sprites_fliped = {
            'boss parado': pygame.transform.flip(self.sprites['boss parado'], True, False),
            'boss magia 1': pygame.transform.flip(self.sprites['boss magia 1'], True, False),
            'boss magia 2': pygame.transform.flip(self.sprites['boss magia 2'], True, False),
            'boss telegraph': pygame.transform.flip(self.sprites['boss telegraph'], True, False),
            'boss ataque': pygame.transform.flip(self.sprites['boss ataque'], True, False),
            'teleporte 1': pygame.transform.flip(self.sprites['teleporte 1'], True, False),
            'teleporte 2': pygame.transform.flip(self.sprites['teleporte 2'], True, False),
            'teleporte 3': pygame.transform.flip(self.sprites['teleporte 3'], True, False),
        }
    


    def load_vidas(self, fase):
        if fase == 2:
            for i in range(0, -self.vidas, -1):
                self.window.blit(self.vida, (1100 + i * 75, 50))
    
    
    def get_sprite(self, sprite, posicao_personagem, posicao_background, posicao):
        if posicao + 150 + posicao_background > posicao_personagem:
            return self.sprites_fliped[sprite]
        else:
            return self.sprites[sprite]


    def lancar_projetil(self, background, personagem, x, y):
        self.projeteis.append(
            {
                'direcao': x + background > personagem,
                'x': x + 100 if x + background > personagem else x + 240,
                'y': y + 70,
            }
        )
    

    def get_projetil_sprite(self, direcao):
        if direcao:
            return self.magia_fliped
        return self.magia


    def load_projeteis(self, background):
        projeteis = list()
        for projetil in self.projeteis:
            projetil_atualizado = dict()
            projetil_atualizado['x'] = projetil['x'] - (int(projetil['direcao']) * 2 - 1) * 8
            projetil_atualizado['y'] = projetil['y']
            projetil_atualizado['direcao'] = projetil['direcao']
            projeteis.append(projetil_atualizado)
        self.projeteis = projeteis
        for projetil in self.projeteis:
            self.window.blit(self.get_projetil_sprite(projetil['direcao']), (projetil['x'] + background, projetil['y']))
    

    def lancar_projetil2(self, background, personagem, x, y):
        self.projeteis2.append(
            {
                'direcao': x + background > personagem,
                'x': x if x + background > personagem else x + 350,
                'y': y + 75,
            }
        )
    

    def get_projetil_sprite2(self, direcao):
        if direcao:
            return self.flecha_fliped
        return self.flecha


    def load_projeteis2(self, background):
        projeteis = list()
        for projetil in self.projeteis2:
            projetil_atualizado = dict()
            projetil_atualizado['x'] = projetil['x'] - (int(projetil['direcao']) * 2 - 1) * 8
            projetil_atualizado['y'] = projetil['y']
            projetil_atualizado['direcao'] = projetil['direcao']
            projeteis.append(projetil_atualizado)
        self.projeteis2 = projeteis
        for projetil in self.projeteis2:
            self.window.blit(self.get_projetil_sprite2(projetil['direcao']), (projetil['x'] + background, projetil['y']))
        

    def load(self, fase, posicao_personagem, posicao_background):
        if fase == 2:
            if not self.atacando:
                self.window.blit(self.get_sprite('boss parado', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                self.ataque = ['teleporte', 'magia', 'espadada'][random.randint(0, 2)]
                self.atacando = True
                if self.ataque == 'teleporte':
                    self.posicao_x_teleporte = self.posicao_x
                    self.posicao_x = [a for a in [400, 800, 1200] if a != self.posicao_x][random.randint(0, 1)]
            else:
                if self.ataque == 'espadada':
                    if self.contador < 90:
                        self.window.blit(self.get_sprite('boss parado', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                    elif self.contador < 110:
                        self.window.blit(self.get_sprite('boss telegraph', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                    elif self.contador < 140:
                        if self.contador == 110:
                            self.lancar_projetil2(posicao_background, posicao_personagem, self.posicao_x, self.posicao_y)
                        self.window.blit(self.get_sprite('boss ataque', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                    else:
                        self.contador = 0
                        self.atacando = False
                    self.contador += 1
                elif self.ataque == 'magia':
                    if self.contador < 90:
                        self.window.blit(self.get_sprite('boss parado', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                    elif self.contador < 110:
                        self.window.blit(self.get_sprite('boss magia 1', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                    elif self.contador < 150:
                        if self.contador == 110:
                            self.lancar_projetil(posicao_background, posicao_personagem, self.posicao_x, self.posicao_y)
                        self.window.blit(self.get_sprite('boss magia 2', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                    else:
                        self.contador = 0
                        self.atacando = False
                    self.contador += 1
                elif self.ataque == 'teleporte':
                    if self.contador < 90:
                        self.window.blit(self.get_sprite('boss parado', posicao_personagem, posicao_background, self.posicao_x_teleporte), (self.posicao_x_teleporte + posicao_background, self.posicao_y))
                    elif self.contador < 110:
                        self.window.blit(self.get_sprite('teleporte 1', posicao_personagem, posicao_background, self.posicao_x_teleporte), (self.posicao_x_teleporte + posicao_background, self.posicao_y))
                        self.window.blit(self.get_sprite('teleporte 3', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                    elif self.contador < 150:
                        self.window.blit(self.get_sprite('teleporte 2', posicao_personagem, posicao_background, self.posicao_x_teleporte), (self.posicao_x_teleporte + posicao_background, self.posicao_y))
                        self.window.blit(self.get_sprite('teleporte 2', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                    elif self.contador < 150:
                        self.window.blit(self.get_sprite('teleporte 3', posicao_personagem, posicao_background, self.posicao_x_teleporte), (self.posicao_x_teleporte + posicao_background, self.posicao_y))
                        self.window.blit(self.get_sprite('teleporte 1', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                    elif self.contador < 190:
                        self.window.blit(self.get_sprite('boss parado', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                    else:
                        self.window.blit(self.get_sprite('boss parado', posicao_personagem, posicao_background, self.posicao_x), (self.posicao_x + posicao_background, self.posicao_y))
                        self.contador = 0
                        self.atacando = False
                    self.contador += 1
            self.load_projeteis(posicao_background)
            self.load_projeteis2(posicao_background)