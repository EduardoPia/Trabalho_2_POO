import pygame as pg
import random as rd
from typing import List

from config_jogo import ConfigJogo
from mapa import Mapa
from vetor2d import Vetor2D
from inimigo_base import Inimigo_base
from utils import ler_imagem, testa_colisao, resultado_colisao
from player import Player
from game_object import GameObject

class Fantasma(Inimigo_base):
    def __init__(self, position: Vetor2D):
        super().__init__(position)
        self.img:pg.Surface = ler_imagem(ConfigJogo.IMG_GHOST,self.size.as_tuple()) # Carrega a imagem do fantasma
        self.circle:pg.Surface = ler_imagem(ConfigJogo.IMG_CIRCLE,ConfigJogo.SIZE_CIRCLE.as_tuple()) # Carrega a imagem do circulo do fantasma
        self.circle.set_alpha(80) # Coloca transparência para poder ver atras do circulo
        self.center:Vetor2D = self.position + Vetor2D(self.size.x/2,self.size.y/2) # Calcula o centro
        self.circle_pos:Vetor2D = self.center - Vetor2D(ConfigJogo.CIRCLE_DIAMENTER/2,ConfigJogo.CIRCLE_DIAMENTER/2) 
        # Calcula o canto superior esquerdo do circulo
        self.tipo_aura:float = rd.choice(ConfigJogo.AURAS_FANTASMA) # tipo da aura, se acelera ou desacelera (por base 1/2 ou 2)
        
    def tratamento(self): # Necessario existir pois é um método de Inimigo_base(herdado de GameObject)
        pass
    
    def atualizar(self, lista: List[GameObject], mapa: Mapa):
        
        ## Caso toque um player diz para a cena principal o remover
        for object in lista:
            if type(object) == Player:
                if testa_colisao(object.position,object.size,self.position,self.size):
                    self.remover[1].append([object,0])

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
                if mapa.blocos[i+int(new_top_left_i_j.x)][j+int(new_top_left_i_j.y)] == ConfigJogo.INDESTRUCTABLE:
                    self.pos = resultado_colisao(self.position,self.size,self.pos,\
                        Vetor2D(new_top_left.x + i*ConfigJogo.TILE_SIZE.x,new_top_left.y + j*ConfigJogo.TILE_SIZE.y),ConfigJogo.TILE_SIZE)       
                  
        # Caso nao tenha andado (porque teria colisão com algo) seta uma nova velocidade, caso contrário atualiza a posição
        if self.position.x == self.pos.x and self.pos.y == self.position.y:
            self.velo = ConfigJogo.INIM_VEL[rd.choice((0,1,2,3))]
        else:
            self.position.x = self.pos.x
            self.position.y = self.pos.y   

        ## Atualiza a posição do circulo
        self.center = self.position + Vetor2D(self.size.x/2,self.size.y/2) 
        self.circle_pos = self.center - Vetor2D(ConfigJogo.CIRCLE_DIAMENTER/2,ConfigJogo.CIRCLE_DIAMENTER/2)

    def desenhar(self, tela: pg.Surface):
        ## Desenha o circulo e dps o mapa
        tela.blit(self.circle,self.circle_pos.as_tuple())
        tela.blit(self.img,self.position.as_tuple())