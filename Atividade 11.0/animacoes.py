
import pygame
import os

pygame.init()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")


LARGURA = 800
ALTURA = 450

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Atividade - Animacoes")

relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 26)

CHAO = 256


moeda = []

for i in range(1, 9):
    imagem = pygame.image.load(
        os.path.join(ASSETS_DIR, "coin_0" + str(i) + ".png")
    ).convert_alpha()

    moeda.append(imagem)

indice_moeda = 0


folha = pygame.image.load(
    os.path.join(ASSETS_DIR, "robo_spritesheet.png")
).convert_alpha()

correndo_direita = []
correndo_esquerda = []

for i in range(8):
    quadro = folha.subsurface((i * 128, 0, 128, 128))

    correndo_direita.append(quadro)

    correndo_esquerda.append(
        pygame.transform.flip(quadro, True, False)
    )

parado_direita = folha.subsurface((8 * 128, 0, 128, 128))
parado_esquerda = pygame.transform.flip(
    parado_direita, True, False
)

pulo_direita = folha.subsurface((9 * 128, 0, 128, 128))
pulo_esquerda = pygame.transform.flip(
    pulo_direita, True, False
)


robo_x = 350
robo_y = CHAO
robo_vel_y = 0

no_ar = False
olhando_direita = True
indice_robo = 0

heroi = []

for i in range(1, 17):

    if i < 10:
        nome = "Hero_Walk_0" + str(i) + ".png"
    else:
        nome = "Hero_Walk_" + str(i) + ".png"

    imagem = pygame.image.load(
        os.path.join(ASSETS_DIR, nome)
    ).convert_alpha()

    heroi.append(imagem)


heroi_x = 20
heroi_andando = False
indice_heroi = 0


rodando = True

while rodando:

    relogio.tick(60)


    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if heroi_andando == False:
                heroi_andando = True

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE and no_ar == False:
                robo_vel_y = -16
                no_ar = True


    indice_moeda = indice_moeda + 0.2

    if indice_moeda >= len(moeda):
        indice_moeda = 0


    teclas = pygame.key.get_pressed()

    correndo = False

    if teclas[pygame.K_RIGHT]:
        robo_x = robo_x + 5
        olhando_direita = True
        correndo = True

    elif teclas[pygame.K_LEFT]:
        robo_x = robo_x - 5
        olhando_direita = False
        correndo = True


    if robo_x < -20:
        robo_x = -20

    if robo_x > LARGURA - 108:
        robo_x = LARGURA - 108


    robo_vel_y = robo_vel_y + 0.8
    robo_y = robo_y + robo_vel_y

    if robo_y >= CHAO:
        robo_y = CHAO
        robo_vel_y = 0
        no_ar = False

    if no_ar:

        if olhando_direita:
            imagem_robo = pulo_direita
        else:
            imagem_robo = pulo_esquerda

    elif correndo:

        indice_robo = indice_robo + 0.3

        if indice_robo >= len(correndo_direita):
            indice_robo = 0

        if olhando_direita:
            imagem_robo = correndo_direita[int(indice_robo)]
        else:
            imagem_robo = correndo_esquerda[int(indice_robo)]

    else:

        indice_robo = 0

        if olhando_direita:
            imagem_robo = parado_direita
        else:
            imagem_robo = parado_esquerda


    if heroi_andando:

        heroi_x = heroi_x + 3

        indice_heroi = indice_heroi + 0.3

        if indice_heroi >= len(heroi):
            indice_heroi = 0

        if heroi_x > LARGURA:
            heroi_x = 20
            heroi_andando = False
            indice_heroi = 0


    tela.fill((120, 180, 230))

    pygame.draw.rect(
        tela,
        (70, 150, 70),
        (0, 380, LARGURA, 70)
    )

    tela.blit(moeda[int(indice_moeda)], (700, 40))

    tela.blit(
        heroi[int(indice_heroi)],
        (heroi_x, CHAO)
    )

    tela.blit(imagem_robo, (robo_x, robo_y))

    texto = fonte.render(
        "Setas: correr   Espaco: pular   Clique: heroi atravessa",
        True,
        (0, 0, 0)
    )

    tela.blit(texto, (20, 20))

    pygame.display.update()

pygame.quit()
