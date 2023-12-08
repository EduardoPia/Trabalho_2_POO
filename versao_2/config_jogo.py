## Esse arquivo contém as configurações do jogo

from vetor2d import Vetor2D
import pygame as pg

class ConfigJogo:
    
    ## Informações gerais
    TEMPO_JOGO = 1/500
    TEMPO_PARTIDA = 120
    
    ## Informações mapa
    ARENA_TILES = Vetor2D(15,13) # area with players and destructable tiles plus a layer of indestructable tiles
    PROBABILITY_EMPTY = 0.3
    INDESTRUCTABLE, DESTRUCTABLE, EMPTY = 1,2,3
    IMG_GRAMA = "sprites/map/grama.png"
    IMG_INDESTRUCTABLE = "sprites/map/parede-fixa.png"
    IMG_DESTRUCTABLE ="sprites/map/parede-destruivel.png"
    COR_FUNDO = (100, 100, 100)

    ## Dimensões e posições gerais
    DIM_TELA = Vetor2D(900, 800)
    BAR_SIZE = Vetor2D(DIM_TELA.x,100)
    TILES_AREA = Vetor2D(DIM_TELA.x,DIM_TELA.y-BAR_SIZE.y)
    ARENA_AREA = Vetor2D(min(TILES_AREA.x/ARENA_TILES.x,TILES_AREA.y/ARENA_TILES.y)*ARENA_TILES.x,min(TILES_AREA.x/ARENA_TILES.x,TILES_AREA.y/ARENA_TILES.y)*ARENA_TILES.y)
    TILE_SIZE = Vetor2D(ARENA_AREA.x/ARENA_TILES.x,ARENA_AREA.x/ARENA_TILES.x) 
    
    ARENA_CENTER = Vetor2D(TILES_AREA.x/2,TILES_AREA.y/2+BAR_SIZE.y)
    ARENA_TOP_LEFT = Vetor2D(ARENA_CENTER.x-ARENA_AREA.x/2,ARENA_CENTER.y-ARENA_AREA.y/2)
    
    ## Informações barra
    TOUGHNESS_BAR = Vetor2D(0.01,0.05)
    TAM_ICONES_BARRA = Vetor2D(BAR_SIZE.y/1.7,BAR_SIZE.y/1.7)
    POS_RELOGIO = Vetor2D(0.05*BAR_SIZE.x,BAR_SIZE.y/2-TAM_ICONES_BARRA.y/2)
    POS_ICONES_PLAYERS = [Vetor2D(0.30*BAR_SIZE.x,BAR_SIZE.y/2-TAM_ICONES_BARRA.y/2) \
                          ,Vetor2D(0.45*BAR_SIZE.x,BAR_SIZE.y/2-TAM_ICONES_BARRA.y/2)]
    
    ## Informações player
    PLAYER_SIZE = Vetor2D(0.98*TILE_SIZE.x,0.98*TILE_SIZE.y)
    STOPPED ,UP, DOWN, LEFT, RIGHT = 0,1,-1,2,-2
    PLAYERS_POS = [ARENA_TOP_LEFT+TILE_SIZE, ARENA_TOP_LEFT + Vetor2D((ARENA_TILES.x-2)*TILE_SIZE.x,(ARENA_TILES.y-2)*TILE_SIZE.y)]
    BOMBAS_PLAYER = 4
    PLAYER_IMGS = ["sprites/chars/pacman-black.png","sprites/chars/pacman-white.png"]
    CONTROLS = [[pg.K_w,pg.K_s,pg.K_a,pg.K_d,pg.K_SPACE],[pg.K_UP,pg.K_DOWN,pg.K_LEFT,pg.K_RIGHT,pg.K_KP0]]
    
    ## Informações bomba
    TEMPO_BOMBA_EXPLOSAO = 2
    TEMPO_BOMBA_RECARGA = 0.2
    DIST_EXPLOSAO = 3
    TOLERANCIA_BOMBA = 10
    
    ## Informações chama
    TEMPO_CHAMA = 1
    
    ## Informações cena inicial
    COR = (0,0,0)
    TITLE_SIZE = Vetor2D(.94*DIM_TELA.x,0.2*DIM_TELA.y)
    TITLE_POS = Vetor2D((DIM_TELA.x-TITLE_SIZE.x)/2, (.025*DIM_TELA.y+0.025*TITLE_SIZE.y))
    POS_TXT1_INIT = Vetor2D(450,400)
    POS_TXT2_INIT = Vetor2D(450,500)
    POS_PERS1_INIT= Vetor2D(POS_TXT1_INIT.x-1.95*PLAYER_SIZE.x,POS_TXT1_INIT.y)
    POS_PERS2_INIT = Vetor2D(POS_TXT2_INIT.x-1.3*PLAYER_SIZE.x,POS_TXT2_INIT.y)
    POS_PERS3_INIT = Vetor2D(POS_TXT2_INIT.x-2.6*PLAYER_SIZE.x,POS_TXT2_INIT.y)
    pg.font.init()      
    fontesys=pg.font.SysFont(None,80) 
    TEXTO1 = fontesys.render('1 Player',False,COR)
    TEXTO2 = fontesys.render('2 Players',True,COR)
    
    
    