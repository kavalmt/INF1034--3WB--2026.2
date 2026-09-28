from random import choice

palavras = ["banana", "maça", "abacaxi", "limao", "mamao", "pera", "melancia", "uva"]

palavra_aleatoria = choice(palavras)
palavra_oculta = "_ " * len(palavra_aleatoria)

print(palavra_oculta)

letra = input("Digite uma letra da palavra: ")

if letra in palavra_aleatoria:
    palavra_aux = ""
    for i in range(len(palavra_aleatoria)):
        if letra == palavra_aleatoria[i]:
            palavra_aux += letra + " "
        else:
            palavra_aux += "_ "

    palavra_oculta = palavra_aux
else:
    print("Errou!")

print(palavra_oculta)
