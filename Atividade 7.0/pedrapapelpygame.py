import pygame
from random import choice

pygame.init()
tela = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Pedra, Papel e Tesoura")
fonte = pygame.font.SysFont(None, 40)
imagem_pedra = pygame.image.load("Atividade 7.0/pedra.png")
imagem_papel = pygame.image.load("Atividade 7.0/papel.png")
imagem_tesoura = pygame.image.load("Atividade 7.0/tesoura.png")

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


def escrever(texto, x, y):
    tela.blit(fonte.render(texto, True, (255, 255, 255)), (x, y))


pontos_jogador = 0
pontos_computador = 0
jogador = ""
computador = ""
mensagem = "Escolha a sua jogada"

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            escolha = ""
            if evento.key == pygame.K_1:
                escolha = "pedra"
            elif evento.key == pygame.K_2:
                escolha = "papel"
            elif evento.key == pygame.K_3:
                escolha = "tesoura"
            elif evento.key == pygame.K_r:
                pontos_jogador = 0
                pontos_computador = 0
                jogador = ""
                computador = ""
                mensagem = "Jogo reiniciado! Escolha a sua jogada"
            if escolha != "":
                jogador = escolha
                computador = jogada_computador()
                resultado = quem_ganhou(jogador, computador)
                if resultado == "empate":
                    mensagem = "Empate!"
                elif resultado == "jogador":
                    pontos_jogador = pontos_jogador + 1
                    mensagem = "Voce ganhou!"
                else:
                    pontos_computador = pontos_computador + 1
                    mensagem = "Voce perdeu!"
    tela.fill((0, 0, 0))

    escrever("Aperte 1, 2 ou 3 para jogar e R para reiniciar", 50, 20)

    tela.blit(imagem_pedra, (100, 70))
    tela.blit(imagem_papel, (325, 70))
    tela.blit(imagem_tesoura, (550, 70))
    escrever("1 - Pedra", 110, 225)
    escrever("2 - Papel", 335, 225)
    escrever("3 - Tesoura", 550, 225)

    if jogador != "":
        escrever("Voce", 100, 290)
        tela.blit(imagem_da_jogada(jogador), (100, 325))
        escrever("Computador", 550, 290)
        tela.blit(imagem_da_jogada(computador), (550, 325))

    escrever(mensagem, 50, 500)
    escrever(f"Placar: Voce {pontos_jogador} x {pontos_computador} Computador", 50, 550)

    pygame.display.flip()
pygame.quit()