from random import choice

vidas = 6
palavras = ["banana", "maça", "abacaxi", "limao", "mamao", "pera", "melancia", "uva"]

palavra_aleatoria = choice(palavras)
palavra_oculta = ["_"] * len(palavra_aleatoria)

while True:

    print(" ".join(palavra_oculta))

    letra = input("Digite uma letra da palavra: ")
    if letra not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print("Apenas permitido LETRAS")
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

    if "_" not in palavra_oculta:
        print("Você acertou a palavra!")
        print(" ".join(palavra_oculta))
        break
