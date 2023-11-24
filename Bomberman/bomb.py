import pygame as pg
from typing import List

from config_jogo import ConfigJogo
from vetor2d import Vetor2D
from utils import ler_imagem
from cronometro import Cronometro

class Bomb:
    
    def __init__(self,position:Vetor2D, img_path:str):
        self.position = position
        self.image = ler_imagem(img_path,ConfigJogo.TILE_SIZE.as_tuple())
        self.cronometro = Cronometro()
        self.explodiu = False
        
    def atualiza(self):
        if self.cronometro.tempo_passado() > ConfigJogo.TEMPO_BOMBA_EXPLOSAO:
            self.explodiu = True
            
    # def explode(self,blocos:List[List[int]]):
    #     pos = Vetor2D((self.position.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,(self.position.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)
        
    #     # UP, DOWN, LEFT, RIGHT
    #     for i in range(1,ConfigJogo.DIST_EXPLOSAO):
    #         if blocos[pos.x][pos.y+i] == ConfigJogo.DESTRUCTABLE:
                
            
    
    def desenha(self,tela):
        tela.blit(self.image,self.position.as_tuple())
        