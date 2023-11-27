
from typing import Tuple, List
import pygame as pg

from config_jogo import ConfigJogo
from vetor2d import Vetor2D
from utils import ler_imagem, dist
from bomb import Bomb
from cronometro import Cronometro

class Player:
    def __init__(self, position: Vetor2D, img_path:str):
        self.position = position
        self.img = ler_imagem(img_path,ConfigJogo.PLAYER_SIZE.as_tuple())
        self.cronometro_recarga = Cronometro() # conta recarga da bomba
        self.cronometro_explosao = Cronometro()
        self.tempo_bombas = []
        self.bombas_postas = 0
        self.orientation = Vetor2D(ConfigJogo.STOPPED,ConfigJogo.STOPPED)

    def bota_bomba(self):
        self.cronometro_recarga.reset()
        self.bombas_postas += 1
        self.tempo_bombas.append(self.cronometro_explosao.tempo_passado())
        
    def atualizar(self, blocos:List[List[int]],bombas:List[Bomb]):
        pos_x = self.position.x
        pos_y = self.position.y

        if self.orientation.y == ConfigJogo.UP:
            pos_y += -ConfigJogo.PLAYER_VEL
        if self.orientation.y == ConfigJogo.DOWN:
            pos_y += ConfigJogo.PLAYER_VEL
        if self.orientation.x == ConfigJogo.LEFT:
            pos_x += -ConfigJogo.PLAYER_VEL
        if self.orientation.x == ConfigJogo.RIGHT:
            pos_x += ConfigJogo.PLAYER_VEL
        
        old_top_left_i_j = Vetor2D(1.0005*(self.position.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,\
                               1.0005*(self.position.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)
        
        new_top_left_i_j = Vetor2D(1.0005*(pos_x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,\
                               1.0005*(pos_y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)
        new_bottom_right_i_j = Vetor2D(1.0005*(pos_x-ConfigJogo.ARENA_TOP_LEFT.x+ConfigJogo.PLAYER_SIZE.x)//ConfigJogo.TILE_SIZE.x+1,\
                               1.0005*(pos_y-ConfigJogo.ARENA_TOP_LEFT.y+ConfigJogo.PLAYER_SIZE.y)//ConfigJogo.TILE_SIZE.y+1)   

        new_top_left = Vetor2D(ConfigJogo.TILE_SIZE.x*new_top_left_i_j.x+ConfigJogo.ARENA_TOP_LEFT.x,\
                               ConfigJogo.TILE_SIZE.y*new_top_left_i_j.y+ConfigJogo.ARENA_TOP_LEFT.y)

        
        for i in range(2):
            for j in range(2):
                if blocos[i+int(new_top_left_i_j.x)][j+int(new_top_left_i_j.y)] != ConfigJogo.EMPTY:
                    min_x = new_top_left.x + i*ConfigJogo.TILE_SIZE.x-ConfigJogo.PLAYER_SIZE.x
                    max_x = new_top_left.x + i*ConfigJogo.TILE_SIZE.x+ConfigJogo.PLAYER_SIZE.x
                    min_y = new_top_left.y + j*ConfigJogo.TILE_SIZE.y-ConfigJogo.PLAYER_SIZE.y
                    max_y = new_top_left.y + j*ConfigJogo.TILE_SIZE.y+ConfigJogo.PLAYER_SIZE.y
                    if (pos_x > min_x) and \
                        (pos_x < max_x) and \
                        (self.position.y > min_y) and \
                        (self.position.y < max_y):
                        pos_x = self.position.x
                    
                    if (self.position.x > min_x) and \
                        (self.position.x < max_x) and \
                        (pos_y > min_y) and \
                        (pos_y < max_y):
                        pos_y = self.position.y
                        
                    if (pos_x > min_x) and \
                        (pos_x < max_x) and \
                        (pos_y > min_y) and \
                        (pos_y < max_y):
                        pos_y = self.position.y
                        pos_x = self.position.x
                    
        for bomba in bombas:
            if ((bomba.position.x-ConfigJogo.PLAYER_SIZE.x) < pos_x) and \
                ((bomba.position.x+ConfigJogo.TILE_SIZE.x) > pos_x) and \
                ((bomba.position.y-ConfigJogo.PLAYER_SIZE.y) < self.position.y) and \
                ((bomba.position.y+ConfigJogo.TILE_SIZE.y) > self.position.y):
                if dist(Vetor2D(pos_x,pos_y),bomba.position) < dist(self.position,bomba.position):
                    pos_x = self.position.x
                
            if ((bomba.position.x-ConfigJogo.PLAYER_SIZE.x) < self.position.x) and \
                ((bomba.position.x+ConfigJogo.TILE_SIZE.x) > self.position.x) and \
                ((bomba.position.y-ConfigJogo.PLAYER_SIZE.y) < pos_y) and \
                ((bomba.position.y+ConfigJogo.TILE_SIZE.y) > pos_y):
                if dist(Vetor2D(pos_x,pos_y),bomba.position) < dist(self.position,bomba.position):
                    pos_x = self.position.x
            
            if ((bomba.position.x-ConfigJogo.PLAYER_SIZE.x) < pos_x) and \
                ((bomba.position.x+ConfigJogo.TILE_SIZE.x) > pos_x) and \
                ((bomba.position.y-ConfigJogo.PLAYER_SIZE.y) < pos_y) and \
                ((bomba.position.y+ConfigJogo.TILE_SIZE.y) > pos_y):
                if dist(Vetor2D(pos_x,pos_y),bomba.position) < dist(self.position,bomba.position):
                    pos_y = self.position.y
                    pos_x = self.position.x
                
                
                
                
        # for bomba in bombas:
        #     if bomba.position == Vetor2D(i*ConfigJogo.TILE_SIZE.x+ConfigJogo.ARENA_TOP_LEFT.x,j*ConfigJogo.TILE_SIZE.y+ConfigJogo.ARENA_TOP_LEFT.y):
        #         pos_x = self.position.x
        #         pos_y = self.position.y
            
        #     if (bomba.position.x == new_top_left.x) and (bomba.position.y == new_top_left.y):
        #         pos_x = self.position.x
        #         pos_y = self.position.y
           
        self.position = Vetor2D(pos_x,pos_y) 
                
        for tempo in self.tempo_bombas:
            if (self.cronometro_explosao.tempo_passado() - tempo) > ConfigJogo.TEMPO_BOMBA_EXPLOSAO:
                self.tempo_bombas.remove(tempo)
                self.bombas_postas -= 1
                    

    def desenha(self, tela):
        tela.blit(self.img,self.position.as_tuple())
