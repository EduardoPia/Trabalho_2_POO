
from typing import Tuple, List
import pygame as pg

from config_jogo import ConfigJogo
from vetor2d import Vetor2D
from utils import ler_imagem, dist
from bomb import Bomb
from cronometro import Cronometro
from chama import Chama

class Player:
    def __init__(self, position: Vetor2D, img_path:str):
        self.position = position
        self.img = ler_imagem(img_path,ConfigJogo.PLAYER_SIZE.as_tuple())
        self.cronometro_recarga = Cronometro() # conta recarga da bomba
        self.cronometro_explosao = Cronometro()
        self.tempo_bombas = []
        self.bombas_postas = 0
        self.orientation = Vetor2D(ConfigJogo.STOPPED,ConfigJogo.STOPPED)
        self.pos = Vetor2D(self.position.x,self.position.y)
        self.morreu = False

    def bota_bomba(self):
        self.cronometro_recarga.reset()
        self.bombas_postas += 1
        self.tempo_bombas.append(self.cronometro_explosao.tempo_passado())
        
    def testa_colisao_x(self,posicao_teste:Vetor2D) -> bool:
        
            if ((posicao_teste.x-ConfigJogo.PLAYER_SIZE.x) < self.pos.x) and \
                ((posicao_teste.x+ConfigJogo.TILE_SIZE.x) > self.pos.x) and \
                ((posicao_teste.y-ConfigJogo.PLAYER_SIZE.y) < self.position.y) and \
                ((posicao_teste.y+ConfigJogo.TILE_SIZE.y) > self.position.y):
                    return True
            return False
        
    def testa_colisao_y(self,posicao_teste:Vetor2D) -> bool:
                
            if ((posicao_teste.x-ConfigJogo.PLAYER_SIZE.x) < self.position.x) and \
                ((posicao_teste.x+ConfigJogo.TILE_SIZE.x) > self.position.x) and \
                ((posicao_teste.y-ConfigJogo.PLAYER_SIZE.y) < self.pos.y) and \
                ((posicao_teste.y+ConfigJogo.TILE_SIZE.y) > self.pos.y):
                    return True
            return False
        
    def testa_colisao_xy(self,posicao_teste:Vetor2D) -> bool:
                   
            if ((posicao_teste.x-ConfigJogo.PLAYER_SIZE.x) < self.pos.x) and \
                ((posicao_teste.x+ConfigJogo.TILE_SIZE.x) > self.pos.x) and \
                ((posicao_teste.y-ConfigJogo.PLAYER_SIZE.y) < self.pos.y) and \
                ((posicao_teste.y+ConfigJogo.TILE_SIZE.y) > self.pos.y):
                    return True
            return False

    def atualizar(self, blocos:List[List[int]],bombas:List[Bomb], chamas:List[Chama]):
        if not self.morreu:
            self.pos.x = self.position.x
            self.pos.y = self.position.y

            if self.orientation.y == ConfigJogo.UP:
                self.pos.y += -ConfigJogo.PLAYER_VEL
            if self.orientation.y == ConfigJogo.DOWN:
                self.pos.y += ConfigJogo.PLAYER_VEL
            if self.orientation.x == ConfigJogo.LEFT:
                self.pos.x += -ConfigJogo.PLAYER_VEL
            if self.orientation.x == ConfigJogo.RIGHT:
                self.pos.x += ConfigJogo.PLAYER_VEL
            
            new_top_left_i_j = Vetor2D(1.0005*(self.pos.x-ConfigJogo.ARENA_TOP_LEFT.x)//ConfigJogo.TILE_SIZE.x,\
                                1.0005*(self.pos.y-ConfigJogo.ARENA_TOP_LEFT.y)//ConfigJogo.TILE_SIZE.y)   

            new_top_left = Vetor2D(ConfigJogo.TILE_SIZE.x*new_top_left_i_j.x+ConfigJogo.ARENA_TOP_LEFT.x,\
                                ConfigJogo.TILE_SIZE.y*new_top_left_i_j.y+ConfigJogo.ARENA_TOP_LEFT.y)
            
            for i in range(2):
                for j in range(2):
                    if blocos[i+int(new_top_left_i_j.x)][j+int(new_top_left_i_j.y)] != ConfigJogo.EMPTY:
                        if self.testa_colisao_x(Vetor2D(new_top_left.x + i*ConfigJogo.TILE_SIZE.x,new_top_left.y + j*ConfigJogo.TILE_SIZE.y)):
                            self.pos.x = self.position.x
                        
                        if self.testa_colisao_y(Vetor2D(new_top_left.x + i*ConfigJogo.TILE_SIZE.x,new_top_left.y + j*ConfigJogo.TILE_SIZE.y)):
                            self.pos.y = self.position.y
                            
                        if self.testa_colisao_xy(Vetor2D(new_top_left.x + i*ConfigJogo.TILE_SIZE.x,new_top_left.y + j*ConfigJogo.TILE_SIZE.y)):
                            self.pos.y = self.position.y
                            self.pos.x = self.position.x
                        
            for bomba in bombas:
                if self.testa_colisao_x(bomba.position):
                    if dist(self.pos,bomba.position) < dist(self.position,bomba.position):
                        if dist(self.pos,bomba.position) > ConfigJogo.TOLERANCIA_BOMBA:    
                            self.pos.x = self.position.x
                    
                if self.testa_colisao_y(bomba.position):
                    if dist(self.pos,bomba.position) < dist(self.position,bomba.position):
                        if dist(self.pos,bomba.position) > ConfigJogo.TOLERANCIA_BOMBA:
                            self.pos.y = self.position.y
                
                if self.testa_colisao_xy(bomba.position):
                    if dist(self.pos,bomba.position) < dist(self.position,bomba.position):
                        if dist(self.pos,bomba.position) > ConfigJogo.TOLERANCIA_BOMBA:
                            self.pos.x = self.position.y
                            self.pos.y = self.position.x
                    
            for chama in chamas:
                if self.testa_colisao_xy(chama.centro):
                        self.morreu = True
                            
                for i in range(1,chama.dim[0]+1):
                    if self.testa_colisao_xy(Vetor2D(chama.centro.x-i*ConfigJogo.TILE_SIZE.x,chama.centro.y)):
                            self.morreu = True
                            
                for i in range(1,chama.dim[1]+1):
                    if self.testa_colisao_xy(Vetor2D(chama.centro.x+i*ConfigJogo.TILE_SIZE.x,chama.centro.y)):
                            self.morreu = True
                            
                for i in range(1,chama.dim[2]+1):
                    if self.testa_colisao_xy(Vetor2D(chama.centro.x,chama.centro.y-i*ConfigJogo.TILE_SIZE.y)):
                            self.morreu = True
                            
                for i in range(1,chama.dim[3]+1):
                    if self.testa_colisao_xy(Vetor2D(chama.centro.x,chama.centro.y+i*ConfigJogo.TILE_SIZE.y)):
                            self.morreu = True
            
            
            
            
                
            self.position.x = self.pos.x
            self.position.y = self.pos.y
                    
        for tempo in self.tempo_bombas:
            if (self.cronometro_explosao.tempo_passado() - tempo) > ConfigJogo.TEMPO_BOMBA_EXPLOSAO:
                self.tempo_bombas.remove(tempo)
                self.bombas_postas -= 1
                    

    def desenha(self, tela):
        if not self.morreu:
            tela.blit(self.img,self.position.as_tuple())
