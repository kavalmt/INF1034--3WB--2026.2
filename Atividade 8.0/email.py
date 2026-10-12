import pygame
from random import choice


def valida_email(email):
    return email[-8:] == "@puc.com"

def possui_maiuscula(senha):
    for carac in senha:
        if 'A' <= carac <= 'Z':
            return True
    return False

def possui_minuscula(senha):
    for carac in senha:
        if 'a' <= carac <= 'z':
            return True
    return False

def possui_numero(senha):
    for carac in senha:
        if carac.isnumeric():
            return True
    return False

def valida_senha(senha):
    if len(senha) < 8:
        return False
    if not possui_maiuscula(senha):
        return False
    if not possui_minuscula(senha):
        return False
    if not possui_numero(senha):
        return False

    return True

def criptografa(senha):
    senha_cripto = ""
    for carac in senha:
        if '0' <= carac <= 'z':
            pos = ord(carac) - ord('0')
            pos = (pos + 3) % 75
            senha_cripto += chr(pos + ord('0'))
    return senha_cripto

def descriptografa(senha_cripto):
    senha = ""
    for carac in senha_cripto:
        if '0' <= carac <= 'z':
            pos = ord(carac) - ord('0')
            pos = (pos - 3) % 75
            senha += chr(pos + ord('0'))
    return senha

palavras = ["banana", "maça", "abacaxi", "limao", "mamao", "pera", "melancia", "uva"]
alfabeto = 'abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ'

def sortear_palavra():
    return choice(palavras)

def escrever_forca(texto, y, cor):
    screen.blit(fonte_forca.render(texto, True, cor), (50, y))

opcoes = ["pedra", "papel", "tesoura"]

def jogada_computador():
    return choice(opcoes)

def quem_ganhou(jogador, computador):
    if jogador == computador:
        return "empate"
    if (jogador == "pedra" and computador == "tesoura") or (jogador == "tesoura" and computador == "papel") or (jogador == "papel" and computador == "pedra"):
        return "jogador"
    return "computador"

def imagem_da_jogada(jogada):
    if jogada == "pedra":
        return imagem_pedra
    if jogada == "papel":
        return imagem_papel
    return imagem_tesoura

def escrever_ppt(texto, x, y):
    screen.blit(fonte_ppt.render(texto, True, (255, 255, 255)), (x, y))

print(valida_email("aluno@puc.com"))
print(valida_email("aluno@gmail.com"))
print(valida_senha("Senha123"))
print(valida_senha("senha123"))
print(criptografa("Senha123"))
print(descriptografa("Vhqkd456"))

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()

tela = "email"
input_string = ""
email = ""
senha_cripto = ""
senha_decripto = ""
mensagem = ""
cor_mensagem = "red"

fonte = pygame.font.Font(size=50)
fonte_validation = pygame.font.Font(size=25)

fonte_coringa = pygame.font.Font("Atividade 6.0/fontecoringa.otf", 40)
imagem_coringa = pygame.image.load("Atividade 6.0/coringa.png")
imagem_coringa = pygame.transform.scale(imagem_coringa, (180, 180))
pygame.mixer.music.load("Atividade 6.0/gotham.mp3")

sfx_manha = pygame.mixer.Sound("Atividade 6.0/manha.mp3")
sfx_tarde = pygame.mixer.Sound("Atividade 6.0/tarde.mp3")
sfx_noite = pygame.mixer.Sound("Atividade 6.0/gotham.mp3")
canal_sfx = pygame.mixer.Channel(0)

texto_coringa = "Why so serious ?"

sol_x = 130
sol_y = 130
sol_raio = 70
sol_vel = 250
sol_limite = 110

nuvem_x = 850
nuvem_y = 150
nuvem_vel = 120
nuvem_dir = 1
nuvem_borda_esq = 45
nuvem_borda_dir = 215

casa_x = 500
casa_largura = 260
casa_altura = 200
casa_y = 600 - casa_altura
arvore_x = 980
arvore_tronco_altura = 120
arvore_y = 600 - 60 - arvore_tronco_altura
cor_manha = (255, 200, 150)
cor_tarde = (135, 206, 235)
cor_noite = (15, 15, 60)

fonte_forca = pygame.font.SysFont(None, 50)
vidas = 6
palavra_aleatoria = sortear_palavra()
palavra_oculta = ["_"] * len(palavra_aleatoria)
letra = ""
mensagem_forca = "Digite uma letra e aperte ENTER"
acabou_forca = False

