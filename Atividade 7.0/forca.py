from random import choice

palavras = ["banana", "maça", "abacaxi", "limao", "mamao", "pera", "melancia", "uva"]
alfabeto = 'abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ'


def sortear_palavra():
    return choice(palavras)


def so_tem_letras(texto):
    if texto == "":
        return False
    for caractere in texto:
        if caractere not in alfabeto:
            return False
    return True


def mostrar_palavra(palavra_oculta):
    print(" ".join(palavra_oculta))


while True:
    vidas = 6
    palavra_aleatoria = sortear_palavra()
    palavra_oculta = ["_"] * len(palavra_aleatoria)

    while True:
        mostrar_palavra(palavra_oculta)

        letra = input("Digite uma letra da palavra: ").lower()

        if so_tem_letras(letra) == False:
            print("Apenas permitido LETRAS")
            continue

        if len(letra) > 1:
            if letra == palavra_aleatoria:
                print("Você acertou a palavra!")
                mostrar_palavra(palavra_aleatoria)
                break
            vidas = vidas - 1
            print(f"Errou a palavra!, Voce perdeu um membro resta apenas: {vidas} ")
            if vidas == 0:
                print("Voce perdeu todas as suas vidas. FIM DE JOGO ! ")
                break
            continue

        if letra in palavra_aleatoria:

            for i in range(len(palavra_aleatoria)):
                if letra == palavra_aleatoria[i]:
                    palavra_oculta[i] = letra
        else:
            vidas = vidas - 1
            print(f"Errou!, Voce perdeu um membro resta apenas: {vidas} ")
            if vidas == 0:
                print("Voce perdeu todas as suas vidas. FIM DE JOGO ! ")
                break

        if "_" not in palavra_oculta:
            print("Você acertou a palavra!")
            mostrar_palavra(palavra_oculta)
            break
    reiniciar = input("Quer jogar de novo? (s/n): ").lower()
    if reiniciar != "s":
        break
