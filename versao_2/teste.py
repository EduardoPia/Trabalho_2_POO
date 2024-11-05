import pygame
import sys

pygame.init()

# Configuração da janela
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ajuste de Transparência")

# Carregar imagens com transparência
foreground_path = "sprites\enemies\GhostCircle.png"

try:
    foreground = pygame.image.load(foreground_path).convert_alpha()
except pygame.error:
    print("Erro ao carregar a imagem.")
    sys.exit()

# Definir a posição da imagem de primeiro plano
foreground_rect = foreground.get_rect()
foreground_rect.center = (width // 2, height // 2)

# Ajustar a transparência (valor alfa)
alpha_value = 12  # Varia de 0 (totalmente transparente) a 255 (totalmente opaco)
foreground.set_alpha(alpha_value)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 255, 255))  # Preencher a tela com um fundo branco

    # Desenhar a imagem de primeiro plano com transparência ajustada
    screen.blit(foreground, foreground_rect)

    pygame.display.flip()
