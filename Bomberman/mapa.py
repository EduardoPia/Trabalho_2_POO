from utils import ler_imagem
from tile import tile
import pygame as pg
from config_jogo import ConfigJogo

from typing import List

class Mapa:
    def __init__(self, img_path:str):
        
        self.indestrutiveis:List[tile] = []
        self.destrutiveis:List[tile] = []
        self.colunas:List[tile] = []
        self.fundo = ler_imagem(img_path,ConfigJogo.DIM_TELA.as_tuple())
        
        for i in range(0,ConfigJogo.DIM_ARENA_TILES.x):
            for j in range(0,ConfigJogo.DIM_ARENA_TILES.y):
                self.inde
        
    def desenha(self,tela:pg.surface):
        tela.blit(self.fundo,(0,0))
        for bloco in self.indestrutiveis:
            bloco.desenha(tela)
        for bloco in self.destrutiveis:
            bloco.desenha(tela)
        for coluna in self.colunas:
            coluna.desenha(tela)
            
