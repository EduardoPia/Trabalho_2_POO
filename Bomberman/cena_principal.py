import pygame as pg
import sys
from typing import List

from mapa import Mapa
from player import Player
from config_jogo import ConfigJogo
from cronometro import Cronometro
from vetor2d import Vetor2D
from bomb import Bomb
from chama import Chama

class CenaPrincipal:
    def __init__(self, tela):
        self.tela = tela
        self.mapa = Mapa()
        self.player = Player(ConfigJogo.PLAYER1_POS,"sprites/chars/pacman-black.png")
        self.cronometro = Cronometro()
        self.cronometro.reset()
        self.encerrado = False
        self.orientation = Vetor2D(ConfigJogo.STOPPED,ConfigJogo.STOPPED) 
        self.bombas:List[Bomb] = []
        self.cronometro_bombas1 = Cronometro()
        self.chamas:List[Chama] = []
            
    def tratamento_player1(self):
        if pg.key.get_pressed()[pg.K_w]:
            self.orientation.y += ConfigJogo.UP
        if pg.key.get_pressed()[pg.K_s]:
            self.orientation.y  += ConfigJogo.DOWN
        if pg.key.get_pressed()[pg.K_a]:
            self.orientation.x  += ConfigJogo.LEFT
        if pg.key.get_pressed()[pg.K_d]:
            self.orientation.x += ConfigJogo.RIGHT
        if pg.key.get_pressed()[pg.K_SPACE]:
            if (len(self.bombas)<ConfigJogo.BOMBAS_PLAYER1) and (self.cronometro_bombas1.tempo_passado() > ConfigJogo.TEMPO_BOMBA_RECARGA):
                self.cronometro_bombas1.reset()
                center_player = self.player.position + Vetor2D(0.5*ConfigJogo.PLAYER_SIZE.x,0.5*ConfigJogo.PLAYER_SIZE.y)
                pos_grid = Vetor2D((center_player.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,(center_player.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)
                pos = Vetor2D(pos_grid.x*ConfigJogo.TILE_SIZE.x+ConfigJogo.ARENA_TOP_LEFT.x,pos_grid.y*ConfigJogo.TILE_SIZE.y+ConfigJogo.ARENA_TOP_LEFT.y)
                self.bombas.append(Bomb(pos,"sprites/items/bomba.png"))
            
    def tratamento_eventos(self):
        pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
        
        self.orientation.x = ConfigJogo.STOPPED
        self.orientation.y = ConfigJogo.STOPPED
        
        # Player 1
        self.tratamento_player1()
            
    def atualiza_estado(self):
        self.player.atualizar(self.mapa.blocos, self.orientation,self.bombas)
        
        for bomba in self.bombas:
            if bomba.explodiu:
                #pos = Vetor2D((bomba.position.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,(bomba.position.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)
                # Exploding
                self.bombas.remove(bomba)
            else:
                bomba.atualiza()
            
            
    
    def desenha(self):
        self.mapa.desenha(self.tela)
        for bomba in self.bombas:
            bomba.desenha(self.tela)
        self.player.desenha(self.tela)

        pg.display.flip()
            
    def executar(self):
        while not self.encerrado:
            if self.cronometro.tempo_passado() > ConfigJogo.TEMPO_JOGO:
                self.cronometro.reset()
                self.tratamento_eventos()
                self.atualiza_estado()
                self.desenha()