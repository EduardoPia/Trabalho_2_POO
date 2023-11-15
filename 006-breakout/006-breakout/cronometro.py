
from time import time

class Cronometro:
    def __init__(self):
        self.reset()

    def reset(self):
        self.total = 0
        self.tempo_referencia = time()
    
    def atualizar_tempo_passado(self):
        tempo_atual = time()
        dt = tempo_atual - self.tempo_referencia
        self.total += dt
        self.tempo_referencia = tempo_atual 
    
    def tempo_passado(self):
        self.atualizar_tempo_passado()
        return self.total
