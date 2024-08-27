from abc import ABC, abstractmethod
from copy import deepcopy
import pygame as pg

from vetor2d import Vetor2D
from mapa import Mapa

# Classe abstrata para os objetos do jogo
class GameObject(ABC):
    def __init__(self, position:Vetor2D,size:Vetor2D, collision:bool, destructable: bool):
        self.position:Vetor2D = deepcopy(position) # Posição do objeto
        self.size:Vetor2D = deepcopy(size) # Tamanho
        self.collision:bool = collision # Ele colide com o player
        self.remover:list = [False,[]] # Lista que indica que o objeto está requerindo que a cena remove o próprio objeto *primeiro argumento"
        # Ou outro objeto (segundo argumento, que contém o objeto e o player que deve ser atribuida a pontuação, se aplicável)  
        self.destructable:bool = destructable # Se ele é destrutível
    
    @abstractmethod # Tratamento de eventos
    def tratamento(self):
        """ faz o tratamento """
    
    @abstractmethod # Atualização
    def atualizar(self,lista:list, mapa: Mapa):
        """ atualiza"""
    
    @abstractmethod # desenho
    def desenhar(self,tela:pg.Surface):
        """ desenha na tela """
