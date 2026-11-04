import pygame

pygame.init()

LARGURA = 800
ALTURA = 448
TAMANHO = 32
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Atividade 12 - Mapa")
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 26)

tileset = pygame.image.load("Atividade 12.0/assets/tileset.png").convert_alpha()

cortes = {
    "G": (0, 0, 32, 32),
    "T": (32, 0, 32, 32),
    "P": (64, 0, 32, 32),
    "B": (96, 0, 32, 32),
    "F": (128, 0, 32, 32),
    "A": (160, 0, 32, 32),
}
solidos = ["G", "T", "P", "B"]

arquivo = open("Atividade 12.0/mapa.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

tiles = []
paredes = []
for linha in range(len(linhas)):
    texto_linha = linhas[linha].strip()
    for coluna in range(len(texto_linha)):
        letra = texto_linha[coluna]
        if letra in cortes:
            imagem = tileset.subsurface(cortes[letra])
            x = coluna * TAMANHO
            y = linha * TAMANHO
            tiles.append([imagem, x, y])
            if letra in solidos:
                paredes.append(pygame.Rect(x, y, TAMANHO, TAMANHO))

LARGURA_MAPA = len(linhas[0].strip()) * TAMANHO
ALTURA_MAPA = len(linhas) * TAMANHO

folha = pygame.image.load("Atividade 12.0/assets/robo_spritesheet.png").convert_alpha()
correndo_direita = []
correndo_esquerda = []
for i in range(8):
    quadro = folha.subsurface((i * 128, 0, 128, 128))
    quadro = pygame.transform.scale(quadro, (64, 64))
    correndo_direita.append(quadro)
    correndo_esquerda.append(pygame.transform.flip(quadro, True, False))

parado_direita = pygame.transform.scale(folha.subsurface((8 * 128, 0, 128, 128)), (64, 64))
parado_esquerda = pygame.transform.flip(parado_direita, True, False)

pulo_direita = pygame.transform.scale(folha.subsurface((9 * 128, 0, 128, 128)), (64, 64))
pulo_esquerda = pygame.transform.flip(pulo_direita, True, False)

robo = pygame.Rect(64, 300, 28, 54)
robo_vel_y = 0
no_ar = True
olhando_direita = True
indice_robo = 0
camera_x = 0

rodando = True
while rodando:
    relogio.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and no_ar == False:
                robo_vel_y = -16
                no_ar = True

    teclas = pygame.key.get_pressed()
    robo_vel_x = 0
    if teclas[pygame.K_RIGHT]:
        robo_vel_x = 5
        olhando_direita = True
    elif teclas[pygame.K_LEFT]:
        robo_vel_x = -5
        olhando_direita = False

    robo.x = robo.x + robo_vel_x
    for parede in paredes:
        if robo.colliderect(parede):
            if robo_vel_x > 0:
                robo.right = parede.left
            if robo_vel_x < 0:
                robo.left = parede.right

    if robo.left < 0:
        robo.left = 0
    if robo.right > LARGURA_MAPA:
        robo.right = LARGURA_MAPA

    robo_vel_y = robo_vel_y + 1
    if robo_vel_y > 15:
        robo_vel_y = 15
    robo.y = robo.y + robo_vel_y

    no_ar = True
    for parede in paredes:
        if robo.colliderect(parede):
            if robo_vel_y > 0:
                robo.bottom = parede.top
                no_ar = False
            if robo_vel_y < 0:
                robo.top = parede.bottom
            robo_vel_y = 0

    if robo.top > ALTURA_MAPA:
        robo.x = 64
        robo.y = 300
        robo_vel_y = 0

    if no_ar:
        if olhando_direita:
            imagem_robo = pulo_direita
        else:
            imagem_robo = pulo_esquerda
    elif robo_vel_x != 0:
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

    camera_x = robo.centerx - LARGURA // 2
    if camera_x < 0:
        camera_x = 0
    if camera_x > LARGURA_MAPA - LARGURA:
        camera_x = LARGURA_MAPA - LARGURA

    tela.fill((135, 200, 240))

    for tile in tiles:
        tela.blit(tile[0], (tile[1] - camera_x, tile[2]))

    tela.blit(imagem_robo, (robo.x - 18 - camera_x, robo.y - 8))

    texto = fonte.render("Setas: andar   Espaco: pular", True, (0, 0, 0))
    tela.blit(texto, (20, 20))

    pygame.display.update()

pygame.quit()
