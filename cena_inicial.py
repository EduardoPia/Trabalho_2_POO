from config_jogo import ConfigJogo as C_J
import pygame as pg
from utils import ler_imagem
import sys
from vetor2d import Vetor2D
import time

class CenaInicial:
    def __init__(self, tela):
        self.tela = tela
        self.encerrado = False
        self.background = ler_imagem('sprites/map/cena_init_background.png', C_J.DIM_TELA.as_tuple())
        self.personagem1 = ler_imagem('sprites/chars/pacman-black.png', C_J.PLAYER_SIZE.as_tuple())
        self.personagem2 = ler_imagem('sprites/chars/pacman-black.png', C_J.PLAYER_SIZE.as_tuple())
        self.personagem3 = ler_imagem('sprites/chars/pacman-white.png', C_J.PLAYER_SIZE.as_tuple())
        self.fogo = ler_imagem('sprites/items/Fogo.png', C_J.PLAYER_SIZE.as_tuple())
        self.bomba = ler_imagem('sprites/items/bomba.png', C_J.PLAYER_SIZE.as_tuple())
        self.apertou_para_cima = False
        self.apertou_para_baixo = False
        self.posicao_cursor = Vetor2D(C_J.POS_TXT1_INIT.x-3.9*C_J.PLAYER_SIZE.x,C_J.POS_TXT1_INIT.y)
        self.selecionou_num_player = False
        self.num_player = 0
        pg.init()
        pg.mixer.init()
        pg.mixer.music.load('sprites/map/INIT_SONG.mp3')
        self.bomb_sound = pg.mixer.Sound('sprites/items/BOMB_SONG.wav')

    def tratamento_eventos(self):
        #VERIFICA TELAS APERTADAS
        pg.event.get()
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
        if pg.key.get_pressed()[pg.K_UP] or pg.key.get_pressed()[pg.K_w]:
            self.apertou_para_cima = True
        if pg.key.get_pressed()[pg.K_DOWN] or pg.key.get_pressed()[pg.K_s]:
            self.apertou_para_baixo = True
        if pg.key.get_pressed()[pg.K_SPACE]:
            self.selecionou_num_player = True

    def atualiza_estado(self):
        #TECLAS UP, DOWN E SPACE MOVEM O CURSOR E SELECIONA
        if self.apertou_para_cima:
            self.posicao_cursor=Vetor2D(C_J.POS_TXT1_INIT.x-3.9*C_J.PLAYER_SIZE.x,C_J.POS_TXT1_INIT.y)
            self.apertou_para_cima=False
        if self.apertou_para_baixo:
            self.posicao_cursor=Vetor2D(C_J.POS_TXT1_INIT.x-3.9*C_J.PLAYER_SIZE.x,C_J.POS_TXT2_INIT.y)
            self.apertou_para_baixo=False
        if self.selecionou_num_player:
            pass
            if self.posicao_cursor.y == C_J.POS_PERS1_INIT.y:
                self.num_player = 1
            else:
                self.num_player = 2
            self.encerrado = True
        
    def desenha(self):
        
        #PREENCHE A TELA INICIAL
        pg.display.set_caption("BOMBERMAN")
        self.tela.blit(self.background,(0,0))
        self.tela.blit(C_J.TEXTO1,C_J.POS_TXT1_INIT.as_tuple())
        self.tela.blit(C_J.TEXTO2,C_J.POS_TXT2_INIT.as_tuple())
        self.tela.blit(self.personagem1,C_J.POS_PERS1_INIT.as_tuple())
        self.tela.blit(self.personagem2,C_J.POS_PERS2_INIT.as_tuple())
        self.tela.blit(self.personagem3,C_J.POS_PERS3_INIT.as_tuple())
        
        # DESENHA MEU CURSOR NA TELA QUE SERÁ A BOMBA
        # DESENHA A EXPLOSÃO SE SELECIONAR
        if self.num_player == 0:
            self.tela.blit(self.bomba,(self.posicao_cursor.as_tuple()))
        elif self.num_player == 1:
            self.tela.blit(self.fogo,(self.posicao_cursor.as_tuple()))
        elif self.num_player == 2:
            self.tela.blit(self.fogo,(self.posicao_cursor.as_tuple()))
        pg.display.flip()
        
    def tocar_sons(self):
        #DEFINIDO O METODO TOCAR_SONS
        if self.selecionou_num_player:
            self.bomb_sound.play()
            time.sleep(0.95)
        else:
            pg.mixer.music.play(-1)
            
        
    def executar(self):
        #EXECUTA O METODO TOCAR SOM FORA DO LOOP
        # self.tocar_sons()
        
        while not self.encerrado:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()
        #FECHA E ABRE NOVAMENTE PARA O EFEITO SONORO DA BOMBA
        pg.mixer.stop()    
        self.tocar_sons()
        pg.mixer.stop()


# tela = pg.display.set_mode((C_J.DIM_TELA.x,C_J.DIM_TELA.y))    
# tela_inicial = CenaInicial(tela)
# tela_inicial.executar()
