from typing import List

import pygame as pg

from game_object import GameObject
from mapa import Mapa
from vetor2d import Vetor2D
from config_jogo import ConfigJogo
from utils import ler_imagem, testa_colisao
from cronometro import Cronometro

class Chama(GameObject):
    def __init__(self, position: Vetor2D, dim:List[int], player:int):
        super().__init__(position, ConfigJogo.TILE_SIZE, False, False)
        self.dim:List[int] = dim ## left, up, right, down
        self.cronometro:Cronometro = Cronometro() # Tempo de duração da chama
        self.tiles:List[list] = [] # Conjunto de listas de imagem/posicao
        size = (ConfigJogo.TILE_SIZE+Vetor2D(1,1)).as_tuple() # Tamanho dela (0 (1,1) existe para preencher lacunas quando desenha com o tamanho normal)
        self.player:int = player # Player que gerou a chama (importante para pontuação)
        
        # center
        self.tiles.append([ler_imagem(ConfigJogo.FOGO_CENT,size),self.position])
        
        # left
        for i in range(1,dim[0]+1):
            self.tiles.append([ler_imagem(ConfigJogo.FOGO_HOR,size), self.position + Vetor2D(-i*self.size.x,0)])
            
        # up     
        for j in range(1,dim[1]+1):
            self.tiles.append([ler_imagem(ConfigJogo.FOGO_VERT,size) , self.position + Vetor2D(0,-j*self.size.y)])
            
        # right    
        for i in range(1,dim[2]+1):
            self.tiles.append([ler_imagem(ConfigJogo.FOGO_HOR,size) , self.position + Vetor2D(i*self.size.x,0)])
            
        # down    
        for j in range(1,dim[3]+1):
            self.tiles.append([ler_imagem(ConfigJogo.FOGO_VERT,size) , self.position + Vetor2D(0,j*self.size.y)])
            
    def tratamento(self):
        pass
    
    def atualizar(self, lista: List[GameObject], mapa: Mapa):
        ## Testa se deu o tempo da chama
        if self.cronometro.tempo_passado() > ConfigJogo.TEMPO_CHAMA:
            self.remover[0] = True
            
        ## Testa colisao
        for object in lista:
            ## Colisao com a barra horizontal da chama
            if testa_colisao(Vetor2D(self.position.x-self.dim[0]*ConfigJogo.TILE_SIZE.x,self.position.y), \
                Vetor2D(self.size.x*(1+self.dim[0]+self.dim[2]),self.size.y), \
                            object.position,object.size):
                if object.destructable:
                    self.remover[1].append([object,self.player])
            ## Colisao com a barra vertical da chama
            if testa_colisao(Vetor2D(self.position.x,self.position.y-self.dim[1]*ConfigJogo.TILE_SIZE.y), \
                Vetor2D(self.size.x,self.size.y*(1+self.dim[1]+self.dim[3])), \
                            object.position,object.size):
                if object.destructable:
                    self.remover[1].append([object,self.player])

            
    def desenhar(self, tela: pg.Surface):
        ## Desenha cada tile na tela
        for fire in self.tiles:
            tela.blit(fire[0],fire[1].as_tuple())