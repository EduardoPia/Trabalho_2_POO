import pygame as pg
import random as rd
from typing import List

from config_jogo import ConfigJogo
from game_object import GameObject
from mapa import Mapa
from cronometro import Cronometro
from alienigina import Alienigina
from utils import ler_imagem
from fantasma import Fantasma

class Quartel(GameObject):
    def __init__(self):
        super().__init__(ConfigJogo.SPAWN_QUARTEL, ConfigJogo.TILE_SIZE, False, True)
        self.img:pg.Surface = ler_imagem(ConfigJogo.IMG_QUARTEL,self.size.as_tuple()) # Img quartel
        self.vida:int = ConfigJogo.VIDA_QUARTEL # Vida
        self.cronometro:Cronometro = Cronometro() # Conta tempo para spawn 
        self.timer_immune:Cronometro = Cronometro() # Deixa imune por um tempo depois de ser atingido por uma bomba (tempo da explosão dela)
        
    def tratamento(self):
        pass
    
    def atualizar(self, lista: List[GameObject], mapa: Mapa):
        
        ## Checa a quantidade de inimigos e tipo
        number_fantasma = 0
        number_alienigina = 0
        for object in lista:
            if (type(object) == Fantasma):
                number_fantasma += 1
            if (type(object) == Alienigina):
                number_alienigina += 1
        
        # Tenta spawnar, pode não conseguir por já ter muitos inimigos
        if self.cronometro.tempo_passado() > ConfigJogo.TEMPO_SPAWN:
            self.cronometro.reset()
            if (number_alienigina < ConfigJogo.MAX_ALIENIGINAS) and (number_fantasma < ConfigJogo.MAX_FANTASMAS):
                if rd.choice((0,1)) == 0:
                    lista.append(Alienigina(self.position))
                else:
                    lista.append(Fantasma(self.position))
            elif (number_alienigina >= ConfigJogo.MAX_ALIENIGINAS) and (number_fantasma < ConfigJogo.MAX_FANTASMAS):
                lista.append(Fantasma(self.position))
            elif (number_alienigina < ConfigJogo.MAX_ALIENIGINAS) and (number_fantasma >= ConfigJogo.MAX_FANTASMAS):
                lista.append(Alienigina(self.position))
                
    def desenhar(self, tela: pg.Surface):
        tela.blit(self.img,self.position.as_tuple())