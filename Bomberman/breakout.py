
import sys
import random 
import pygame as pg
from time import time 
from typing import Tuple, List

from bola import Bola
from barra import Barra
from vetor2d import Vetor2D
from cronometro import Cronometro
from config_jogo import ConfigJogo


class Breakout:
    def __init__(self):
        pg.init()

        self.tela = pg.display.set_mode((
            ConfigJogo.DIM_TELA.x,
            ConfigJogo.DIM_TELA.y
        ))
        
        # salvamos a fonte para nao precisar criar ela toda hora
        self.font = pg.font.SysFont(None, 48)
        
        # cronometro para medir o tempo de jogo
        self.cronometro = Cronometro()
        
        self.n_vidas = 10
        self.pontuacao = 0 
        
        self.muro: List[Barra] = []
        
        self.cria_barra()
        self.cria_muro()
        self.cria_bola()
        
        self.instante_ultima_colisao = 0

    def cria_barra(self):
        py = ConfigJogo.DIM_TELA.y * 0.9 - ConfigJogo.DIM_BARRA_JOGADOR.y 
        px = ConfigJogo.DIM_TELA.x // 2 - ConfigJogo.DIM_BARRA_JOGADOR.x // 2
        self.barra = Barra(posicao=Vetor2D(px, py), tamanho=ConfigJogo.DIM_BARRA_JOGADOR, cor=(255,69,0))

    def cria_muro(self):
        nx = int(ConfigJogo.DIM_TELA.x // ConfigJogo.DIM_BARRA_MURO.x)
        ny = 5 
        
        displacement_x = (ConfigJogo.DIM_TELA.x - nx * ConfigJogo.DIM_BARRA_MURO.x) // 2
        displacement_y = (ConfigJogo.DIM_TELA.y * 0.1)
        
        colors = ((255, 0, 0), # red
                    (255,165, 0), # 'orange', 
                    (255, 255, 0), # 'yellow', 
                    (0, 255, 0), # 'green', 
                    (0, 0, 255), # 'blue'
                    )

        self.muro = []
        for row_idx in range(ny):
            for col_idx in range(nx):
                px = col_idx * ConfigJogo.DIM_BARRA_MURO.x + displacement_x
                py = row_idx * ConfigJogo.DIM_BARRA_MURO.y + displacement_y
                self.muro.append(
                    Barra(
                        posicao=Vetor2D(px, py),
                        tamanho=ConfigJogo.DIM_BARRA_MURO,
                        cor=colors[row_idx]
                    )
                )

    def cria_bola(self):
        posicao = ConfigJogo.POSICAO_INICIAL_BOLA

        velocidade = Vetor2D(
            random.choice([-1, 1]) * ConfigJogo.VELOCIDADE_BOLA,
            ConfigJogo.VELOCIDADE_BOLA,
        )
        
        self.bola = Bola(
            posicao=posicao, 
            raio=ConfigJogo.RAIO_BOLA, 
            cor=(255, 69, 0),
            velocidade=velocidade
        ) 

    def encerrada(self):
        return (self.cronometro.tempo_passado() > ConfigJogo.DURACAO_PARTIDA) or \
                (self.n_vidas <= 0)

    def executar(self):
        while True:
            self.tratamento_eventos()
            
            if not self.encerrada():
                self.atualiza_estado()
            
            self.desenha()

    def tratamento_eventos(self):
        pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
        
        # controle da barra 
        if pg.key.get_pressed()[pg.K_a]:
            self.barra.velocidade = Vetor2D(-ConfigJogo.VELOCIDADE_BARRAS, 0)
        elif pg.key.get_pressed()[pg.K_d]:
            self.barra.velocidade = Vetor2D(ConfigJogo.VELOCIDADE_BARRAS, 0)
        else:
            self.barra.velocidade = Vetor2D(0, 0)

    def atualiza_estado(self):
        self.bola.atualizar()
        self.barra.atualizar()
        self.trata_colisoes()
        self.trata_bola_fora_tela()

    def trata_colisoes(self):
        if time() - self.instante_ultima_colisao < 0.3:
            return
        
        if self.circ_rect_collision(self.bola, self.barra):
            self.bola.velocidade.y = -self.bola.velocidade.y
            self.instante_ultima_colisao = time()

        for idx in range(len(self.muro)):
            pedra = self.muro[idx]
            if self.circ_rect_collision(self.bola, pedra):
                self.bola.velocidade.y = -self.bola.velocidade.y
                self.muro.pop(idx)
                self.pontuacao += 1
                self.instante_ultima_colisao = time()
                break

    def trata_bola_fora_tela(self):
        if self.bola.posicao.y > ConfigJogo.DIM_TELA.y:
            self.n_vidas -= 1
            self.bola.posicao = ConfigJogo.POSICAO_INICIAL_BOLA
            return

        if (self.bola.posicao.x + self.bola.raio > \
            ConfigJogo.DIM_TELA.x) or \
                (self.bola.posicao.x - self.bola.raio < 0):
            self.bola.velocidade.x = -self.bola.velocidade.x

        if (self.bola.posicao.y - self.bola.raio < 0):
            self.bola.velocidade.y = -self.bola.velocidade.y
        
    def desenha(self):
        self.tela.fill((0, 0, 0))
        
        for pedra in self.muro:
            pedra.desenha(self.tela)
        
        self.bola.desenha(self.tela)
        self.barra.desenha(self.tela)
        self.desenha_pontuacao(self.tela)
        self.desenha_tempo(self.tela)
        self.desenha_vidas(self.tela)
        
        pg.display.flip()

    def desenha_pontuacao(self, tela: pg.Surface):
        img = self.font.render(f'{self.pontuacao:03d}',
                                True, (255, 255, 255))
        px = ConfigJogo.DIM_TELA.x * 0.85
        py = ConfigJogo.DIM_TELA.y * 0.02
        tela.blit(img, (px, py))

    def desenha_vidas(self, tela: pg.Surface):
        img = self.font.render(f'{self.n_vidas}',
                                True, (255, 255, 255))
        px = ConfigJogo.DIM_TELA.x * 0.7
        py = ConfigJogo.DIM_TELA.y * 0.02
        tela.blit(img, (px, py))
        
        if self.encerrada():
            img = self.font.render(f'** FIM **', True, (255, 255, 255))
            px = ConfigJogo.DIM_TELA.x // 2 - img.get_width() // 2
            py = ConfigJogo.DIM_TELA.y * 0.7
            tela.blit(img, (px, py))
            
    def desenha_tempo(self, tela: pg.Surface):
        tempo = ConfigJogo.DURACAO_PARTIDA - self.cronometro.tempo_passado()
        img = self.font.render(f'{tempo:.0f}',
                                True, (255, 255, 255))
        px = ConfigJogo.DIM_TELA.x * 0.1
        py = ConfigJogo.DIM_TELA.y * 0.02
        tela.blit(img, (px, py))
    
    def circ_rect_collision(self,
                            bola: Bola,
                            barra: Barra) -> bool:
        c_px, c_py = bola.posicao.x, bola.posicao.y
        r_px, r_py, r_larg, r_alt = barra.rect()
        DeltaX = c_px - max(r_px, min(c_px, r_px + r_larg))
        DeltaY = c_py - max(r_py, min(c_py, r_py + r_alt))
        return (DeltaX * DeltaX + DeltaY * DeltaY) < (bola.raio * bola.raio)
