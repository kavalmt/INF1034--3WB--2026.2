from random import choice

<<<<<<< HEAD
palavras = ["banana", "maça", "abacaxi", "limao", "mamao", "pera", "melancia", "uva"]


def sortear_palavra():
    return choice(palavras)
def mostrar_palavra(palavra):
    print(" ".join(palavra))
def letra_valida(letra):
    if letra == "" or letra not in 'abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ':
        return False
    return True
def revelar_letra(letra, palavra_aleatoria, palavra_oculta):
    for i in range(len(palavra_aleatoria)):
        if letra == palavra_aleatoria[i]:
            palavra_oculta[i] = letra


while True:
    vidas = 6
    palavra_aleatoria = sortear_palavra()
    palavra_oculta = ["_"] * len(palavra_aleatoria)

    while True:
        mostrar_palavra(palavra_oculta)
        letra = input("Digite uma letra da palavra: ").lower()
        if len(letra) > 1:
            if not letra.isalpha():
                print("Apenas permitido LETRAS")
                continue
            if letra == palavra_aleatoria:
                print("Você acertou a palavra!")
                mostrar_palavra(palavra_aleatoria)
                break
            vidas = vidas - 1
            print(f"Errou a palavra! Voce perdeu um membro resta apenas: {vidas} ")
            if vidas == 0:
                print("Voce perdeu todas as suas vidas. fim de jogo ! ")
                break
            continue
        if letra_valida(letra) == False:
            print("Apenas permitido LETRAS")
            continue

        if letra in palavra_aleatoria:
            revelar_letra(letra, palavra_aleatoria, palavra_oculta)
        else:
            vidas = vidas - 1
            print(f"Errou!, Voce perdeu um membro resta apenas: {vidas} ")
            if vidas == 0:
                print("Voce perdeu todas as suas vidas. fim de jogo! ")
                break

        if "_" not in palavra_oculta:
            print("Você acertou a palavra!")
            mostrar_palavra(palavra_oculta)
            break

    reiniciar = input("Quer jogar de novo? (S/n): ").lower()
    if reiniciar != "s":
        break
=======
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
>>>>>>> 71055a309ec72ccd9b661a6344a0daa69a3108ea
