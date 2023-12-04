from typing import List
import pygame as pg

from config_jogo import ConfigJogo
from utils import ler_imagem
from cronometro import Cronometro

class Barra:
    def __init__(self):
        self.pontuacoes_icones_players:List(list) = [] # cada player é uma lista de 2 itens, sua pontuacao e sua img
        for i in range(2):
            player_img = ler_imagem(ConfigJogo.PLAYER_IMGS[i],ConfigJogo.TAM_ICONES_BARRA.as_tuple())
            self.pontuacoes_icones_players.append([0,player_img])
        self.cronometro = Cronometro()
        self.relogio = ler_imagem("sprites\map\Relogio.png",ConfigJogo.TAM_ICONES_BARRA.as_tuple())
        self.fonte = pg.font.Font(None,48)  # None usa a fonte padrão, tamanho 36

    
    def atualizar(self):
        pass
    
    def desenha(self,tela:pg.surface):
        pg.draw.rect(tela,(0,255,0),(0,0,ConfigJogo.BAR_SIZE.x,ConfigJogo.BAR_SIZE.y))
        pg.draw.rect(tela,(0,0,200),(ConfigJogo.BAR_SIZE.x*ConfigJogo.TOUGHNESS_BAR.x \
                                    ,ConfigJogo.BAR_SIZE.y*ConfigJogo.TOUGHNESS_BAR.y \
                                    ,ConfigJogo.BAR_SIZE.x-2*ConfigJogo.TOUGHNESS_BAR.x*ConfigJogo.BAR_SIZE.x \
                                    ,ConfigJogo.BAR_SIZE.y-2*ConfigJogo.TOUGHNESS_BAR.y*ConfigJogo.BAR_SIZE.y))
        
        tela.blit(self.relogio,ConfigJogo.POS_RELOGIO.as_tuple())
        t_restante = int(ConfigJogo.TEMPO_PARTIDA - self.cronometro.tempo_passado())
        tempo_restante = f"{t_restante//60}:{t_restante-60*(t_restante//60)}"
        texto_tempo = self.fonte.render(tempo_restante, True, (255,255,255))
        tela.blit(texto_tempo,(ConfigJogo.POS_RELOGIO.x+1.1*ConfigJogo.TAM_ICONES_BARRA.x, \
                                ConfigJogo.POS_RELOGIO.y+ConfigJogo.TAM_ICONES_BARRA.y/2.5))
        
        for i in range(len(self.pontuacoes_icones_players)):
            tela.blit(self.pontuacoes_icones_players[i][1],ConfigJogo.POS_ICONES_PLAYERS[i].as_tuple())
            text = str(self.pontuacoes_icones_players[i][0])
            texto = self.fonte.render(text, True, (255,255,255))
            tela.blit(texto,(ConfigJogo.POS_ICONES_PLAYERS[i].x+1.1*ConfigJogo.TAM_ICONES_BARRA.x, \
                                ConfigJogo.POS_ICONES_PLAYERS[i].y+ConfigJogo.TAM_ICONES_BARRA.y/2.5))
