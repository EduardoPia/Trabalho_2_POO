from utils import ler_imagem
from tile import Tile
import pygame as pg
from config_jogo import ConfigJogo

from typing import List

class Mapa:
    def __init__(self, img_path:str):
        
        self.blocos:List[List[Tile]] = []
        self.fundo = ler_imagem(img_path,ConfigJogo.DIM_TELA.as_tuple())
        
        for i in range(0,ConfigJogo.ARENA_TILES.y):
            self.blocos.append([])
            for j in range(0,ConfigJogo.ARENA_TILES.x):
                if i == 0 or i == (ConfigJogo.ARENA_TILES.y-1):
                    self.blocos[i].append(Tile())

        
        
        
        
    def desenha(self,tela:pg.surface):
        tela.blit(self.fundo,(0,0))
        for linha in self.blocos:
            for bloco in linha:
                bloco.desenha(tela)
