
from typing import Tuple, List
import pygame as pg

from config_jogo import ConfigJogo
from vetor2d import Vetor2D
from utils import ler_imagem

class Player:
    def __init__(self, position: Vetor2D, img_path:str):
        self.position = position
        self.img = ler_imagem(img_path,ConfigJogo.PLAYER_SIZE.as_tuple())

    def atualizar(self, blocos:List[List[int]], orientacao:Vetor2D):
        pos_x = self.position.x
        pos_y = self.position.y

        if orientacao.y == ConfigJogo.UP:
            pos_y += -ConfigJogo.PLAYER_VEL
        if orientacao.y == ConfigJogo.DOWN:
            pos_y += ConfigJogo.PLAYER_VEL
        if orientacao.x == ConfigJogo.LEFT:
            pos_x += -ConfigJogo.PLAYER_VEL
        if orientacao.x == ConfigJogo.RIGHT:
            pos_x += ConfigJogo.PLAYER_VEL
        # if (pos_x == self.position.x) and (pos_x == self.position.x):
        #      return

        
        new_top_left_i_j = Vetor2D((pos_x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,\
                               (pos_y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)
        # old_top_left_i_j = Vetor2D((self.position.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,\
        #                        (self.position.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)

        new_top_left = Vetor2D(ConfigJogo.TILE_SIZE.x*new_top_left_i_j.x+ConfigJogo.ARENA_TOP_LEFT.x,\
                               ConfigJogo.TILE_SIZE.y*new_top_left_i_j.y+ConfigJogo.ARENA_TOP_LEFT.y)
        # old_top_left = Vetor2D(ConfigJogo.TILE_SIZE.x*old_top_left_i_j.x+ConfigJogo.ARENA_TOP_LEFT.x,\
        #                        ConfigJogo.TILE_SIZE.y*old_top_left_i_j.y+ConfigJogo.ARENA_TOP_LEFT.y)

        # print(f"Topo: {ConfigJogo.ARENA_TOP_LEFT}")
        # print(f"Topo atual: {old_top_left}")
        # print(f"Topo futuro: {new_top_left}")

        for i in range(2):
            for j in range(2):
                if blocos[i+int(new_top_left_i_j.x)][j+int(new_top_left_i_j.y)] != ConfigJogo.EMPTY:
                    max_x = new_top_left.x + i*ConfigJogo.TILE_SIZE.x-ConfigJogo.PLAYER_SIZE.x
                    min_x = new_top_left.x + i*ConfigJogo.TILE_SIZE.x+ConfigJogo.PLAYER_SIZE.x
                    max_y = new_top_left.y + j*ConfigJogo.TILE_SIZE.y-ConfigJogo.PLAYER_SIZE.y
                    min_y = new_top_left.y + j*ConfigJogo.TILE_SIZE.y+ConfigJogo.PLAYER_SIZE.y
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


        # for i in range(len(blocos)):
        #     for j in range(len(blocos[i])):
        #         if blocos[i][j] != ConfigJogo.EMPTY:
        #             max_x = ConfigJogo.ARENA_TOP_LEFT.x + i*ConfigJogo.TILE_SIZE.x-ConfigJogo.PLAYER_SIZE.x
        #             min_x = ConfigJogo.ARENA_TOP_LEFT.x + i*ConfigJogo.TILE_SIZE.x+ConfigJogo.PLAYER_SIZE.x
        #             max_y = ConfigJogo.ARENA_TOP_LEFT.y + j*ConfigJogo.TILE_SIZE.y-ConfigJogo.PLAYER_SIZE.y
        #             min_y = ConfigJogo.ARENA_TOP_LEFT.y + j*ConfigJogo.TILE_SIZE.y+ConfigJogo.PLAYER_SIZE.y
        #             if (pos_x > max_x) and \
        #                 (pos_x < min_x) and \
        #                 (self.position.y > max_y) and \
        #                 (self.position.y < min_y):
        #                 pos_x = self.position.x
                    
        #             if (self.position.x > max_x) and \
        #                 (self.position.x < min_x) and \
        #                 (pos_y > max_y) and \
        #                 (pos_y < min_y):
        #                 pos_y = self.position.y
                        
        #             if (pos_x > max_x) and \
        #                 (pos_x < min_x) and \
        #                 (pos_y > max_y) and \
        #                 (pos_y < min_y):
        #                 pos_y = self.position.y
        #                 pos_x = self.position.x
                        
        self.position = Vetor2D(pos_x,pos_y)

    def desenha(self, tela):
        tela.blit(self.img,self.position.as_tuple())
