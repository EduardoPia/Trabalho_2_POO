import pygame as pg
import random as rd
from copy import deepcopy
from typing import List

from config_jogo import ConfigJogo
from mapa import Mapa
from vetor2d import Vetor2D
from inimigo_base import Inimigo_base
from utils import ler_imagem,testa_colisao,resultado_colisao,dist
from cronometro import Cronometro
from projetil import Projetil
from player import Player
from bomba import Bomba
from game_object import GameObject

class Alienigina(Inimigo_base):
    def __init__(self, position: Vetor2D):
        super().__init__(position)
        self.pos:Vetor2D = deepcopy(self.position) # Posição depois do movimento
        self.img:pg.Surface = ler_imagem(ConfigJogo.IMG_ALIEN[rd.choice((0,1,2,3))],self.size.as_tuple()) # Carrega a imagem do alienigina
        self.cronometro:Cronometro = Cronometro() # Controla a criação de projéteis
        
    def tratamento(self): # Necessario existir pois é um método de Inimigo_base(herdado de GameObject)
        pass
    
    def atualizar(self, lista: List[GameObject], mapa: Mapa):
        
        ## Caso toque um player diz para a cena principal o remover
        for object in lista:
            if type(object) == Player:
                if testa_colisao(object.position,object.size,self.position,self.size):
                    self.remover[1].append([object,0])
        
        ## Cria projetil
        if self.cronometro.tempo_passado() > ConfigJogo.RECARGA_PROJETIL:
            self.cronometro.reset()
            lista.append(Projetil(self.position))
        
        ## Faz o movimento 
        self.pos = self.position + self.velo
        
        # Testa colisão com o mapa
        # Para essa colisão testa-se os quadrados ao redor do alienígina por colisão, caso ela ocorra não anda
        new_top_left_i_j = Vetor2D(1.0005*(self.pos.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,\
                                1.0005*(self.pos.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)   

        new_top_left = Vetor2D(ConfigJogo.TILE_SIZE.x*new_top_left_i_j.x+ConfigJogo.ARENA_TOP_LEFT.x,\
                                ConfigJogo.TILE_SIZE.y*new_top_left_i_j.y+ConfigJogo.ARENA_TOP_LEFT.y)
            
        for i in range(2):
            for j in range(2):
                if mapa.blocos[i+int(new_top_left_i_j.x)][j+int(new_top_left_i_j.y)] != ConfigJogo.EMPTY:
                    self.pos = resultado_colisao(self.position,self.size,self.pos,\
                        Vetor2D(new_top_left.x + i*ConfigJogo.TILE_SIZE.x,new_top_left.y + j*ConfigJogo.TILE_SIZE.y),ConfigJogo.TILE_SIZE)
    
        # Testa colisão com outros objetos, caso ela ocorra não anda
        for object in lista:
            if type(object) == Bomba:
                self.pos = resultado_colisao(self.position,self.size,self.pos,object.position,ConfigJogo.TILE_SIZE)       
                  
        # Caso nao tenha andado (porque teria colisão com algo) seta uma nova velocidade, caso contrário atualiza a posição
        if self.position.x == self.pos.x and self.pos.y == self.position.y:
            self.velo = ConfigJogo.INIM_VEL[rd.choice((0,1,2,3))]
        else:
            self.position.x = self.pos.x
            self.position.y = self.pos.y                        
           
    def desenhar(self, tela: pg.Surface):
        tela.blit(self.img,self.position.as_tuple())