from math import sqrt
import pygame
from typing import Tuple
from math import sqrt

from vetor2d import Vetor2D

def ler_imagem(caminho: str, tamanho: Tuple[int, int]) -> pygame.Surface:
    # le a imagem do arquivo
    image = pygame.image.load(caminho)

    # redimensiona a imagem para o tamanho especificado
    image = pygame.transform.scale(image, tamanho)

    # ajusta o colorkey para dar suporte para transparencia
    image = image.convert_alpha()

    return image

def dist(a:Vetor2D, b:Vetor2D) -> float:
    ## Retorna a distância entre dois pontos
    return(sqrt((a.x-b.x)**2 + (a.y-b.y)**2))

def testa_colisao(pos_1:Vetor2D,size_1:Vetor2D,pos_2:Vetor2D,size_2:Vetor2D) -> bool:
    ## Testa colisão entre dois retângulos
    if ((pos_2.x-size_1.x) < pos_1.x) and \
    ((pos_2.x+size_2.x) > pos_1.x) and \
    ((pos_2.y-size_1.y) < pos_1.y) and \
    ((pos_2.y+size_2.y) > pos_1.y):
        return True
    return False

def resultado_colisao(pos_ini:Vetor2D,size_ini:Vetor2D,pos_final:Vetor2D,pos_2:Vetor2D,size_2:Vetor2D) -> Vetor2D:
    """
    Testa colisao e retorna a nova posicao sem colisões
    """
    nova_posicao = Vetor2D(pos_final.x,pos_final.y)

    ## testa colisao x
    if ((pos_2.x-size_ini.x) < nova_posicao.x) and \
        ((pos_2.x+size_2.x) > nova_posicao.x) and \
        ((pos_2.y-size_ini.y) < pos_ini.y) and \
        ((pos_2.y+size_2.y) > pos_ini.y):
            nova_posicao.x = pos_ini.x

    ## testa colisao y
    if ((pos_2.x-size_ini.x) < pos_ini.x) and \
        ((pos_2.x+size_2.x) > pos_ini.x) and \
        ((pos_2.y-size_ini.y) < nova_posicao.y) and \
        ((pos_2.y+size_2.y) > nova_posicao.y):
            nova_posicao.y = pos_ini.y

    ## testa colisao xy
    if ((pos_2.x-size_ini.x) < nova_posicao.x) and \
        ((pos_2.x+size_2.x) > nova_posicao.x) and \
        ((pos_2.y-size_ini.y) < nova_posicao.y) and \
        ((pos_2.y+size_2.y) > nova_posicao.y):
            nova_posicao.x = pos_ini.x
               
    return nova_posicao

def colisao_rect_circle(rect_pos:Vetor2D,rect_size:Vetor2D,center:Vetor2D,radius:float) -> bool:
    ## Colisão entre retângulo e círculo
    if (center.x < rect_pos.x+rect_size.x+radius) and \
       (center.x > rect_pos.x-radius) and \
       (center.y < rect_pos.y+rect_size.y+radius) and \
       (center.y > rect_pos.y-radius):
        if ((center.x < rect_pos.x) and (center.y < rect_pos.y)) or \
           ((center.x > rect_pos.x+rect_size.x) and (center.y < rect_pos.y)) or \
           ((center.x < rect_pos.x) and (center.y > rect_pos.y+rect_size.y)) or \
           ((center.x > rect_pos.x+rect_size.x) and (center.y > rect_pos.y+rect_size.y)):    
            if ((dist(center,rect_pos) < radius) or \
                (dist(center,rect_pos+Vetor2D(rect_size.x,0)) < radius) or \
                (dist(center,rect_pos+Vetor2D(0,rect_size.y)) < radius) or \
                (dist(center,rect_pos+rect_size)) < radius):
                return True
            return False
        return True
    return False
            