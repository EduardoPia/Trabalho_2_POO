import pygame as pg
import sys

from mapa import Mapa
from player import Player
from config_jogo import ConfigJogo
from cronometro import Cronometro
from vetor2d import Vetor2D

class CenaPrincipal:
    def __init__(self, tela):
        self.tela = tela
        self.mapa = Mapa()
        self.player = Player(ConfigJogo.PLAYER1_POS,"sprites\chars\pacman-black.png")
        self.player1_ori = Vetor2D(ConfigJogo.STOPPED,ConfigJogo.STOPPED)
        self.cronometro = Cronometro()
        self.cronometro.reset()
            
    def tratamento_eventos(self):
        pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
        
        self.player1_ori = Vetor2D(ConfigJogo.STOPPED,ConfigJogo.STOPPED)    
        if pg.key.get_pressed()[pg.K_w]:
            self.player1_ori.y += ConfigJogo.UP
        if pg.key.get_pressed()[pg.K_s]:
            self.player1_ori.y += ConfigJogo.DOWN
        if pg.key.get_pressed()[pg.K_a]:
            self.player1_ori.x += ConfigJogo.LEFT
        if pg.key.get_pressed()[pg.K_d]:
            self.player1_ori.x += ConfigJogo.RIGHT
            
    def atualiza_estado(self):
        self.player.atualizar(self.player1_ori, self.mapa.blocos)
    
    def desenha(self):
        self.mapa.desenha(self.tela)
        self.player.desenha(self.tela)
        
        pg.display.flip()
            
    def encerrado(self):
        return False
    
    def executar(self):
        while not self.encerrado():
            if self.cronometro.tempo_passado() > ConfigJogo.TEMPO_JOGO:
                self.cronometro.reset()
                self.tratamento_eventos()
                self.atualiza_estado()
                self.desenha()