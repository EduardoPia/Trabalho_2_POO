import pygame as pg
from typing import List

from game_object import GameObject
from vetor2d import Vetor2D
from cronometro import Cronometro
from chama import Chama
from utils import ler_imagem, testa_colisao
from config_jogo import ConfigJogo
from mapa import Mapa
from projetil import Projetil

class Bomba(GameObject):
    def __init__(self, position: Vetor2D, size: Vetor2D, player:int):
        super().__init__(position, size, True, False)
        self.img:pg.Surface = ler_imagem(ConfigJogo.BOMBA_IMG,ConfigJogo.TILE_SIZE.as_tuple()) # Carrega imagem da bomba
        self.cronometro:Cronometro = Cronometro() # Controla quando a bomba explode
        self.player:int = player # Salva o player que a colocou
        self.bomb_sound:pg.mixer.sound = pg.mixer.Sound('sprites/items/BOMB_SONG.wav') # Som da bomba explodindo
        self.tempo_passado:float = 0 # Junto do cronometro controla quando a bomba explode, essa variável existe por causa do fantasma
        self.tempo:float = 1 # Velocidade que o tempo passa (afetado pelo fantasma)
        
    def tratamento(self): ## Necessário que exista porque herda de GameObject
        pass
    
    def atualizar(self, lista: List[GameObject], mapa: Mapa):
        
        ## Checa se algum projetil atingiu a bomba
        bomba_explode = False
        for object in lista:
            if type(object) == Projetil:
                if testa_colisao(object.position,object.size, self.position, self.size):
                    bomba_explode = True
                    break

        ## Atualiza o tempo desde que a bomba foi colocada
        self.tempo_passado += self.tempo*self.cronometro.tempo_passado()        
        self.cronometro.reset()
        
        ## Se um projetil atingiu a bomba ou deu o tempo ela explode
        if (self.tempo_passado > ConfigJogo.TEMPO_BOMBA_EXPLOSAO) or bomba_explode:
            self.bomb_sound.play()
            self.remover = [True,[]]
            pos = Vetor2D(int((self.position.x-ConfigJogo.ARENA_TOP_LEFT.x)/ConfigJogo.TILE_SIZE.x+0.0001),int((self.position.y-ConfigJogo.ARENA_TOP_LEFT.y)/ConfigJogo.TILE_SIZE.y+0.0001))
            chama_dim = [ConfigJogo.DIST_EXPLOSAO,ConfigJogo.DIST_EXPLOSAO,ConfigJogo.DIST_EXPLOSAO,ConfigJogo.DIST_EXPLOSAO] ## left, up, right, down
            
            ## Testa colisão
            for j in range(-2,2): # defini se é esquerda, direita, cima ou baixo
                sair = False
                for i in range(1,ConfigJogo.DIST_EXPLOSAO+1): # anda ao longo do sentido cima, baixo, esquerda e direta
                    
                    # Essa dimensão_expansao simplesmente alterna de [-1,0],[0,-1],[1,0],[0,1] com base no j, para percorre para cima,
                    # baixo, esquerda e direita (nao nessa ordem)
                    dimensao_expansao = [((j+1)%2*(j//2+(j+2)//2)),((j)%2*(j//2+(j+2)//2))]
                    pos_teste = Vetor2D(pos.x+i*dimensao_expansao[0],pos.y+i*dimensao_expansao[1])
                    pos_chama = Vetor2D(ConfigJogo.ARENA_TOP_LEFT.x + ConfigJogo.TILE_SIZE.x*(pos_teste.x), \
                                                ConfigJogo.ARENA_TOP_LEFT.y + ConfigJogo.TILE_SIZE.y*(pos_teste.y))
                    
                    # Testa colisão com objetos que não são bombas, se atinge um ele para de se propagar
                    for object in lista:
                        if type(object) != Bomba:
                            if testa_colisao(object.position,Vetor2D(0.95*object.size.x,0.95*object.size.y), \
                                pos_chama,Vetor2D(0.95*ConfigJogo.TILE_SIZE.x,0.95*ConfigJogo.TILE_SIZE.y)):
                                chama_dim[j+2] = i
                                sair = True
                                break
                    if sair:
                        break
                    ## Testa com o mapa
                    if mapa.blocos[pos_teste.x][pos_teste.y] == ConfigJogo.DESTRUCTABLE:
                        mapa.blocos[pos_teste.x][pos_teste.y] = ConfigJogo.EMPTY
                        chama_dim[j+2] = i
                        mapa.barra.pontuacoes_icones_players[self.player][0] += 1
                        break
                    if mapa.blocos[pos_teste.x][pos_teste.y] == ConfigJogo.INDESTRUCTABLE:
                        chama_dim[j+2] = i-1
                        break
                    
            ## Cria uma chama com base nas dimensões coletadas
            lista.append(Chama(self.position,chama_dim, self.player))
                
    
    def desenhar(self, tela:pg.Surface):
        tela.blit(self.img,self.position.as_tuple())