fonte_ppt = pygame.font.SysFont(None, 40)
imagem_pedra = pygame.image.load("Atividade 7.0/pedra.png")
imagem_papel = pygame.image.load("Atividade 7.0/papel.png")
imagem_tesoura = pygame.image.load("Atividade 7.0/tesoura.png")
pontos_jogador = 0
pontos_computador = 0
jogador = ""
computador = ""
mensagem_ppt = "Escolha a sua jogada"
acabou_ppt = False

while running:
    clock.tick(60)
    dt = clock.get_time() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if tela == "email":
                if event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]
                elif event.key == pygame.K_RETURN:
                    if valida_email(input_string):
                        email = input_string
                        input_string = ""
                        tela = "senha"
                        mensagem = "E-mail válido! Agora digite a senha."
                        cor_mensagem = "green"
                    else:
                        mensagem = "O seu e-mail não é válido. Digite novamente!"
                        cor_mensagem = "red"
                else:
                    input_string += event.unicode

            elif tela == "senha":
                if event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]
                elif event.key == pygame.K_RETURN:
                    if valida_senha(input_string):
                        senha_cripto = criptografa(input_string)
                        senha_decripto = descriptografa(senha_cripto)
                        tela = "menu"
                    else:
                        mensagem = "Senha fraca! Precisa de 8 caracteres, maiúscula, minúscula e número."
                        cor_mensagem = "red"
                else:
                    input_string += event.unicode

            elif tela == "menu":
                if event.unicode == "1":
                    tela = "casinha"
                    pygame.mixer.music.play(-1)
                elif event.unicode == "2":
                    tela = "forca"
                elif event.unicode == "3":
                    tela = "ppt"

            elif event.key == pygame.K_ESCAPE:
                if tela == "casinha":
                    pygame.mixer.music.stop()
                    canal_sfx.stop()
                tela = "menu"

            elif tela == "forca":
                if acabou_forca == True:
                    if event.key == pygame.K_n:
                        tela = "menu"
                    if event.key == pygame.K_s:
                        vidas = 6
                        palavra_aleatoria = sortear_palavra()
                        palavra_oculta = ["_"] * len(palavra_aleatoria)
                        letra = ""
                        mensagem_forca = "Digite uma letra e aperte ENTER"
                        acabou_forca = False
                elif event.key == pygame.K_BACKSPACE:
                    letra = ""
                elif event.key == pygame.K_RETURN:
                    if letra == "":
                        mensagem_forca = "Apenas permitido LETRAS"
                    elif letra == palavra_aleatoria:
                        palavra_oculta = list(palavra_aleatoria)
                    elif len(letra) == 1 and letra in palavra_aleatoria:
                        mensagem_forca = "Acertou!"
                        for i in range(len(palavra_aleatoria)):
                            if letra == palavra_aleatoria[i]:
                                palavra_oculta[i] = letra
                    else:
                        vidas = vidas - 1
                        mensagem_forca = f"Errou!, Voce perdeu um membro resta apenas: {vidas}"
                    letra = ""
                    if vidas == 0:
                        mensagem_forca = "FIM DE JOGO ! Jogar de novo? (S/N)"
                        acabou_forca = True
                    if "_" not in palavra_oculta:
                        mensagem_forca = "Você acertou a palavra! Jogar de novo? (S/N)"
                        acabou_forca = True
                elif event.unicode != "" and event.unicode in alfabeto:
                    letra = letra + event.unicode.lower()
                elif event.unicode != "":
                    mensagem_forca = "Apenas permitido LETRAS"

            elif tela == "ppt":
                if acabou_ppt == True:
                    if event.key == pygame.K_n:
                        tela = "menu"
                    if event.key == pygame.K_s:
                        jogador = ""
                        computador = ""
                        mensagem_ppt = "Escolha a sua jogada"
                        acabou_ppt = False
                else:
                    escolha = ""
                    if event.key == pygame.K_1:
                        escolha = "pedra"
                    elif event.key == pygame.K_2:
                        escolha = "papel"
                    elif event.key == pygame.K_3:
                        escolha = "tesoura"
                    if escolha != "":
                        jogador = escolha
                        computador = jogada_computador()
                        resultado = quem_ganhou(jogador, computador)
                        if resultado == "empate":
                            mensagem_ppt = "Empate! Quer jogar de novo? (S/N)"
                        elif resultado == "jogador":
                            pontos_jogador = pontos_jogador + 1
                            mensagem_ppt = "Voce ganhou! Quer jogar de novo? (S/N)"
                        else:
                            pontos_computador = pontos_computador + 1
                            mensagem_ppt = "Voce perdeu! Quer jogar de novo? (S/N)"
                        acabou_ppt = True

        if tela == "casinha":
            if event.type == pygame.MOUSEMOTION:
                sol_x, sol_y = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                faixa = (720 - 2 * sol_limite) / 3
                if sol_y < sol_limite + faixa:
                    canal_sfx.play(sfx_manha)
                elif sol_y < sol_limite + 2 * faixa:
                    canal_sfx.play(sfx_tarde)
                else:
                    canal_sfx.play(sfx_noite)

    if tela == "email":
        screen.fill("white")
        texto = fonte_validation.render("Digite o e-mail e aperte Enter:", True, "black")
        screen.blit(texto, (100, 70))
        pygame.draw.rect(screen, "black", (100, 100, 500, 50), 3)
        input_text = fonte.render(input_string, True, "#000000")
        screen.blit(input_text, (120, 105))
        valid_text = fonte_validation.render(mensagem, True, cor_mensagem)
        screen.blit(valid_text, (120, 180))

    elif tela == "senha":
        screen.fill("white")
        texto = fonte_validation.render("E-mail: " + email, True, "black")
        screen.blit(texto, (100, 40))
        texto = fonte_validation.render("Digite a senha e aperte Enter:", True, "black")
        screen.blit(texto, (100, 70))
        pygame.draw.rect(screen, "black", (100, 100, 500, 50), 3)
        input_text = fonte.render(input_string, True, "#000000")
        screen.blit(input_text, (120, 105))
        valid_text = fonte_validation.render(mensagem, True, cor_mensagem)
        screen.blit(valid_text, (120, 180))

    elif tela == "menu":
        screen.fill("white")
        texto = fonte.render("Menu - digite o número do projeto", True, "black")
        screen.blit(texto, (100, 60))
        texto = fonte.render("1 - Casinha", True, "black")
        screen.blit(texto, (100, 150))
        texto = fonte.render("2 - Jogo da forca", True, "black")
        screen.blit(texto, (100, 220))
        texto = fonte.render("3 - Pedra, papel e tesoura", True, "black")
        screen.blit(texto, (100, 290))
        texto = fonte_validation.render("Senha criptografada: " + senha_cripto, True, "blue")
        screen.blit(texto, (100, 450))
        texto = fonte_validation.render("Senha descriptografada: " + senha_decripto, True, "blue")
        screen.blit(texto, (100, 490))

    elif tela == "casinha":
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            sol_x = sol_x - sol_vel * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            sol_x = sol_x + sol_vel * dt
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            sol_y = sol_y - sol_vel * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            sol_y = sol_y + sol_vel * dt

        if sol_x < sol_limite:
            sol_x = sol_limite
        elif sol_x > 1280 - sol_limite:
            sol_x = 1280 - sol_limite
        if sol_y < sol_limite:
            sol_y = sol_limite
        elif sol_y > 720 - sol_limite:
            sol_y = 720 - sol_limite

        nuvem_x = nuvem_x + nuvem_vel * nuvem_dir * dt
        if nuvem_x + nuvem_borda_dir >= 1280:
            nuvem_x = 1280 - nuvem_borda_dir
            nuvem_dir = -1
        elif nuvem_x - nuvem_borda_esq <= 0:
            nuvem_x = nuvem_borda_esq
            nuvem_dir = 1

        meio_tela = 720 / 2
        if sol_y <= meio_tela:
            t = (sol_y - sol_limite) / (meio_tela - sol_limite)
            if t < 0:
                t = 0
            elif t > 1:
                t = 1
            r = cor_manha[0] + (cor_tarde[0] - cor_manha[0]) * t
            g = cor_manha[1] + (cor_tarde[1] - cor_manha[1]) * t
            b = cor_manha[2] + (cor_tarde[2] - cor_manha[2]) * t
        else:
            t = (sol_y - meio_tela) / (720 - sol_limite - meio_tela)
            if t < 0:
                t = 0
            elif t > 1:
                t = 1
            r = cor_tarde[0] + (cor_noite[0] - cor_tarde[0]) * t
            g = cor_tarde[1] + (cor_noite[1] - cor_tarde[1]) * t
            b = cor_tarde[2] + (cor_noite[2] - cor_tarde[2]) * t

        background_color = (int(r), int(g), int(b))

        screen.fill(background_color)
        pygame.draw.rect(screen, "#4CAF50", (0, 600, 1280, 120))

        pygame.draw.circle(screen, "#FFD93D", (sol_x, sol_y), sol_raio)

        pygame.draw.line(screen, "#FFD93D", (sol_x, sol_y - 110), (sol_x, sol_y - 80), 6)
        pygame.draw.line(screen, "#FFD93D", (sol_x, sol_y + 110), (sol_x, sol_y + 80), 6)
        pygame.draw.line(screen, "#FFD93D", (sol_x - 110, sol_y), (sol_x - 80, sol_y), 6)
        pygame.draw.line(screen, "#FFD93D", (sol_x + 110, sol_y), (sol_x + 80, sol_y), 6)
        pygame.draw.line(screen, "#FFD93D", (sol_x - 78, sol_y - 78), (sol_x - 56, sol_y - 56), 6)
        pygame.draw.line(screen, "#FFD93D", (sol_x + 78, sol_y - 78), (sol_x + 56, sol_y - 56), 6)
        pygame.draw.line(screen, "#FFD93D", (sol_x - 78, sol_y + 78), (sol_x - 56, sol_y + 56), 6)
        pygame.draw.line(screen, "#FFD93D", (sol_x + 78, sol_y + 78), (sol_x + 56, sol_y + 56), 6)

        pygame.draw.circle(screen, "#FFFFFF", (nuvem_x, nuvem_y), 45)
        pygame.draw.circle(screen, "#FFFFFF", (nuvem_x + 55, nuvem_y - 15), 55)
        pygame.draw.circle(screen, "#FFFFFF", (nuvem_x + 120, nuvem_y), 50)
        pygame.draw.circle(screen, "#FFFFFF", (nuvem_x + 175, nuvem_y + 10), 40)

        pygame.draw.rect(screen, "#5C3A21", (arvore_x, arvore_y + 60, 30, arvore_tronco_altura))
        pygame.draw.circle(screen, "#2E8B57", (arvore_x + 15, arvore_y), 80)

        pygame.draw.polygon(screen, "#6A0DAD", [
            (casa_x - 40, casa_y),
            (casa_x + casa_largura + 40, casa_y),
            (casa_x + casa_largura / 2, casa_y - 150)])
        pygame.draw.rect(screen, "#3B3B3B", (casa_x, casa_y, casa_largura, casa_altura))
        pygame.draw.rect(screen, "#1FA31F", (casa_x + 30, casa_y + 50, 60, 70))
        pygame.draw.rect(screen, "#4B2E13", (casa_x + 150, casa_y + 70, 80, 130))
        pygame.draw.circle(screen, "#000000", (casa_x + 220, casa_y + 135), 5)

        screen.blit(imagem_coringa, (200, 420))
        texto_render = fonte_coringa.render(texto_coringa, True, "#8A2BE2")
        screen.blit(texto_render, (150, 370))

        texto = fonte_validation.render("ESC para voltar ao menu", True, "black")
        screen.blit(texto, (20, 20))

    elif tela == "forca":
        screen.fill((0, 0, 0))
        escrever_forca(" ".join(palavra_oculta), 50, (255, 255, 255))
        escrever_forca(f"Vidas: {vidas}", 130, (255, 255, 255))
        escrever_forca(f"Letra: {letra}", 210, (255, 255, 255))
        escrever_forca(mensagem_forca, 290, (255, 255, 0))
        escrever_forca("ESC para voltar ao menu", 400, (150, 150, 150))

    elif tela == "ppt":
        screen.fill((0, 0, 0))

        escrever_ppt("Aperte 1, 2 ou 3 para jogar", 50, 20)

        screen.blit(imagem_pedra, (100, 70))
        screen.blit(imagem_papel, (325, 70))
        screen.blit(imagem_tesoura, (550, 70))
        escrever_ppt("1 - Pedra", 110, 225)
        escrever_ppt("2 - Papel", 335, 225)
        escrever_ppt("3 - Tesoura", 550, 225)

        if jogador != "":
            escrever_ppt("Voce", 100, 290)
            screen.blit(imagem_da_jogada(jogador), (100, 325))
            escrever_ppt("Computador", 550, 290)
            screen.blit(imagem_da_jogada(computador), (550, 325))

        escrever_ppt(mensagem_ppt, 50, 500)
        escrever_ppt(f"Placar: Voce {pontos_jogador} x {pontos_computador} Computador", 50, 550)
        escrever_ppt("ESC para voltar ao menu", 50, 620)

    pygame.display.update()

pygame.quit()
