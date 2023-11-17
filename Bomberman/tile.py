from vetor2d import Vetor2D
from utils import ler_imagem
from config_jogo import ConfigJogo
import pygame as pg

class Tile:
    def __init__(self, destructable: bool, img_path:str,position:Vetor2D):
        self.img = ler_imagem(img_path,ConfigJogo.TILE_SIZE.as_tuple())
        self.destructable = destructable
        self.position = position
        
    def desenha(self,tela:pg.surface):
        tela.blit(self.img, self.position.as_tuple())
        
    