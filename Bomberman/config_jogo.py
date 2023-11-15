from vetor2d import Vetor2D

class ConfigJogo:
    DIM_TELA = Vetor2D(900, 1000)
    TOTAL_TILES = Vetor2D(22,21)
    ARENA_TILES = Vetor2D(20,20) # number of tiles the arena has, not including the indestructible area
    UMBREAKABLE_TILES = Vetor2D(TOTAL_TILES.x-ARENA_TILES.x,TOTAL_TILES.y-ARENA_TILES.y) # number of indestructible tiles to the left/right, and number for top/bottom
    TILE_SIZE = Vetor2D(DIM_TELA.x/TOTAL_TILES.x, DIM_TELA.y/TOTAL_TILES.y)



