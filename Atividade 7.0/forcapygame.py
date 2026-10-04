import pygame
from random import choice

pygame.init()
tela = pygame.display.set_mode((800, 400))
fonte = pygame.font.SysFont(None, 50)

palavras = ["banana", "maça", "abacaxi", "limao", "mamao", "pera", "melancia", "uva"]
alfabeto = 'abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ'



def sortear_palavra():
    return choice(palavras)
def escrever(texto, y, cor):
    tela.blit(fonte.render(texto, True, cor), (50, y))


vidas = 6
palavra_aleatoria = sortear_palavra()
palavra_oculta = ["_"] * len(palavra_aleatoria)
letra = ""
mensagem = "Digite uma letra e aperte ENTER"
acabou = False

rodando = True
while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if acabou == True:
                if evento.key == pygame.K_n:
                    rodando = False
                if evento.key == pygame.K_s:
                    vidas = 6
                    palavra_aleatoria = sortear_palavra()
                    palavra_oculta = ["_"] * len(palavra_aleatoria)
                    letra = ""
                    mensagem = "Digite uma letra e aperte ENTER"
                    acabou = False
            elif evento.key == pygame.K_BACKSPACE:
                letra = ""
            elif evento.key == pygame.K_RETURN:
                if letra == "":
                    mensagem = "Apenas permitido LETRAS"
                elif letra == palavra_aleatoria:
                    palavra_oculta = list(palavra_aleatoria)
                elif len(letra) == 1 and letra in palavra_aleatoria:
                    mensagem = "Acertou!"
                    for i in range(len(palavra_aleatoria)):
                        if letra == palavra_aleatoria[i]:
                            palavra_oculta[i] = letra
                else:
                    vidas = vidas - 1
                    mensagem = f"Errou!, Voce perdeu um membro resta apenas: {vidas}"
                letra = ""
                if vidas == 0:
                    mensagem = "FIM DE JOGO ! Jogar de novo? (S/N)"
                    acabou = True
                if "_" not in palavra_oculta:
                    mensagem = "Você acertou a palavra! Jogar de novo? (S/N)"
                    acabou = True
            elif evento.unicode != "" and evento.unicode in alfabeto:
                letra = letra + evento.unicode.lower()
            elif evento.unicode != "":
                mensagem = "Apenas permitido LETRAS"

    tela.fill((0, 0, 0))
    escrever(" ".join(palavra_oculta), 50, (255, 255, 255))
    escrever(f"Vidas: {vidas}", 130, (255, 255, 255))
    escrever(f"Letra: {letra}", 210, (255, 255, 255))
    escrever(mensagem, 290, (255, 255, 0))
    pygame.display.flip()

pygame.quit()