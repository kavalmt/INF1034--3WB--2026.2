from random import choice

opcoes = ["pedra", "papel", "tesoura"]
def jogada_computador():
    return choice(opcoes)
def quem_ganhou(jogador, computador):
    if jogador == computador:
        return "empate"
    if (jogador == "pedra" and computador == "tesoura") or (jogador == "tesoura" and computador == "papel") or (jogador == "papel" and computador == "pedra"):
        return "jogador"
    return "computador"


pontos_jogador = 0
pontos_computador = 0

while True:

    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    if jogador not in opcoes:
        print("Opcao invalida!")
        continue
    computador = jogada_computador()
    print(f"Voce jogou {jogador} e o computador jogou {computador}")
    resultado = quem_ganhou(jogador, computador)
    if resultado == "empate":
        print("Empate!")
    elif resultado == "jogador":
        pontos_jogador = pontos_jogador + 1
        print("Voce ganhou!")

    else:
        pontos_computador = pontos_computador + 1
        print("Voce perdeu!")

    print(f"Placar: Voce {pontos_jogador} x {pontos_computador} Computador")

    reiniciar = input("Quer jogar de novo? (s/n): ").lower()
    if reiniciar != "s":
        break