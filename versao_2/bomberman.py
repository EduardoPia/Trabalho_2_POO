import pygame as pg

from config_jogo import ConfigJogo
from cena_inicial import CenaInicial
from cena_principal import CenaPrincipal
from cena_final import CenaFinal

class Bomberman:
    
    def __init__(self):
        
        pg.init()
        
        self.tela = pg.display.set_mode((ConfigJogo.DIM_TELA.x,ConfigJogo.DIM_TELA.y))
        
    def executar(self):
        cena_inicial = CenaInicial(self.tela)
        cena_inicial.executar()
        
        while True:
            cena_principal = CenaPrincipal(self.tela,cena_inicial.num_player)
            cena_principal.executar()
            
            cena_final = CenaFinal(self.tela, cena_principal)
            cena_final.executar()
            