from vetor2d import Vetor2D

class ConfigJogo:
    DIM_TELA = Vetor2D(900, 1100)
    BAR_SIZE = Vetor2D(DIM_TELA.x,100)
    ARENA_TILES = Vetor2D(15,13) # area with players and destructable tiles plus a layer of indestructable tiles
    TILES_AREA = Vetor2D(DIM_TELA.x,DIM_TELA.y-BAR_SIZE.y)
    ARENA_AREA = Vetor2D(min(TILES_AREA.x/ARENA_TILES.x,TILES_AREA.y/ARENA_TILES.y)*ARENA_TILES.x,min(TILES_AREA.x/ARENA_TILES.x,TILES_AREA.y/ARENA_TILES.y)*ARENA_TILES.y)
    ARENA_CENTER = Vetor2D(TILES_AREA.x/2,TILES_AREA.y/2+BAR_SIZE.y)
    ARENA_TOP_LEFT = Vetor2D(ARENA_CENTER.x-ARENA_AREA.x/2,ARENA_CENTER.y-ARENA_AREA.y/2)
    TILE_SIZE = Vetor2D(ARENA_AREA.x/ARENA_TILES.x,ARENA_AREA.x/ARENA_TILES.x) 
    



