import pygame as pg
from typing import List

from game_object import GameObject
from config_jogo import ConfigJogo
from vetor2d import Vetor2D
from utils import ler_imagem,resultado_colisao, testa_colisao, dist
from cronometro import Cronometro
from bomba import Bomba
from mapa import Mapa
from projetil import Projetil

class Player(GameObject):
    def __init__(self,position:Vetor2D, player:int):
        super().__init__(position,ConfigJogo.PLAYER_SIZE, True, True)
        self.player:int = player # Qual o player
        self.img:pg.Surface = ler_imagem(ConfigJogo.PLAYER_IMGS[player],self.size.as_tuple()) # Img player
        self.cronometro_recarga:Cronometro = Cronometro() # Conta recarga da bomba
        self.bombas_postas:int = 0 # Numero de bombas postas
        self.orientation:Vetor2D = Vetor2D(ConfigJogo.STOPPED,ConfigJogo.STOPPED) # orientação
        self.pos:Vetor2D = Vetor2D(self.position.x,self.position.y) # Posição depois de andar
        self.botar_bomba:bool = False # Indica que foi requisitado botar uma bomba
        self.tempo:int = 1 # Velocidade de passagem do tempo (afetada pelo fantasma)

    def tratamento(self):
        ## Reseta orientação e botar_bomba, depois detecta se houve algum comando do player
        self.orientation.x = ConfigJogo.STOPPED
        self.orientation.y = ConfigJogo.STOPPED
        self.botar_bomba = False
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
                
    def atualizar(self, lista: List[GameObject], mapa:Mapa):
        
        ## Conta o número de bombas postas por esse player e morte por projetil
        self.bombas_postas = 0
        for object in lista:
            if type(object) == Bomba:
                if object.player == self.player:
                    self.bombas_postas += 1 
            elif type(object) == Projetil:
                if testa_colisao(object.position,object.size,self.position,self.size):
                    self.remover[0] = True
        
        ## Checa se a bomba deve ser colocada e a coloca, se possível
        if self.botar_bomba and (self.bombas_postas<ConfigJogo.BOMBAS_PLAYER) and (self.cronometro_recarga.tempo_passado() > ConfigJogo.TEMPO_BOMBA_RECARGA):
            self.cronometro_recarga.reset()
            self.botar_bomba = False
            center_player = self.position + Vetor2D(0.5*ConfigJogo.PLAYER_SIZE.x,0.5*ConfigJogo.PLAYER_SIZE.y)
            pos_grid = Vetor2D((center_player.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,(center_player.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)
            pos = Vetor2D(pos_grid.x*ConfigJogo.TILE_SIZE.x+ConfigJogo.ARENA_TOP_LEFT.x,pos_grid.y*ConfigJogo.TILE_SIZE.y+ConfigJogo.ARENA_TOP_LEFT.y)
            botar = True
            for object in lista:
                if (type(object) == Bomba) and (object.position == pos):
                    botar = False
            if botar:        
                lista.append(Bomba(pos,ConfigJogo.TILE_SIZE,self.player))    
           
        ## Faz o movimento 
        self.pos.x = self.position.x
        self.pos.y = self.position.y

        if self.orientation.y == ConfigJogo.UP:
            self.pos.y += -ConfigJogo.PLAYER_VEL*self.tempo
        if self.orientation.y == ConfigJogo.DOWN:
            self.pos.y += ConfigJogo.PLAYER_VEL*self.tempo
        if self.orientation.x == ConfigJogo.LEFT:
            self.pos.x += -ConfigJogo.PLAYER_VEL*self.tempo
        if self.orientation.x == ConfigJogo.RIGHT:
            self.pos.x += ConfigJogo.PLAYER_VEL*self.tempo
        
        ## Testa colisão com o mapa
        new_top_left_i_j = Vetor2D((0.0005*ConfigJogo.TILE_SIZE.x + self.pos.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,\
                                (0.0005*ConfigJogo.TILE_SIZE.y + self.pos.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)  

        new_top_left = Vetor2D(ConfigJogo.TILE_SIZE.x*new_top_left_i_j.x+ConfigJogo.ARENA_TOP_LEFT.x,\
                                ConfigJogo.TILE_SIZE.y*new_top_left_i_j.y+ConfigJogo.ARENA_TOP_LEFT.y)
            
        for i in range(2):
            for j in range(2):
                if mapa.blocos[i+int(new_top_left_i_j.x)][j+int(new_top_left_i_j.y)] != ConfigJogo.EMPTY:
                    self.pos = resultado_colisao(self.position,self.size,self.pos,\
                        Vetor2D(new_top_left.x + i*ConfigJogo.TILE_SIZE.x,new_top_left.y + j*ConfigJogo.TILE_SIZE.y),ConfigJogo.TILE_SIZE)
    
        ## Testa colisão com outros objetos
        for object in lista:
            if object.collision:
                if type(object) == Bomba:
                    if testa_colisao(self.pos,self.size,object.position,object.size):
                        if dist(self.pos,object.position) < dist(self.position,object.position):
                            if dist(self.pos,object.position) > ConfigJogo.TOLERANCIA_BOMBA:
                                self.pos.x = self.position.x
                                self.pos.y = self.position.y        
                  
        self.position.x = self.pos.x
        self.position.y = self.pos.y
        
            
    def desenhar(self, tela:pg.Surface):
        tela.blit(self.img,self.position.as_tuple())