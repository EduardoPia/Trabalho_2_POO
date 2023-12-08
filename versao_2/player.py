import pygame as pg

from game_object import GameObject
from config_jogo import ConfigJogo
from vetor2d import Vetor2D
from utils import ler_imagem
from cronometro import Cronometro
from bomba import Bomba

class Player(GameObject):
    def __init__(self,position:Vetor2D, player:int):
        super().__init__(position)
        self.player = player
        self.img = ler_imagem(ConfigJogo.PLAYER_IMGS[player],ConfigJogo.PLAYER_SIZE.as_tuple())
        self.cronometro_recarga = Cronometro() # conta recarga da bomba
        self.bombas_postas = 0
        self.orientation = Vetor2D(ConfigJogo.STOPPED,ConfigJogo.STOPPED)
        self.pos = Vetor2D(self.position.x,self.position.y)
        self.botar_bomba = False

    def tratamento(self):
        self.orientation.x = ConfigJogo.STOPPED
        self.orientation.y = ConfigJogo.STOPPED
        if pg.key.get_pressed()[ConfigJogo.CONTROLS[self.player][0]]:
            self.orientation.y += ConfigJogo.UP
        if pg.key.get_pressed()[ConfigJogo.CONTROLS[self.player][1]]:
            self.orientation.y  += ConfigJogo.DOWN
        if pg.key.get_pressed()[ConfigJogo.CONTROLS[self.player][2]]:
            self.orientation.x  += ConfigJogo.LEFT
        if pg.key.get_pressed()[ConfigJogo.CONTROLS[self.player][3]]:
            self.orientation.x += ConfigJogo.RIGHT
        if pg.key.get_pressed()[ConfigJogo.CONTROLS[self.player][4]]:
            self.botar_bomba = True
                
    def atualizar(self, lista: list):
        
        ## Conta o número de bombas postas por esse player
        self.bombas_postas = 0
        for object in lista:
            if type(object) == Bomba:
                if object.player == self.player:
                    self.bombas_postas += 1 
        
        ## Checa se a bomba deve ser colocada e a coloca, se possível
        if self.botar_bomba and (self.bombas_postas<ConfigJogo.BOMBAS_PLAYER) and (self.cronometro_recarga.tempo_passado() > ConfigJogo.TEMPO_BOMBA_RECARGA):
            self.cronometro_recarga.reset()
            self.botar_bomba = False
            center_player = self.position + Vetor2D(0.5*ConfigJogo.PLAYER_SIZE.x,0.5*ConfigJogo.PLAYER_SIZE.y)
            pos_grid = Vetor2D((center_player.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,(center_player.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)
            pos = Vetor2D(pos_grid.x*ConfigJogo.TILE_SIZE.x+ConfigJogo.ARENA_TOP_LEFT.x,pos_grid.y*ConfigJogo.TILE_SIZE.y+ConfigJogo.ARENA_TOP_LEFT.y)
            lista.append(Bomba(pos,"sprites/items/bomba.png",1))    
            
        