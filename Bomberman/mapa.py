import pygame as pg
from typing import List
from enum import Enum
import random

from utils import ler_imagem
from config_jogo import ConfigJogo
from vetor2d import Vetor2D

class Mapa:
    def __init__(self):
        
        self.blocos:List[List[int]] = []
        self.grama = ler_imagem("sprites/map/grama.png",ConfigJogo.ARENA_AREA.as_tuple())
        self.indestructable = ler_imagem("sprites/map/parede-fixa.png",(ConfigJogo.TILE_SIZE.x+1,ConfigJogo.TILE_SIZE.y+1))
        self.destructable = ler_imagem("sprites/map/parede-destruivel.png",(ConfigJogo.TILE_SIZE.x+1,ConfigJogo.TILE_SIZE.y+1))
        
        for i in range(ConfigJogo.ARENA_TILES.x):
            self.blocos.append([])
            for j in range(ConfigJogo.ARENA_TILES.y):
                if (i ==0) or (i==ConfigJogo.ARENA_TILES.x-1) or (j==0) or (j==ConfigJogo.ARENA_TILES.y-1):
                    self.blocos[i].append(ConfigJogo.INDESTRUCTABLE)
                elif (i%2 ==0) and (j%2==0):
                    self.blocos[i].append(ConfigJogo.INDESTRUCTABLE)
                elif ((i<3) and (j<3)) or ((i+4>ConfigJogo.ARENA_TILES.x) and (j<3)) or ((i<3) and (j+4>ConfigJogo.ARENA_TILES.y)) or ((i+4>ConfigJogo.ARENA_TILES.x) and (j+4>ConfigJogo.ARENA_TILES.y)):
                    self.blocos[i].append(ConfigJogo.EMPTY)
                elif (random.random() < ConfigJogo.PROBABILITY_EMPTY):
                    self.blocos[i].append(ConfigJogo.EMPTY)
                else:
                    self.blocos[i].append(ConfigJogo.DESTRUCTABLE)
        
        
    def desenha(self,tela:pg.surface):
        tela.fill((100, 100, 100))
        tela.blit(self.grama,ConfigJogo.ARENA_TOP_LEFT.as_tuple())
        for i in range(len(self.blocos)):
            for j in range(len(self.blocos[i])):
                if self.blocos[i][j] == ConfigJogo.INDESTRUCTABLE:
                    tela.blit(self.indestructable,(ConfigJogo.ARENA_TOP_LEFT.x+i*ConfigJogo.TILE_SIZE.x,ConfigJogo.ARENA_TOP_LEFT.y+j*ConfigJogo.TILE_SIZE.y))
                elif self.blocos[i][j] == ConfigJogo.DESTRUCTABLE:
                    tela.blit(self.destructable,(ConfigJogo.ARENA_TOP_LEFT.x+i*ConfigJogo.TILE_SIZE.x,ConfigJogo.ARENA_TOP_LEFT.y+j*ConfigJogo.TILE_SIZE.y))
