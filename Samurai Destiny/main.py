import pygame

pygame.init()

# tela
LARGURA = 1920
ALTURA = 1080
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Samurai Destiny")
relogio = pygame.time.Clock()

#fundo
fundo = pygame.image.load("Samurai Destiny/Fundo/fundo_dia.png").convert()

# sprite samurai cada quadro
TAMANHO_QUADRO = 96
# aumentei o samurai em 3 vzs
ESCALA = 3


# lista de recorte com os sprites e sheets ( 10 cortes , 960/96 = 10)
def cortar_quadros(caminho):
    imagem = pygame.image.load(caminho).convert_alpha()
    # descubro quantos quadros tem dividindo a largura da imagem por 96
    quantidade = imagem.get_width() // TAMANHO_QUADRO
    quadros = []
    for i in range(quantidade):
        x = i * TAMANHO_QUADRO
        #reCORTO CADA UM QUADRO E GUARDO NUMA LISTA (subsurface)
        quadro = imagem.subsurface((x, 0, TAMANHO_QUADRO, TAMANHO_QUADRO))
        # reajuste do quadro para o tamanho da tela 
        quadro = pygame.transform.scale(quadro, (TAMANHO_QUADRO * ESCALA, TAMANHO_QUADRO * ESCALA))
        quadros.append(quadro)
    return quadros


#animacoes 
parado = cortar_quadros("Samurai Destiny/Samurai/IDLE.png")
correndo = cortar_quadros("Samurai Destiny/Samurai/RUN.png")

# Posicao do samurai na tela
samurai_x = 800
samurai_y = 720          # se ele ficar flutuando ou afundado no chao, ajusto esse numero
velocidade = 8           # quantos pixels ele anda a cada volta do loop
olhando_direita = True   # para saber se preciso espelhar a imagem

# Controle da animacao
animacao = parado        # qual lista de quadros esta sendo mostrada
quadro_atual = 0         # qual quadro da lista aparece agora
contador = 0             # conta as voltas do loop para trocar de quadro

#Jogo em si 
rodando = True
while rodando:

    # Esq = fechar janela
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False

    # teclas apertadas A D 
    teclas = pygame.key.get_pressed()
    andando = False

    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        samurai_x = samurai_x - velocidade
        olhando_direita = False
        andando = True

    elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        samurai_x = samurai_x + velocidade
        olhando_direita = True
        andando = True

    # limitar a tela
    if samurai_x < 0:
        samurai_x = 0
    if samurai_x > LARGURA - TAMANHO_QUADRO * ESCALA:
        samurai_x = LARGURA - TAMANHO_QUADRO * ESCALA

    # ANIMACAO: escolho a animacao certa
    if andando:
        nova_animacao = correndo
    else:
        nova_animacao = parado
    # Se mudou de animacao, comeco do primeiro quadro
    if nova_animacao != animacao:
        animacao = nova_animacao
        quadro_atual = 0
        contador = 0
    # A cada 5 voltas do loop passo para o proximo quadro
    contador = contador + 1
    if contador >= 5:
        contador = 0
        quadro_atual = quadro_atual + 1
        if quadro_atual >= len(animacao):
            quadro_atual = 0
            
    # desenho do fundo primeiro dps o samurai
    tela.blit(fundo, (0, 0))
    imagem_samurai = animacao[quadro_atual]
    if not olhando_direita:
        # Espelho a imagem para ele olhar para a esquerda
        imagem_samurai = pygame.transform.flip(imagem_samurai, True, False)
    tela.blit(imagem_samurai, (samurai_x, samurai_y))

    pygame.display.update()
    relogio.tick(60)   # o jogo roda a 60 quadros por segundo

pygame.quit()