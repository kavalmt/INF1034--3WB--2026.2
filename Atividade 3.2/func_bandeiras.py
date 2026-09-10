
from turtle import *
from time import sleep

t = Turtle()
t.speed(0)

def desenha_retangulo(x, y, larg, alt, cor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()

def desenha_circulo(x, y, raio, cor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

def desenha_estrela(x, y, tamanho, cor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(5):
        t.fd(tamanho)
        t.rt(144)
    t.end_fill()


def intervalo():
    t.pu()
    t.goto(0, 0)
    sleep(2)
    t.clear()
    t.pd()

def desenha_bandeira_japao():
    desenha_retangulo(-125, 100, 250, 200, "white")
    desenha_circulo(0, -60, 60, "#BC002C")


def desenha_bandeira_irlanda():
    desenha_retangulo(-125, 100, 83.3, 200, "#179B62")
    desenha_retangulo(-41.7, 100, 83.3, 200, "white")
    desenha_retangulo(41.6, 100, 83.3, 200, "#FF883D")


def desenha_bandeira_botswana():
    cores = ["#75AADB", "white", "black", "white", "#75AADB"]
    alturas = [66, 22, 24, 22, 66]
    y = 100

    for i in range(5):
        desenha_retangulo(-125, y, 250, alturas[i], cores[i])
        y -= alturas[i]

def desenha_bandeira_costa_rica():
    cores = ["#1F255E", "white", "#CE4652", "white", "#1F255E"]
    alturas = [33.3, 33.3, 66.6, 33.3, 33.3]
    y = 100
    for i in range(5):
        desenha_retangulo(-125, y, 250, alturas[i], cores[i])
        y -= alturas[i]


def desenha_bandeira_chile():
    desenha_retangulo(-125, 100, 250, 100, "white")
    desenha_retangulo(-125, 0, 250, 100, "#D52B1E")
    desenha_retangulo(-125, 100, 83, 100, "#0039A6")
    desenha_estrela(-95, 65, 20, "white")


def desenha_bandeira_panama():
    desenha_retangulo(-125, 100, 125, 100, "white")
    desenha_retangulo(0, 100, 125, 100, "#DA121A")
    desenha_retangulo(-125, 0, 125, 100, "#0033A0")
    desenha_retangulo(0, 0, 125, 100, "white")
    desenha_estrela(-72, 45, 18, "#0033A0")
    desenha_estrela(52, -55, 18, "#DA121A")


def desenha_bandeira_cuba():
    cores = ["#002A8F", "white", "#002A8F", "white", "#002A8F"]
    alturas = [40, 40, 40, 40, 40]
    y = 100
    for i in range(5):
        desenha_retangulo(-125, y, 250, alturas[i], cores[i])
        y -= alturas[i]
    t.pu()
    t.goto(-125, 100)
    t.pd()
    t.fillcolor("#CE1126")
    t.begin_fill()
    t.goto(-125, -100)
    t.goto(-45, 0)
    t.goto(-125, 100)
    t.end_fill()
    desenha_estrela(-105, 8, 15, "white")


def desenha_bandeira_siria():
    cores = ["#CE1126", "white", "black"]
    alturas = [66.6, 66.6, 66.6]
    y = 100
    for i in range(3):
        desenha_retangulo(-125, y, 250, alturas[i], cores[i])
        y -= alturas[i]

    desenha_estrela(-30, 10, 18, "#007A3D")
    desenha_estrela(10, 10, 18, "#007A3D")


def desenha_bandeira_georgia():
    desenha_retangulo(-125, 100, 250, 200, "white")

    desenha_retangulo(-12.5, 100, 25, 200, "#FF0000")
    desenha_retangulo(-125, 12.5, 250, 25, "#FF0000")

    desenha_retangulo(-66.5, 65, 8, 30, "#FF0000")
    desenha_retangulo(-77.5, 54, 30, 8, "#FF0000")

    desenha_retangulo(58.5, 65, 8, 30, "#FF0000")
    desenha_retangulo(47.5, 54, 30, 8, "#FF0000")

    desenha_retangulo(-66.5, -35, 8, 30, "#FF0000")
    desenha_retangulo(-77.5, -46, 30, 8, "#FF0000")

    desenha_retangulo(58.5, -35, 8, 30, "#FF0000")
    desenha_retangulo(47.5, -46, 30, 8, "#FF0000")


def desenha_bandeira_grecia():
    altura = 200 / 9
    y = 100
    for i in range(9):
        if i % 2 == 0:
            cor = "#0D5EAF"
        else:
            cor = "white"
        desenha_retangulo(-125, y, 250, altura, cor)
        y -= altura
    canto = altura * 5
    desenha_retangulo(-125, 100, canto, canto, "#0D5EAF")
    desenha_retangulo(
        -125 + canto / 2 - canto / 10,
        100,
        canto / 5,
        canto,
        "white" )
    desenha_retangulo(
        -125,
        100 - canto / 2 - canto / 10,
        canto,
        canto / 5,
        "white"
    )


def desenha_bandeira_cambodia():
    desenha_retangulo(-125, 100, 250, 50, "#032EA1")
    desenha_retangulo(-125, 50, 250, 100, "#E00025")
    desenha_retangulo(-125, -50, 250, 50, "#032EA1")
    t.pu()
    t.goto(-45, -30)
    t.pd()
    t.fillcolor("#E5E5E5")
    t.begin_fill()

    t.goto(-45, -15)
    t.goto(-35, -15)
    t.goto(-35, -5)
    t.goto(-25, -5)
    t.goto(-25, 5)
    t.goto(-20, 20)
    t.goto(-15, 5)
    t.goto(-9, 5)
    t.goto(-9, 15)
    t.goto(-5, 25)
    t.goto(0, 32)
    t.goto(5, 25)
    t.goto(9, 15)
    t.goto(9, 5)
    t.goto(15, 5)
    t.goto(20, 20)
    t.goto(25, 5)
    t.goto(25, -5)
    t.goto(35, -5)
    t.goto(35, -15)
    t.goto(45, -15)
    t.goto(45, -30)
    t.goto(-45, -30)
    t.end_fill()

bandeira = textinput("Bandeiras","Escolha uma bandeira:\n\n"
    "japao\n" "irlanda\n" "botswana\n" "costa rica\n" "chile\n" "panama\n" "cuba\n" "siria\n"
    "georgia\n""grecia\n"
"cambodia")

if bandeira == "japao":
    desenha_bandeira_japao()
elif bandeira == "irlanda":
    desenha_bandeira_irlanda()
elif bandeira == "botswana":
    desenha_bandeira_botswana()
elif bandeira == "costa rica":
    desenha_bandeira_costa_rica()
elif bandeira == "chile":
    desenha_bandeira_chile()
elif bandeira == "panama":
    desenha_bandeira_panama()
elif bandeira == "cuba":
    desenha_bandeira_cuba()
elif bandeira == "siria":
    desenha_bandeira_siria() 
elif bandeira == "georgia":
    desenha_bandeira_georgia()
elif bandeira == "grecia":
    desenha_bandeira_grecia()
elif bandeira == "cambodia":
    desenha_bandeira_cambodia()

mainloop()

