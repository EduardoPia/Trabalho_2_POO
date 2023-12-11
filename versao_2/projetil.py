import pygame as pg
import random as rd
from typing import List

from config_jogo import ConfigJogo
from game_object import GameObject
from mapa import Mapa
from vetor2d import Vetor2D
from utils import ler_imagem

class Projetil(GameObject):
    def __init__(self, position: Vetor2D):
        escolha = rd.choice((0,1,2,3)) # Determina direção e sentido do projetil, e por conseguinte forma
        self.velo:Vetor2D = ConfigJogo.VELO_PROJETIL[escolha] # Velocidade
        super().__init__(position, ConfigJogo.SIZE_PROJETIL[escolha], False, False) # Base do projetil
        self.img:pg.Surface = ler_imagem(ConfigJogo.IMG_PROJETIL[escolha],self.size.as_tuple()) # Img projetil
        
    def tratamento(self):
        pass
    
    def atualizar(self, lista: List[GameObject], mapa: Mapa):
        self.position += self.velo
        
        ## Testa se saiu da tela
        if (self.position.x+self.size.x) < 0 or (self.position.x> ConfigJogo.DIM_TELA.x) or \
            (self.position.y+self.size.y) < 0 or (self.position.y>ConfigJogo.DIM_TELA.y):
                self.remover[0] = True
            
                
    def desenhar(self, tela: pg.Surface):
        tela.blit(self.img,self.position.as_tuple())