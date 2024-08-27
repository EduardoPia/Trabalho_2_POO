from typing import List
import pygame as pg
import sys

from game_object import GameObject
from config_jogo import ConfigJogo
from cronometro import Cronometro
from player import Player
from mapa import Mapa
from quartel import Quartel
from alienigina import Alienigina
from fantasma import Fantasma
from bomba import Bomba
from utils import colisao_rect_circle

class CenaPrincipal:
    def __init__(self,tela:pg.Surface,num_player:int):
        self.objects:List[GameObject] = []
        self.mapa:Mapa = Mapa()
        self.tela:pg.Surface = tela
        self.cronometro:Cronometro = Cronometro()
        self.tempo_jogo:Cronometro = Cronometro()
        
        ## Cria os players
        for i in range(num_player):
            new_player = Player(ConfigJogo.PLAYERS_POS[i],i)
            self.objects.append(new_player)
            
        ## Cria o quartel
        self.objects.append(Quartel())
        
    def desacelera_player_bomba(self):
        
        ## Reseta a velocidade de cada player/bomba
        bombas_player:List[GameObject] = []
        for object in self.objects:
            if type(object) == Bomba or type(object) == Player:
                object.tempo = 1
                bombas_player.append(object)
                
        ## Ajusta a velocidade do tempo de cada player/bomba com base em cada fantasma
        for object in self.objects:
            if type(object) == Fantasma:
                for obj in bombas_player:
                    if colisao_rect_circle(obj.position,obj.size,object.center,ConfigJogo.CIRCLE_DIAMENTER/2):
                        obj.tempo = obj.tempo*object.tipo_aura
                     
    def tratamento(self):
        pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
            
        for object in self.objects:
            object.tratamento()
            
    def atualizar(self):
        ## Atualiza a velocidade da passagem do tempo para bombas e players com base em fantasmas
        self.desacelera_player_bomba()
        
        for object in self.objects:
            object.atualizar(self.objects, self.mapa)

            ## remover objetos que o objeto falou para remover
            for objeto in object.remover[1]:
                remova = objeto[0] # Armazena o objeto que deve ser removido
                if remova in self.objects: # Se esse objeto existir na lista do jogo, analisa para removê-lo
                    
                    # Tentar remover o quartel nada mais é que reduzir suas vidas
                    if type(remova) == Quartel:
                        # Esse timer existe para que um quartel não possa ser atingido por várias bombas ao mesmo tempo
                        if remova.timer_immune.tempo_passado() > ConfigJogo.TEMPO_IMMUNE:
                            remova.timer_immune.reset()
                            remova.vida = remova.vida - 1
                            # Se acabarem as vidas ele pode então ser removido
                            if remova.vida == 0:
                                self.mapa.barra.pontuacoes_icones_players[objeto[1]][0] += 100
                                self.objects.remove(remova)
                    else:
                        # Caso remova um inimigo adiciona pontuação ao player
                        if type(remova) == Fantasma:
                            self.mapa.barra.pontuacoes_icones_players[objeto[1]][0] += 10
                        elif type(remova) == Alienigina:
                            self.mapa.barra.pontuacoes_icones_players[objeto[1]][0] += 10
                        self.objects.remove(remova)
                object.remover[1].remove(objeto)
            ## Remove objeto caso ele tenha falado para se remover
            if  object.remover[0]:
                self.objects.remove(object)
           
    def desenha(self):
        # Desenha o mapa e depois os objetos
        self.mapa.desenhar(self.tela)
        for object in self.objects:
            object.desenhar(self.tela)
        
        pg.display.flip()
            
    def encerrado(self):
        ## Casos para que o jogo encerre
        
        # Caso o tempo acabe
        if self.tempo_jogo.tempo_passado() > ConfigJogo.TEMPO_PARTIDA:
            return True
        
        # Caso nao tenha mais quartel ou jogadores
        tem_quartel = False
        tem_player = False
        for object in self.objects:
            if type(object) == Player:
                tem_player = True
            elif type(object) == Quartel:
                tem_quartel = True
        if not tem_quartel or not tem_player:
            return True
        else:
            return False
            
    def executar(self):
        ## Loop principal
        while not self.encerrado():
            if self.cronometro.tempo_passado() > ConfigJogo.TEMPO_JOGO:
                self.cronometro.reset()
                self.tratamento()
                self.atualizar()
                self.desenha()
            
        