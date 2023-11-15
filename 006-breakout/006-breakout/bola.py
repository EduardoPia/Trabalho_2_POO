

import pygame as pg

from config_jogo import ConfigJogo
from vetor2d import Vetor2D

class Bola:
    def __init__(self, posicao, raio, cor, velocidade = Vetor2D()):
        self.posicao = posicao
        self.velocidade = velocidade
        self.raio = raio
        self.cor = cor

    def atualizar(self):
        self.posicao += self.velocidade 

    def desenha(self, tela: pg.Surface):
        center = (self.posicao.x, self.posicao.y)
        pg.draw.circle(tela, self.cor,
                       center, ConfigJogo.RAIO_BOLA)
