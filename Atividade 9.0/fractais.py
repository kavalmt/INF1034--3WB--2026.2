import pygame, math

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Fractais')
clock = pygame.time.Clock()

def desenha_slider(x, y, largura, valor, maximo):
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + largura, y), 4)
    bolinha_x = x + valor * largura // maximo
    pygame.draw.circle(screen, (0, 0, 0), (bolinha_x, y), 10)

def atualiza_slider(x, y, largura, valor, maximo):
    mouse = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if mouse[0] >= x and mouse[0] <= x + largura and mouse[1] > y - 15 and mouse[1] < y + 15:
            valor = (mouse[0] - x) * maximo // largura
    return valor

def desenha_galho(x, y, tamanho, angulo, abertura, nivel):
    if nivel == 0:
        return
    x2 = x + tamanho * math.cos(math.radians(angulo))
    y2 = y - tamanho * math.sin(math.radians(angulo))
    pygame.draw.line(screen, (0, 150, 0), (x, y), (x2, y2), 2)
    desenha_galho(x2, y2, tamanho * 0.6, angulo - abertura, abertura, nivel - 1)
    desenha_galho(x2, y2, tamanho * 0.6, angulo, abertura, nivel - 1)
    desenha_galho(x2, y2, tamanho * 0.6, angulo + abertura, abertura, nivel - 1)

def desenha_triangulo(x, y, tamanho, cor):
    altura = tamanho * 0.87
    pygame.draw.polygon(screen, cor, [(x, y), (x - tamanho / 2, y + altura), (x + tamanho / 2, y + altura)])

def desenha_triangulo_invertido(x, y, tamanho, cor):
    altura = tamanho * 0.87
    pygame.draw.polygon(screen, cor, [(x, y), (x - tamanho / 2, y - altura), (x + tamanho / 2, y - altura)])

def sierpinski(x, y, tamanho, nivel, cor1, cor2):
    if nivel == 0:
        desenha_triangulo(x, y, tamanho, cor1)
        return
    metade = tamanho / 2
    altura = metade * 0.87
    desenha_triangulo_invertido(x, y + altura * 2, metade, cor2)
    sierpinski(x, y, metade, nivel - 1, cor2, cor1)
    sierpinski(x - metade / 2, y + altura, metade, nivel - 1, cor2, cor1)
    sierpinski(x + metade / 2, y + altura, metade, nivel - 1, cor2, cor1)

qtd_circulos = 6
abertura = 30
profundidade = 4

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    clock.tick(60)

    qtd_circulos = atualiza_slider(100, 650, 200, qtd_circulos, 10)
    abertura = atualiza_slider(500, 650, 200, abertura, 90)
    profundidade = atualiza_slider(880, 650, 200, profundidade, 6)

    screen.fill((255, 255, 255))

    for i in range(qtd_circulos):
        pygame.draw.circle(screen, (255, i * 25, 100), (200, 330), 150 - i * 15)

    desenha_galho(600, 600, 130, 90, abertura, 6)

    sierpinski(980, 150, 360, profundidade, (30, 60, 200), (250, 200, 0))

    desenha_slider(100, 650, 200, qtd_circulos, 10)
    desenha_slider(500, 650, 200, abertura, 90)
    desenha_slider(880, 650, 200, profundidade, 6)

    pygame.display.update()

pygame.quit()
