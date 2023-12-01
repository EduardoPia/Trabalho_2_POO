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
    def __init__(self, tela:pg.Surface, players:int):
        self.tela = tela
        self.mapa = Mapa()
        self.players:List[Player] = []
        for i in range(players):
            self.players.append(Player(ConfigJogo.PLAYERS_POS[i],ConfigJogo.PLAYER_IMGS[i]))
        self.cronometro = Cronometro()
        self.cronometro.reset()
        self.encerrado = False
        self.bombas:List[Bomb] = []
        self.chamas:List[Chama] = []
        self.bomb_sound = pg.mixer.Sound('sprites/items/BOMB_SONG.wav')
            
    def tratamento_player2(self):
        self.players[1].orientation.x = ConfigJogo.STOPPED
        self.players[1].orientation.y = ConfigJogo.STOPPED
        if pg.key.get_pressed()[pg.K_UP]:
            self.players[1].orientation.y += ConfigJogo.UP
        if pg.key.get_pressed()[pg.K_DOWN]:
            self.players[1].orientation.y  += ConfigJogo.DOWN
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.players[1].orientation.x  += ConfigJogo.LEFT
        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.players[1].orientation.x += ConfigJogo.RIGHT
        if pg.key.get_pressed()[pg.K_0] or pg.key.get_pressed()[pg.K_KP0]:
            if (self.players[1].bombas_postas<ConfigJogo.BOMBAS_PLAYER1) and (self.players[1].cronometro_recarga.tempo_passado() > ConfigJogo.TEMPO_BOMBA_RECARGA):
                center_player = self.players[1].position + Vetor2D(0.5*ConfigJogo.PLAYER_SIZE.x,0.5*ConfigJogo.PLAYER_SIZE.y)
                pos_grid = Vetor2D((center_player.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,(center_player.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)
                pos = Vetor2D(pos_grid.x*ConfigJogo.TILE_SIZE.x+ConfigJogo.ARENA_TOP_LEFT.x,pos_grid.y*ConfigJogo.TILE_SIZE.y+ConfigJogo.ARENA_TOP_LEFT.y)
                self.players[1].bota_bomba()
                self.bombas.append(Bomb(pos,"sprites/items/bomba.png"))
            
    def tratamento_player1(self):
        self.players[0].orientation.x = ConfigJogo.STOPPED
        self.players[0].orientation.y = ConfigJogo.STOPPED
        if pg.key.get_pressed()[pg.K_w]:
            self.players[0].orientation.y += ConfigJogo.UP
        if pg.key.get_pressed()[pg.K_s]:
            self.players[0].orientation.y  += ConfigJogo.DOWN
        if pg.key.get_pressed()[pg.K_a]:
            self.players[0].orientation.x  += ConfigJogo.LEFT
        if pg.key.get_pressed()[pg.K_d]:
            self.players[0].orientation.x += ConfigJogo.RIGHT
        if pg.key.get_pressed()[pg.K_SPACE]:
            if (self.players[0].bombas_postas<ConfigJogo.BOMBAS_PLAYER1) and (self.players[0].cronometro_recarga.tempo_passado() > ConfigJogo.TEMPO_BOMBA_RECARGA):
                center_player = self.players[0].position + Vetor2D(0.5*ConfigJogo.PLAYER_SIZE.x,0.5*ConfigJogo.PLAYER_SIZE.y)
                pos_grid = Vetor2D((center_player.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,(center_player.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)
                pos = Vetor2D(pos_grid.x*ConfigJogo.TILE_SIZE.x+ConfigJogo.ARENA_TOP_LEFT.x,pos_grid.y*ConfigJogo.TILE_SIZE.y+ConfigJogo.ARENA_TOP_LEFT.y)
                self.players[0].bota_bomba()
                self.bombas.append(Bomb(pos,"sprites/items/bomba.png"))
     
    def destroy_and_flame(self,bomba:Bomb):
        
        pos = Vetor2D(int((bomba.position.x-ConfigJogo.ARENA_TOP_LEFT.x)/ConfigJogo.TILE_SIZE.x+0.0001),int((bomba.position.y-ConfigJogo.ARENA_TOP_LEFT.y)/ConfigJogo.TILE_SIZE.y+0.0001))
        chama_dim = [ConfigJogo.DIST_EXPLOSAO,ConfigJogo.DIST_EXPLOSAO,ConfigJogo.DIST_EXPLOSAO,ConfigJogo.DIST_EXPLOSAO] #left, right, up, down
        
        # left   
        for i in range(1,ConfigJogo.DIST_EXPLOSAO+1):
            
            if self.mapa.blocos[pos.x-i][pos.y] == ConfigJogo.DESTRUCTABLE:
                self.mapa.blocos[pos.x-i][pos.y] = ConfigJogo.EMPTY
                chama_dim[0] = i
                break
            elif self.mapa.blocos[pos.x-i][pos.y] == ConfigJogo.INDESTRUCTABLE:
                chama_dim[0] = i-1
                break
        
        # right
        for i in range(1,ConfigJogo.DIST_EXPLOSAO+1):
            if self.mapa.blocos[pos.x+i][pos.y] == ConfigJogo.DESTRUCTABLE:
                self.mapa.blocos[pos.x+i][pos.y] = ConfigJogo.EMPTY
                chama_dim[1] = i
                break
            elif self.mapa.blocos[pos.x+i][pos.y] == ConfigJogo.INDESTRUCTABLE:
                chama_dim[1] = i-1
                break
            
        # up
        for j in range(1,ConfigJogo.DIST_EXPLOSAO+1):
            if self.mapa.blocos[pos.x][pos.y-j] == ConfigJogo.DESTRUCTABLE:
                self.mapa.blocos[pos.x][pos.y-j] = ConfigJogo.EMPTY
                chama_dim[2] = j
                break
            elif self.mapa.blocos[pos.x][pos.y-j] == ConfigJogo.INDESTRUCTABLE:
                chama_dim[2] = j-1
                break
        
        # down    
        for j in range(1,ConfigJogo.DIST_EXPLOSAO+1):
            if self.mapa.blocos[pos.x][pos.y+j] == ConfigJogo.DESTRUCTABLE:
                self.mapa.blocos[pos.x][pos.y+j] = ConfigJogo.EMPTY
                chama_dim[3] = j
                break
            elif self.mapa.blocos[pos.x][pos.y+j] == ConfigJogo.INDESTRUCTABLE:
                chama_dim[3] = j-1
                break
            
        self.chamas.append(Chama(bomba.position,chama_dim))
     
    def som_bomba(self):
        self.bomb_sound.play()
            
    def tratamento_eventos(self):
        pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
        
        
        self.tratamento_player1()
        if len(self.players) > 1:
            self.tratamento_player2()
            
    def atualiza_estado(self):
        for player in self.players:
            player.atualizar(self.mapa.blocos,self.bombas, self.chamas) 
        
        for bomba in self.bombas:
            if bomba.explodiu(): # remover destrutiveis, criar chama e depois remover bomba
                self.destroy_and_flame(bomba)
                self.bombas.remove(bomba)
                self.som_bomba()
        
        for chama in self.chamas:
            if chama.terminou():
                self.chamas.remove(chama)
    
    def desenha(self):
        self.mapa.desenha(self.tela)
        for chama in self.chamas:
            chama.desenha(self.tela)
        for bomba in self.bombas:
            bomba.desenha(self.tela)
        for player in self.players:
            player.desenha(self.tela)

        pg.display.flip()
            
    def executar(self):
        while not self.encerrado:
            if self.cronometro.tempo_passado() > ConfigJogo.TEMPO_JOGO:
                self.cronometro.reset()
                self.tratamento_eventos()
                self.atualiza_estado()
                self.desenha()