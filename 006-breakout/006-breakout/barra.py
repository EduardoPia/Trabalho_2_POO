
from typing import Tuple
import pygame as pg

from config_jogo import ConfigJogo
from vetor2d import Vetor2D

class Barra:
    def __init__(self, posicao: Vetor2D, tamanho: Vetor2D, cor, velocidade = Vetor2D()):
        self.posicao = posicao
        self.tamanho = tamanho 
        self.cor = cor
        self.velocidade = velocidade

    def atualizar(self):
        nova_posicao = self.posicao + self.velocidade

        if (nova_posicao.x >= 0) and \
            (nova_posicao.y >= 0) and \
            (nova_posicao.y + self.tamanho.y  <= ConfigJogo.DIM_TELA.y) and \
            (nova_posicao.x + self.tamanho.x  <= ConfigJogo.DIM_TELA.x):
            self.posicao = nova_posicao

    def desenha(self, tela):
        rect = pg.rect.Rect(self.posicao.x, 
                            self.posicao.y, 
                            self.tamanho.x, 
                            self.tamanho.y)
        
        pg.draw.rect(
            tela,
            self.cor,
            rect
        )

    def rect(self) -> Tuple[float, float, float, float]:
        """ retorna os dados da barra como os retangulos sao representados 
            no pygame, i.e., como uma tupla do tipo (px, py, largura, altura).
        """
        return (self.posicao.x, self.posicao.y, self.tamanho.x, self.tamanho.y)
