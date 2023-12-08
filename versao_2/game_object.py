from abc import ABC, abstractmethod
from copy import deepcopy
import pygame as pg

from vetor2d import Vetor2D

# Classe abstrata pura.
class GameObject(ABC):
    def __init__(self, position:Vetor2D):
        self.position = deepcopy(position)
    
    @abstractmethod
    def tratamento(self):
        """ faz o tratamento """
    
    @abstractmethod
    def atualizar(self,lista:list):
        """ atualiza"""
    
    @abstractmethod
    def desenhar(self,tela:pg.surface):
        """ desenha na tela """
