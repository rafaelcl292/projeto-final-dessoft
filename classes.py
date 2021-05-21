import pygame


class Background():
    def __init__(self, window):
        self.window = window
        self.grama = pygame.transform.scale(pygame.image.load('tiles/grama.png'), (50, 50))
    

    def load(self):
        self.window.fill((69,179,224))
        for x in range(0, 1200, 50):
            self.window.blit(self.grama, (x, 650))


class Personagem():
    def __init__(self, window):
        self.window = window
        self.personagem = pygame.transform.scale(pygame.image.load('personagem_temporario.png'), (50, 100))
    

    def load(self):
        self.window.blit(self.personagem, (200, 550))