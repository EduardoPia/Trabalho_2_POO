

from config_jogo import ConfigJogo
from vetor2d import Vetor2D
from typing import List
from utils import ler_imagem
from cronometro import Cronometro
from vetor2d import Vetor2D

class Chama:
    def __init__(self,centro:Vetor2D,dim:List[int]):
        self.centro = centro
        self.dim = dim
        self.cronometro = Cronometro()
        self.tiles = []
        self.tiles.append([ler_imagem("sprites\items\Fogo.png",(ConfigJogo.TILE_SIZE+Vetor2D(1,1)).as_tuple()),self.centro])
        for i in range(1,dim[0]+1):
            self.tiles.append([ler_imagem("sprites\items\FogoHorizontal.png",(ConfigJogo.TILE_SIZE+Vetor2D(1,1)).as_tuple()) \
                , self.centro+Vetor2D(-i*ConfigJogo.TILE_SIZE.x,0)])
        for i in range(1,dim[1]+1):
            self.tiles.append([ler_imagem("sprites\items\FogoHorizontal.png",(ConfigJogo.TILE_SIZE+Vetor2D(1,1)).as_tuple()) \
                , self.centro+Vetor2D(i*ConfigJogo.TILE_SIZE.x,0)])
        for j in range(1,dim[2]+1):
            self.tiles.append([ler_imagem("sprites\items\FogoVertical.png",(ConfigJogo.TILE_SIZE+Vetor2D(1,1)).as_tuple()) \
                , self.centro+Vetor2D(0,-j*ConfigJogo.TILE_SIZE.y)])
        for j in range(1,dim[3]+1):
            self.tiles.append([ler_imagem("sprites\items\FogoVertical.png",(ConfigJogo.TILE_SIZE+Vetor2D(1,1)).as_tuple()) \
                , self.centro+Vetor2D(0,j*ConfigJogo.TILE_SIZE.y)])
        
        
            
        
    def terminou(self):
        return (self.cronometro.tempo_passado() > ConfigJogo.TEMPO_CHAMA)
        
    def desenha(self,tela):
        for fire in self.tiles:
            tela.blit(fire[0],fire[1].as_tuple())