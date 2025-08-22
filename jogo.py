import pygame
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 1280, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Primeiro Jogo")

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Jogador (um quadrado)
jogador = pygame.Rect(100, 100, 50, 50)  # posição x,y e tamanho
velocidade = 5

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentação com teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador.x -= velocidade
    if teclas[pygame.K_RIGHT]:
        jogador.x += velocidade
    if teclas[pygame.K_UP]:
        jogador.y -= velocidade
    if teclas[pygame.K_DOWN]:
        jogador.y += velocidade

    # Preencher a tela
    tela.fill(BRANCO)

    # Desenhar o jogador
    pygame.draw.rect(tela, AZUL, jogador)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar FPS
    pygame.time.Clock().tick(60)

