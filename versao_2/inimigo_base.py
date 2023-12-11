import pygame as pg
import random as rd
from copy import deepcopy
from typing import List

from game_object import GameObject
from mapa import Mapa
from vetor2d import Vetor2D
from config_jogo import ConfigJogo

# Classe genérica de inimigos
class Inimigo_base(GameObject):
    def __init__(self, position: Vetor2D):
        super().__init__(position, Vetor2D(0.98*ConfigJogo.TILE_SIZE.x,0.98*ConfigJogo.TILE_SIZE.y), True, True)
        self.pos:Vetor2D = deepcopy(self.position) # Posição depois de andar
        self.velo:Vetor2D = deepcopy(ConfigJogo.INIM_VEL[rd.choice((0,1,2,3))]) # Velocidade inicial
        
    def tratamento(self):
        pass
    
    def atualizar(self, lista: List[GameObject], mapa: Mapa):
        pass
        
    def desenhar(self, tela: pg.Surface):
        pass