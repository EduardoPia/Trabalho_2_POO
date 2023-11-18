
from typing import Tuple, List
import pygame as pg

from config_jogo import ConfigJogo
from vetor2d import Vetor2D
from utils import ler_imagem

class Player:
    def __init__(self, position: Vetor2D, img_path:str):
        self.position = position
        self.img = ler_imagem(img_path,ConfigJogo.PLAYER_SIZE.as_tuple())

    def atualizar(self, orientation:Vetor2D, blocos:List[List[int]]):
        pos_x = self.position.x
        pos_y = self.position.y
        if orientation.y == ConfigJogo.UP:
            pos_y += -ConfigJogo.PLAYER_VEL
        if orientation.y == ConfigJogo.DOWN:
            pos_y += ConfigJogo.PLAYER_VEL
        if orientation.x == ConfigJogo.LEFT:
            pos_x += -ConfigJogo.PLAYER_VEL
        if orientation.x == ConfigJogo.RIGHT:
            pos_x += ConfigJogo.PLAYER_VEL
        # if (pos_x == self.position.x) and (pos_x == self.position.x):
        #      return

        
        for i in range(len(blocos)):
            for j in range(len(blocos[i])):
                if blocos[i][j] != ConfigJogo.EMPTY:
                    max_x = ConfigJogo.ARENA_TOP_LEFT.x + i*ConfigJogo.TILE_SIZE.x-ConfigJogo.PLAYER_SIZE.x
                    min_x = ConfigJogo.ARENA_TOP_LEFT.x + i*ConfigJogo.TILE_SIZE.x+ConfigJogo.PLAYER_SIZE.x
                    max_y = ConfigJogo.ARENA_TOP_LEFT.y + j*ConfigJogo.TILE_SIZE.y-ConfigJogo.PLAYER_SIZE.y
                    min_y = ConfigJogo.ARENA_TOP_LEFT.y + j*ConfigJogo.TILE_SIZE.y+ConfigJogo.PLAYER_SIZE.y
                    if (pos_x > max_x) and \
                        (pos_x < min_x) and \
                        (self.position.y > max_y) and \
                        (self.position.y < min_y):
                        pos_x = self.position.x
                    
                    if (self.position.x > max_x) and \
                        (self.position.x < min_x) and \
                        (pos_y > max_y) and \
                        (pos_y < min_y):
                        pos_y = self.position.y
                        
                    if (pos_x > max_x) and \
                        (pos_x < min_x) and \
                        (pos_y > max_y) and \
                        (pos_y < min_y):
                        pos_y = self.position.y
                        pos_x = self.position.x
                        
        self.position = Vetor2D(pos_x,pos_y)

    def desenha(self, tela):
        tela.blit(self.img,self.position.as_tuple())
