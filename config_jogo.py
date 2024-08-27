## Esse arquivo contém as configurações do jogo

from vetor2d import Vetor2D
import pygame as pg

class ConfigJogo:
    
    ## Informações gerais
    TEMPO_JOGO = 1/300
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
    RELOGIO_IMG = "sprites/map/Relogio.png"
    
    ## Informações player
    PLAYER_SIZE = Vetor2D(0.93*TILE_SIZE.x,0.93*TILE_SIZE.y)
    STOPPED ,UP, DOWN, LEFT, RIGHT = 0,1,-1,2,-2
    PLAYERS_POS = [ARENA_TOP_LEFT+TILE_SIZE, ARENA_TOP_LEFT + Vetor2D((ARENA_TILES.x-2)*TILE_SIZE.x,(ARENA_TILES.y-2)*TILE_SIZE.y)]
    BOMBAS_PLAYER = 4
    PLAYER_IMGS = ["sprites/chars/pacman-black.png","sprites/chars/pacman-white.png"]
    CONTROLS = [[pg.K_w,pg.K_s,pg.K_a,pg.K_d,pg.K_SPACE],[pg.K_UP,pg.K_DOWN,pg.K_LEFT,pg.K_RIGHT,pg.K_KP0]]
    PLAYER_VEL = 0.7
    
    ## Informações bomba
    TEMPO_BOMBA_EXPLOSAO = 2.5
    TEMPO_BOMBA_RECARGA = 0.3
    DIST_EXPLOSAO = 3
    TOLERANCIA_BOMBA = 25
    BOMBA_IMG = "sprites/items/bomba.png"
    
    ## Informações chama
    TEMPO_CHAMA = 0.7
    FOGO_CENT = "sprites/items/Fogo.png"
    FOGO_HOR = "sprites/items/FogoHorizontal.png"
    FOGO_VERT = "sprites/items/FogoVertical.png"
    
    ## Informações do quartel
    IMG_QUARTEL = "sprites/enemies/ship.png"
    AREA_QUARTEL = Vetor2D(4,4)
    SPAWN_QUARTEL = Vetor2D(ARENA_TOP_LEFT.x+(ARENA_TILES.x//2)*TILE_SIZE.x,ARENA_TOP_LEFT.y+(ARENA_TILES.y//2)*TILE_SIZE.y)
    VIDA_QUARTEL = 15
    MAX_FANTASMAS = 4
    MAX_ALIENIGINAS = 4
    TEMPO_SPAWN = 4 
    TEMPO_IMMUNE = TEMPO_CHAMA + 0.1
    
    ## Informações alienigina/fantasma
    IMG_ALIEN = ["sprites/enemies/enemy-alien.png","sprites/enemies/enemy-baby-bearded.png","sprites/enemies/enemy-chamaleon.png","sprites/enemies/enemy-bicudo.png"]
    IMG_GHOST = "sprites/enemies/Ghost.png"
    INIM_VEL = [Vetor2D(PLAYER_VEL/2,0),Vetor2D(-PLAYER_VEL/2,0),Vetor2D(0,PLAYER_VEL/2),Vetor2D(0,-PLAYER_VEL/2)]
    RECARGA_PROJETIL = 3
    CIRCLE_DIAMENTER = 6*TILE_SIZE.x
    SIZE_CIRCLE = Vetor2D(CIRCLE_DIAMENTER,CIRCLE_DIAMENTER)
    IMG_CIRCLE = "sprites/enemies/GhostCircle.png"
    AURAS_FANTASMA = (1/2,2)
    
    ## Informações Projetil
    SIZE_PROJETIL = [Vetor2D(TILE_SIZE.x/2,TILE_SIZE.x/4),Vetor2D(TILE_SIZE.x/2,TILE_SIZE.x/4), \
                    Vetor2D(TILE_SIZE.x/4,TILE_SIZE.x/2),Vetor2D(TILE_SIZE.x/4,TILE_SIZE.x/2)]
    VELO_PROJETIL = [Vetor2D(PLAYER_VEL,0),Vetor2D(-PLAYER_VEL,0),Vetor2D(0,PLAYER_VEL),Vetor2D(0,-PLAYER_VEL)]
    IMG_PROJETIL = ["sprites/enemies/LaserHorizontal.jpg","sprites/enemies/LaserHorizontal.jpg",\
                    "sprites/enemies/LaserVertical.jpg","sprites/enemies/LaserVertical.jpg"]
    
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
    
    ## Informações cena final
    COR_END = (255,255,255)
    GAME_OVER = "sprites/map/GameOver.jpg"
    SIZE_IMG_PLAYER = Vetor2D(PLAYER_SIZE.x*2,PLAYER_SIZE.y*2)
    SIZE_GAMEOVER_WON = Vetor2D(DIM_TELA.x,DIM_TELA.y)
    SIZE_BIG_PLAYER = Vetor2D(PLAYER_SIZE.x*4,PLAYER_SIZE.y*4)
    
    # Posições
    POS_PLAYER1 = Vetor2D(DIM_TELA.x*0.1, DIM_TELA.y*0.05)
    POS_PLAYER2 = Vetor2D(DIM_TELA.x*0.6, DIM_TELA.y*0.05)
    DISTANCE_TO_TXT = Vetor2D(DIM_TELA.x*0.15,DIM_TELA.y*0.05)
    POS_EMPATE = Vetor2D(DIM_TELA.x*0.1,DIM_TELA.y*0.4)
    POS_GANHADOR = Vetor2D(DIM_TELA.x*0.05,DIM_TELA.y*0.4)
    POS_TXT_GANHOU = Vetor2D(DIM_TELA.x*0.3,DIM_TELA.y*0.5)
    
    # Texto
    FONTEEND = pg.font.SysFont(None,60) 
    TEXTO_ENTER = FONTEEND.render("Aperte enter para jogar novamente",False,COR_END)
    POS_TXT_ENTER = Vetor2D(DIM_TELA.x*0.1,DIM_TELA.y*0.9)
    BIGER_FONTEEND = pg.font.SysFont(None,180) 
    TXT_EMPATE = BIGER_FONTEEND.render("EMPATOU!!!",False,COR_END)
    BIG_FONTEEND = pg.font.SysFont(None,150) 
    TXT_GANHOU = BIG_FONTEEND.render("GANHOU!!!",False,COR_END)
    
    
    
    