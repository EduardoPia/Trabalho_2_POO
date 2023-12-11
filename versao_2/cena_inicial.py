import pygame as pg
import sys

from utils import ler_imagem
from vetor2d import Vetor2D
from config_jogo import ConfigJogo as C_J
import time

class CenaInicial:
    def __init__(self, tela:pg.Surface):
        
        ## Tela e posição do cursor
        self.tela:pg.Surface = tela
        self.posicao_cursor:Vetor2D = Vetor2D(C_J.POS_TXT1_INIT.x-3.9*C_J.PLAYER_SIZE.x,C_J.POS_TXT1_INIT.y)
        
        ## Imagens
        self.background:pg.Surface = ler_imagem('sprites/map/cena_init_background.png', C_J.DIM_TELA.as_tuple())
        self.personagem1:pg.Surface = ler_imagem('sprites/chars/pacman-black.png', C_J.PLAYER_SIZE.as_tuple())
        self.personagem2:pg.Surface = ler_imagem('sprites/chars/pacman-black.png', C_J.PLAYER_SIZE.as_tuple())
        self.personagem3:pg.Surface = ler_imagem('sprites/chars/pacman-white.png', C_J.PLAYER_SIZE.as_tuple())
        self.fogo:pg.Surface = ler_imagem('sprites/items/Fogo.png', C_J.PLAYER_SIZE.as_tuple())
        self.bomba:pg.Surface = ler_imagem('sprites/items/bomba.png', C_J.PLAYER_SIZE.as_tuple())
        
        ## Variaveis de controle
        self.encerrado:bool = False
        self.apertou_para_cima:bool = False
        self.apertou_para_baixo:bool = False
        self.selecionou_num_player:bool = False
        self.num_player:int = 0
       
        ## Coisas do pygame para botar música
        pg.mixer.init()
        pg.mixer.music.load('sprites/map/INIT_SONG.mp3')
        self.bomb_sound:pg.mixer.Sound = pg.mixer.Sound('sprites/items/BOMB_SONG.wav')

    def tratamento_eventos(self):
        
        ## Se apertou esc encerra
        pg.event.get()
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
            
        ## Checa as teclas apertadas e registra
        if pg.key.get_pressed()[pg.K_UP] or pg.key.get_pressed()[pg.K_w]:
            self.apertou_para_cima = True
        if pg.key.get_pressed()[pg.K_DOWN] or pg.key.get_pressed()[pg.K_s]:
            self.apertou_para_baixo = True
        if pg.key.get_pressed()[pg.K_SPACE]:
            self.selecionou_num_player = True

    def atualiza_estado(self):
        
        
        ## Movimentação do cursor
        if self.apertou_para_cima:
            self.posicao_cursor=Vetor2D(C_J.POS_TXT1_INIT.x-3.9*C_J.PLAYER_SIZE.x,C_J.POS_TXT1_INIT.y)
            self.apertou_para_cima=False
        if self.apertou_para_baixo:
            self.posicao_cursor=Vetor2D(C_J.POS_TXT1_INIT.x-3.9*C_J.PLAYER_SIZE.x,C_J.POS_TXT2_INIT.y)
            self.apertou_para_baixo=False
            
        ## Se selecionou entre um ou dois players sinalizará que encerrará
        if self.selecionou_num_player:
            if self.posicao_cursor.y == C_J.POS_PERS1_INIT.y:
                self.num_player = 1
            else:
                self.num_player = 2
            self.encerrado = True
        
    def desenha(self):
        
        ## Desenha na tela inicial
        pg.display.set_caption("BOMBERMAN")
        self.tela.blit(self.background,(0,0))
        self.tela.blit(C_J.TEXTO1,C_J.POS_TXT1_INIT.as_tuple())
        self.tela.blit(C_J.TEXTO2,C_J.POS_TXT2_INIT.as_tuple())
        self.tela.blit(self.personagem1,C_J.POS_PERS1_INIT.as_tuple())
        self.tela.blit(self.personagem2,C_J.POS_PERS2_INIT.as_tuple())
        self.tela.blit(self.personagem3,C_J.POS_PERS3_INIT.as_tuple())
        
        ## Desenha cursor na tela
        if self.num_player == 0:
            self.tela.blit(self.bomba,(self.posicao_cursor.as_tuple()))
        elif self.num_player == 1:
            self.tela.blit(self.fogo,(self.posicao_cursor.as_tuple()))
        elif self.num_player == 2:
            self.tela.blit(self.fogo,(self.posicao_cursor.as_tuple()))
        pg.display.flip()
        
    def tocar_sons(self):
        ## Definido o metodo tocar_sons
        if self.selecionou_num_player:
            self.bomb_sound.play()
            time.sleep(0.95)
        else:
            pg.mixer.music.play(-1)
                   
    def executar(self):
        ## Executa o metodo tocar som fora do loop
        self.tocar_sons()
        
        ## Loop principal
        while not self.encerrado:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()
            
        ## Coloca o som da bomba
        pg.mixer.stop()    
        self.tocar_sons()
        pg.mixer.stop()
