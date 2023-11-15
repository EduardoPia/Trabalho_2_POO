
from vetor2d import Vetor2D

class ConfigJogo:
    DIM_TELA = Vetor2D(700, 700)
    VELOCIDADE_BOLA = 0.2
    VELOCIDADE_BARRAS = 1.25
    DIM_BARRA_JOGADOR = Vetor2D(0.15 * DIM_TELA.x, 0.01 * DIM_TELA.y)
    DIM_BARRA_MURO = Vetor2D(0.07 * DIM_TELA.x, 0.05 * DIM_TELA.y)
    RAIO_BOLA = (0.02 * DIM_TELA.y)
    ALTURA_PLACAR = 0.1 * DIM_TELA.y
    ALTURA_TEMPO = 0.15 * DIM_TELA.y
    DURACAO_PARTIDA = 60
    FONTE_TITULO = 72
    FONTE_SUBTITULO = 36
    POSICAO_INICIAL_BOLA = Vetor2D(
        DIM_TELA.x // 2, 
        DIM_TELA.y * 0.5
    )
