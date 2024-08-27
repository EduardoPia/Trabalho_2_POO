import pygame as pg
import sys
from typing import List

from utils import ler_imagem
from config_jogo import ConfigJogo 
from player import Player
from game_object import GameObject

class CenaFinal:
    def __init__(self, tela:pg.Surface,pontuacoes_players:List[list],objetos:List[GameObject]):
        
        ## Tela e pontuações
        self.tela:pg.Surface = tela
        self.pont_player1:pg.Surface = ConfigJogo.FONTEEND.render(f"{pontuacoes_players[0][0]}", True, ConfigJogo.COR_END)
        self.pont_player2:pg.Surface = ConfigJogo.FONTEEND.render(f"{pontuacoes_players[1][0]}", True, ConfigJogo.COR_END) 
        
        ## Variaveis de controle
        self.encerrado:bool = False
        self.perderam:bool = True
        self.ganhador:int = 0
        for object in objetos:
            if type(object) == Player:
                self.perderam = False
                break
        if pontuacoes_players[0][0] > pontuacoes_players[1][0]:
            self.ganhador = 1
        elif pontuacoes_players[0][0] < pontuacoes_players[1][0]:
            self.ganhador = 2
        
        ## Imagens
        self.game_over:pg.Surface = ler_imagem(ConfigJogo.GAME_OVER, ConfigJogo.SIZE_GAMEOVER_WON.as_tuple())
        self.players:List[pg.Surface] = [ler_imagem(ConfigJogo.PLAYER_IMGS[0],ConfigJogo.SIZE_IMG_PLAYER.as_tuple()), \
                        ler_imagem(ConfigJogo.PLAYER_IMGS[1],ConfigJogo.SIZE_IMG_PLAYER.as_tuple())]
        self.big_players:List[pg.Surface] = [ler_imagem(ConfigJogo.PLAYER_IMGS[0],ConfigJogo.SIZE_BIG_PLAYER.as_tuple()), \
                        ler_imagem(ConfigJogo.PLAYER_IMGS[1],ConfigJogo.SIZE_BIG_PLAYER.as_tuple())]
                
    def tratamento_eventos(self):
        
        ## Se apertou esc encerra
        pg.event.get()
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
            
        ## Variaveis de controle
            
        ## Checa as teclas apertadas e registra
        if pg.key.get_pressed()[pg.K_RETURN]:
            self.encerrado = True

    def atualiza_estado(self):
        
        pass
        
    def desenha(self):
        
        ## Desenha na tela inicial
        self.tela.fill((0,0,0))
        
        # Desenha game over se perderam, desenha ganharam se ganharam
        if self.perderam:
            self.tela.blit(self.game_over,(0,0))
        elif self.ganhador == 0:
            self.tela.blit(ConfigJogo.TXT_EMPATE, ConfigJogo.POS_EMPATE.as_tuple())
        else:
            self.tela.blit(self.big_players[self.ganhador-1],ConfigJogo.POS_GANHADOR.as_tuple())
            self.tela.blit(ConfigJogo.TXT_GANHOU,ConfigJogo.POS_TXT_GANHOU.as_tuple())
            
        # Desenha pontuações e escrita para apertar enter
        self.tela.blit(self.players[0],ConfigJogo.POS_PLAYER1.as_tuple())
        self.tela.blit(self.pont_player1,(ConfigJogo.POS_PLAYER1+ConfigJogo.DISTANCE_TO_TXT).as_tuple())
        
        self.tela.blit(self.players[1],ConfigJogo.POS_PLAYER2.as_tuple())
        self.tela.blit(self.pont_player2,(ConfigJogo.POS_PLAYER2+ConfigJogo.DISTANCE_TO_TXT).as_tuple())
        
        self.tela.blit(ConfigJogo.TEXTO_ENTER,ConfigJogo.POS_TXT_ENTER.as_tuple())


        pg.display.flip()
                   
    def executar(self):
        
        ## Loop principal
        while not self.encerrado:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()
            