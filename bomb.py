import pygame as pg
from typing import List

from config_jogo import ConfigJogo
from vetor2d import Vetor2D
from utils import ler_imagem
from cronometro import Cronometro

class Bomb:
    
    def __init__(self,position:Vetor2D, img_path:str, player:int):
        self.position = position
        self.image = ler_imagem(img_path,ConfigJogo.TILE_SIZE.as_tuple())
        self.cronometro = Cronometro()
        self.player = player
        
    def explodiu(self):
        return (self.cronometro.tempo_passado() > ConfigJogo.TEMPO_BOMBA_EXPLOSAO)         
    
    def desenha(self,tela):
        tela.blit(self.image,self.position.as_tuple())
        