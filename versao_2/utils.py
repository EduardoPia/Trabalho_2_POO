
import pygame
from typing import Tuple, List
from vetor2d import Vetor2D
from math import sqrt

def ler_imagem(caminho: str, tamanho: Tuple[int, int]):
    # le a imagem do arquivo
    image = pygame.image.load(caminho)

    # redimensiona a imagem para o tamanho especificado
    image = pygame.transform.scale(image, tamanho)

    # ajusta o colorkey para dar suporte para transparencia
    image = image.convert_alpha()

    return image

def dist(a:Vetor2D, b:Vetor2D):
    return(sqrt((a.x-b.x)**2 + (a.y-b.y)**2))

def testa_colisao(pos_1:Vetor2D,size_1:Vetor2D,pos_2:Vetor2D,size_2:Vetor2D) -> bool:
        if ((pos_2.x-size_1.x) < pos_1.x) and \
            ((pos_2.x+size_2.x) > pos_1.x) and \
            ((pos_2.y-size_1.y) < pos_1.y) and \
            ((pos_2.y+size_2.y) > pos_1.y):
                return True
        return False