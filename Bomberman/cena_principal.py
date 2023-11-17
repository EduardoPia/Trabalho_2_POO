import pygame as pg
import sys

from mapa import Mapa

class CenaPrincipal:
    def __init__(self, tela):
        self.tela = tela
        self.mapa = Mapa()
            
    def tratamento_eventos(self):
        pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
            
    def atualiza_estado(self):
        pass
    
    def desenha(self):
        self.mapa.desenha(self.tela)
        
        pg.display.flip()
            
    def encerrado(self):
        return False
    
    def executar(self):
        while not self.encerrado():
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()