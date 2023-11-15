import pygame as pg
import sys
from typing import Tuple, List

from config_jogo import ConfigJogo
from mapa import Mapa

class Bomberman:
    
    def __init__(self):
        
        pg.init()
        
        self.tela = pg.display.set_mode((
            ConfigJogo.DIM_TELA.x,
            ConfigJogo.DIM_TELA.y
        ))
        
        # salvamos a fonte para nao precisar criar ela toda hora
        self.font = pg.font.SysFont(None, 48)
        
        self.mapa = Mapa("sprites/map/grama.png")
        
    def executar(self):
        while True:
            self.tratamento_eventos()
            
            if self.encerrada():
                self.atualiza_estado()
            
            self.desenha()
            
    def tratamento_eventos(self):
        pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
        
    def encerrada(self):
        return False
    
    def atualiza_estado(self):
        pass
    
    def desenha(self):
        self.tela.fill((0, 0, 0))
        
        self.mapa.desenha(self.tela)
        
        pg.display.flip()
        
# jogo = Bomberman()
# jogo.executar()