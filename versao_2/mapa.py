import pygame as pg
from typing import List
import random

from utils import ler_imagem
from config_jogo import ConfigJogo

from barra import Barra

class Mapa:
    def __init__(self):
        self.blocos:List[List[int]] = [] # Matriz de blocos
        self.grama:pg.Surface = ler_imagem(ConfigJogo.IMG_GRAMA,ConfigJogo.ARENA_AREA.as_tuple()) # Img grama
        self.indestructable:pg.Surface = ler_imagem(ConfigJogo.IMG_INDESTRUCTABLE,(ConfigJogo.TILE_SIZE.x+1,ConfigJogo.TILE_SIZE.y+1)) # Img indestrutivel
        self.destructable:pg.Surface = ler_imagem(ConfigJogo.IMG_DESTRUCTABLE,(ConfigJogo.TILE_SIZE.x+1,ConfigJogo.TILE_SIZE.y+1))# Img destrutivel
        self.barra:Barra = Barra() # Barra de pontuação
        
        ## Preenche o mapa
        for i in range(ConfigJogo.ARENA_TILES.x):
            self.blocos.append([]) # Cria uma linha de blocos e depois a preenche
            for j in range(ConfigJogo.ARENA_TILES.y):
                # Preenche a linha de blocos com espaços vazios, destrutíveis e indestrutíveis
                # Se bloco é na borda:
                if (i ==0) or (i==ConfigJogo.ARENA_TILES.x-1) or (j==0) or (j==ConfigJogo.ARENA_TILES.y-1):
                    self.blocos[i].append(ConfigJogo.INDESTRUCTABLE)
                # Se bloco é area do quartel:
                elif (int(ConfigJogo.ARENA_TILES.x/2-ConfigJogo.AREA_QUARTEL.x/2) < i < int(ConfigJogo.ARENA_TILES.x/2+ConfigJogo.AREA_QUARTEL.x/2)) \
                    and (int(ConfigJogo.ARENA_TILES.y/2-ConfigJogo.AREA_QUARTEL.y/2) < j < int(ConfigJogo.ARENA_TILES.y/2+ConfigJogo.AREA_QUARTEL.y/2)):
                    self.blocos[i].append(ConfigJogo.EMPTY)
                # Se bloco é pilastra
                elif (i%2 ==0) and (j%2==0):
                    self.blocos[i].append(ConfigJogo.INDESTRUCTABLE)
                # Se bloco é quina de jogador:
                elif ((i<3) and (j<3)) or ((i+4>ConfigJogo.ARENA_TILES.x) and (j<3)) or ((i<3) and (j+4>ConfigJogo.ARENA_TILES.y)) or ((i+4>ConfigJogo.ARENA_TILES.x) and (j+4>ConfigJogo.ARENA_TILES.y)):
                    self.blocos[i].append(ConfigJogo.EMPTY)
                # Se bloco é aleatório:
                elif (random.random() < ConfigJogo.PROBABILITY_EMPTY):
                    self.blocos[i].append(ConfigJogo.EMPTY)
                else:
                    self.blocos[i].append(ConfigJogo.DESTRUCTABLE)
 
    
    def desenhar(self,tela:pg.Surface):
        # Preenche o fundo, barra e grama, depois desenha cada bloco
        tela.fill(ConfigJogo.COR_FUNDO)
        self.barra.desenha(tela)
        tela.blit(self.grama,ConfigJogo.ARENA_TOP_LEFT.as_tuple())
        for i in range(len(self.blocos)):
            for j in range(len(self.blocos[i])):
                if self.blocos[i][j] == ConfigJogo.INDESTRUCTABLE:
                    tela.blit(self.indestructable,(ConfigJogo.ARENA_TOP_LEFT.x+i*ConfigJogo.TILE_SIZE.x,ConfigJogo.ARENA_TOP_LEFT.y+j*ConfigJogo.TILE_SIZE.y))
                elif self.blocos[i][j] == ConfigJogo.DESTRUCTABLE:
                    tela.blit(self.destructable,(ConfigJogo.ARENA_TOP_LEFT.x+i*ConfigJogo.TILE_SIZE.x,ConfigJogo.ARENA_TOP_LEFT.y+j*ConfigJogo.TILE_SIZE.y))
        
    
