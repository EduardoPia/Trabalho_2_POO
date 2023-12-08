from typing import List
import pygame as pg
import sys

from game_object import GameObject
from config_jogo import ConfigJogo
from cronometro import Cronometro
from player import Player
from mapa import Mapa

class CenaPrincipal:
    def __init__(self,tela:pg.Surface,num_player:int):
        self.objects:List[GameObject] = []
        self.mapa = Mapa()
        self.tela = tela
        self.cronometro = Cronometro()
        self.tempo_jogo = Cronometro()
        
    def tratamento(self):
        pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
            
        for object in self.objects:
            object.tratamento()
            
    def atualizar(self):
        for object in self.objects:
            object.atualizar()
            
    def desenha(self):
        for object in self.objects:
            object.desenhar(self.tela)
        self.mapa.desenhar(self.tela)
        
        pg.display.flip()
            
    def encerrado(self):
        # if self.tempo_jogo.tempo_passado() > ConfigJogo.TEMPO_JOGO:
        #     return True
        # for object in self.objects:
        #     if type(object) == Player:
        #         return False
        # return True
        return False
            
    def executar(self):
        while not self.encerrado():
            if self.cronometro.tempo_passado() > ConfigJogo.TEMPO_JOGO:
                self.cronometro.reset()
                self.tratamento()
                self.atualizar()
                self.desenha()
            
        